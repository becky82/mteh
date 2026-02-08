# Author: ChatGPT (patched)
# Purpose: Parse mteh.txt and verify formatting of Chinese character entries,
#          outputting a concise categorized Markdown debug report,
#          with Jun Da frequency consistency check.

import re
from collections import defaultdict
from datetime import datetime

file_path = "../mteh.txt"
jun_da_path = "../sources/JunDa/JunDa_modern_chars_original_order.txt"
output_md = "debug_report.md"

entries = []

# Regular expressions
chinese_char_re = re.compile(r'[\u4e00-\u9fff]')
chinese_or_punct_re = re.compile(
    r'['
    r'\u4e00-\u9fff'
    r'\u3000-\u303F'
    r'\uFF00-\uFFEF'
    r'\u2000-\u206F'
    r'\u00B7'
    r']'
)

# Expanded regex allowing accented vowels and ü variants
PINYIN_RE = re.compile(r"^[a-zA-ZüÜǎáàāǍÁÀĀěéèēĚÉÈĒǐíìīǏÍÌĪǒóòōǑÓÒŌǔúùūǓÚÙŪǚǜǘǖǙǛǗǕńňḿ]+$")

# For detecting tone-marked vowels
TONE_VOWELS = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛ"

def check_pinyin_format(pinyin):
    """Return error message if invalid or tone count mismatch."""
    if not PINYIN_RE.fullmatch(pinyin):
        return "Unexpected characters in pinyin"

    syllables = pinyin.split()
    for s in syllables:
        tone_marks = sum(c in TONE_VOWELS for c in s)
        if tone_marks == 0:
            return f"Missing tone mark in syllable '{s}'"
        elif tone_marks > 1:
            return f"Multiple tone marks in syllable '{s}'"
    return None

def is_variant_hint(hint: str) -> bool:
    if not hint:
        return False
    h = hint.strip()
    if h == "变体":
        return True
    if re.search(r'\bvariant\b', h, flags=re.IGNORECASE):
        return True
    if h.lower().startswith("variant"):
        return True
    return False

# --- LOAD JUN DA CORPUS FOR FREQUENCY CHECK ---
jun_da_map = {}
try:
    with open(jun_da_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, 1):  # line numbers start at 1
            c = line.strip()
            if c:
                jun_da_map[c] = idx
except FileNotFoundError:
    print(f"⚠️ Jun Da file not found: {jun_da_path}")

# --- Initialize counters, sets, and warning collectors ---
previous_char_code = None
previous_char = None
seen_hints = {}
hsk_counts = defaultdict(int)
structure_counts = defaultdict(int)
hint_length_counts = defaultdict(int)
characters_set = set()
hint_characters_set = set()
variant_characters = set()
capital_pinyin_chars = set()
error_characters = set()
unicode_out_of_order = []
duplicate_characters = defaultdict(list)

valid_hsk = set(["1","2","3","4","5","6","+","n"])
valid_structure = set([str(i) for i in range(0,13)] + ["none"])

# Warning collectors
duplicate_hints = defaultdict(list)
frequency_issues = {}
high_frequency_chars = {}  # freq >=5000
hsk_issues = {}
structure_issues = {}
hint_content_issues = {}
unicode_issues = {}
variant_map = {}
seen_frequencies = set()  # track distinct frequencies

# --- PARSE FILE ---
with open(file_path, "r", encoding="utf-8") as f:
    for line_no, line in enumerate(f, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split()

        if len(parts) == 5 and parts[2].lower() == "variant":
            parts.append("none")

        if len(parts) != 6 or any(p.strip() == "" for p in parts):
            error_char = parts[0] if parts else '?'
            hsk_issues[error_char] = f"Incorrect or incomplete fields (got {len(parts)})"
            error_characters.add(error_char)
            continue

        char, pinyin, hint, freq, hsk, structure = parts
        characters_set.add(char)

        if char in duplicate_characters:
            duplicate_characters[char].append(line_no)
        else:
            duplicate_characters[char] = [line_no]

        # Pinyin check
        err = check_pinyin_format(pinyin)
        if err:
            hint_content_issues[char] = (hint_content_issues.get(char, "") + "; " + err).strip("; ")

        # --- Frequency check (distinct, 1-9933) ---
        if not freq.isdigit():
            frequency_issues[char] = f"Not a number: {freq}"
        else:
            freq_value = int(freq)
            if not (1 <= freq_value <= 9933):
                frequency_issues[char] = f"Out of range (1-9933): {freq_value}"
            elif freq_value in seen_frequencies:
                frequency_issues[char] = f"Duplicate frequency: {freq_value}"
            else:
                seen_frequencies.add(freq_value)

            # High frequency warning
            if freq_value >= 5000:
                high_frequency_chars[char] = freq_value

            # --- Jun Da consistency check ---
            jun_da_line = jun_da_map.get(char)
            if jun_da_line is not None and freq_value != jun_da_line:
                frequency_issues[char] = frequency_issues.get(char, "") + f"Jun Da line {jun_da_line} mismatch"

        # HSK check
        if hsk not in valid_hsk:
            hsk_issues[char] = hsk
        hsk_counts[hsk] += 1

        # Structure check
        if structure not in valid_structure:
            structure_issues[char] = structure
        structure_counts[structure] += 1

        # Pinyin capitalization
        if pinyin and pinyin[0].isupper():
            capital_pinyin_chars.add(char)

        # Variant detection
        if is_variant_hint(hint):
            if previous_char:
                variant_map[char] = previous_char
            else:
                variant_map[char] = "?"
            variant_characters.add(char)
            skip_unicode_check = True
        else:
            skip_unicode_check = False

            # Duplicate hints
            if hint in seen_hints:
                duplicate_hints[hint].append(char)
                duplicate_hints[hint].append(seen_hints[hint])
            else:
                seen_hints[hint] = char

            # Hint content checks
            non_chinese_chars = [c for c in hint if not chinese_or_punct_re.match(c)]
            chinese_chars_in_hint = chinese_char_re.findall(hint)
            hint_characters_set.update(chinese_chars_in_hint)
            hint_len = len(chinese_chars_in_hint)
            hint_length_counts[hint_len] += 1

            content_issues = []
            if non_chinese_chars:
                content_issues.append("non-Chinese chars/punctuation: " + ''.join(non_chinese_chars))
            if hint_len not in (2,3,4):
                content_issues.append(f"hint length {hint_len} unexpected")
            if content_issues:
                hint_content_issues[char] = "; ".join(content_issues)

        # Unicode order check
        if not skip_unicode_check:
            try:
                char_code = ord(char)
                if previous_char_code and char_code < previous_char_code:
                    unicode_issues[char] = f"Unicode out of sequence (U+{char_code:X})"
                    unicode_out_of_order.append(char)
                previous_char_code = char_code
            except TypeError:
                unicode_issues[char] = "Cannot determine Unicode code point"

        if not is_variant_hint(hint):
            previous_char = char

        entries.append({
            "char": char,
            "pinyin": pinyin,
            "hint": hint,
            "frequency": freq,
            "hsk": hsk,
            "structure": structure
        })

# --- SANITY CHECKS ---
missing_in_hint = [
    e["char"]
    for e in entries
    if e["char"] not in e["hint"] and not is_variant_hint(e["hint"])
]
invalid_hsk = [e["char"] for e in entries if e["hsk"] not in valid_hsk]
invalid_structure = [e["char"] for e in entries if e["structure"] not in valid_structure]

# --- WRITE MARKDOWN REPORT ---
with open(output_md, "w", encoding="utf-8") as md:
    md.write(f"# MteH Debug Report\n\n")
    md.write(f"_Generated on {datetime.now()}_\n\n")
    md.write(f"_Generated using Python code generated by ChatGPT_\n\n")
    md.write(f"**Total characters parsed:** {len(entries)}\n\n")

    # --- SANITY CHECK SECTION ---
    md.write("## Integrity Checks\n\n")
    md.write(f"- Characters appearing in their hints: "
             f"{'✅ OK' if not missing_in_hint else f'❌ {len(missing_in_hint)} missing'}\n")
    if missing_in_hint:
        md.write("  - " + " ".join(sorted(missing_in_hint)) + "\n")
    md.write(f"- Valid HSK values: "
             f"{'✅ OK' if not invalid_hsk else f'❌ {len(invalid_hsk)} invalid'}\n")
    if invalid_hsk:
        md.write("  - " + " ".join(sorted(invalid_hsk)) + "\n")
    md.write(f"- Valid structure values: "
             f"{'✅ OK' if not invalid_structure else f'❌ {len(invalid_structure)} invalid'}\n")
    if invalid_structure:
        md.write("  - " + " ".join(sorted(invalid_structure)) + "\n")

    if duplicate_characters:
        dupes = {c: lines for c, lines in duplicate_characters.items() if len(lines) > 1}
        md.write(f"- Duplicate characters: {len(dupes)}\n")
        if dupes:
            for char, lines in sorted(dupes.items()):
                md.write(f"  - Character '{char}' on lines: {', '.join(map(str, lines))}\n")
    else:
        md.write("- No duplicate characters found ✅\n")

    if error_characters:
        md.write(f"- Lines with missing or malformed fields: {len(error_characters)}\n")
    else:
        md.write("- All lines have 6 complete fields ✅\n")

    md.write("\n")

    # --- VARIANTS, CAPITALS, DUPLICATES ---
    if variant_characters:
        md.write(f"## [ {len(variant_characters)} ] Variant Characters\n")
        md.write("\n".join(f"- {v} → {variant_map[v]}" for v in sorted(variant_characters)) + "\n\n")

    if capital_pinyin_chars:
        md.write(f"## [ {len(capital_pinyin_chars)} ] Characters with Capitalized Pinyin\n")
        md.write("  " + " ".join(sorted(capital_pinyin_chars)) + "\n\n")

    # --- FREQUENCY REPORTS ---
    md.write(f"## [ {len(frequency_issues)} ] Frequency Errors\n")
    if frequency_issues:
        for char, val in sorted(frequency_issues.items()):
            md.write(f"- Character '{char}': {val}\n")
    else:
        md.write("No frequency errors ✅\n")
    md.write("\n")

    md.write(f"## [ {len(high_frequency_chars)} ] High Frequency Warning (≥5000)\n")
    if high_frequency_chars:
        # One-line per character, sorted by frequency descending
        md.write("  " + " ".join(f"{char}({val})" for char, val in sorted(high_frequency_chars.items(), key=lambda x: x[1], reverse=False)) + "\n")
    else:
        md.write("No characters with frequency ≥5000 ✅\n")
    md.write("\n")

    # --- HSK, STRUCTURE, HINT, UNICODE, DUPLICATE HINTS ---
    if hsk_issues:
        md.write(f"## [ {len(hsk_issues)} ] HSK Issues\n")
        for char, val in sorted(hsk_issues.items()):
            md.write(f"- Character '{char}': HSK level unexpected: {val}\n")
        md.write("\n")

    if structure_issues:
        md.write(f"## [ {len(structure_issues)} ] Structure Issues\n")
        for char, val in sorted(structure_issues.items()):
            md.write(f"- Character '{char}': Structure code unexpected: {val}\n")
        md.write("\n")

    if hint_content_issues:
        md.write(f"## [ {len(hint_content_issues)} ] Hint Content Issues\n")
        for char, val in sorted(hint_content_issues.items()):
            md.write(f"- Character '{char}': {val}\n")
        md.write("\n")

    if unicode_issues:
        md.write(f"## [ {len(unicode_issues)} ] Unicode Order Issues\n")
        for char, val in sorted(unicode_issues.items()):
            md.write(f"- Character '{char}': {val}\n")
        md.write("\n")

    extra_hint_chars = hint_characters_set - characters_set
    if extra_hint_chars:
        md.write(f"## [ {len(extra_hint_chars)} ] Characters in Hints but not in 'character' Field\n")
        md.write("  " + " ".join(sorted(extra_hint_chars)) + "\n\n")

    if duplicate_hints:
        md.write(f"## [ {len(duplicate_hints)} ] Duplicate Hints\n")
        for hint, chars in duplicate_hints.items():
            unique_chars = sorted(set(chars))
            md.write(f"- Hint '{hint}': {', '.join(unique_chars)}\n")
        md.write("\n")

print(f"Markdown debug report written to {output_md}")

