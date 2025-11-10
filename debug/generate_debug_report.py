# Author: ChatGPT (patched)
# Purpose: Parse mteh.txt and verify formatting of Chinese character entries, outputting a concise categorized Markdown debug report

import re
from collections import defaultdict
from datetime import datetime

file_path = "../mteh.txt"
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

import re

# Expanded regex allowing accented vowels and ü variants
PINYIN_RE = re.compile(r"^[a-zA-ZüÜǎáàāǍÁÀĀěéèēĚÉÈĒǐíìīǏÍÌĪǒóòōǑÓÒŌǔúùūǓÚÙŪǚǜǘǖǙǛǗǕńňḿ]+$")

# For detecting tone-marked vowels
TONE_VOWELS = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛ"

def check_pinyin_format(pinyin):
    """Return error message if invalid or tone count mismatch."""
    if not PINYIN_RE.fullmatch(pinyin):
        return "Unexpected characters in pinyin"

    # Split by spaces or syllables
    syllables = pinyin.split()
    for s in syllables:
        tone_marks = sum(c in TONE_VOWELS for c in s)
        if tone_marks == 0:
            return f"Missing tone mark in syllable '{s}'"
        elif tone_marks > 1:
            return f"Multiple tone marks in syllable '{s}'"
    return None

# Helper functions
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

# Initialize counters, sets, and warning collectors
previous_char_code = None
previous_char = None
seen_hints = {}
hsk_counts = defaultdict(int)
structure_counts = defaultdict(int)
hint_length_counts = defaultdict(int)
characters_set = set()
hint_characters_set = set()
variant_characters = set()
two_char_hint_chars = set()
capital_pinyin_chars = set()
error_characters = set()
unicode_out_of_order = []
duplicate_characters = defaultdict(list)

valid_hsk = set(["1","2","3","4","5","6","+","n"])
valid_structure = set([str(i) for i in range(0,13)] + ["none"])

# Warning collectors
duplicate_hints = defaultdict(list)
frequency_issues = {}
hsk_issues = {}
structure_issues = {}
hint_content_issues = {}
unicode_issues = {}
variant_map = {}

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

        # Frequency check
        if not freq.isdigit():
            frequency_issues[char] = freq

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

        # example explicit class — covers a lot of common pinyin diacritics
        pinyin_re = re.compile(r"^[A-Za-záÁàÀǎǍāĀéÉèÈêÊěĚēĒíÍìÌǐǏīĪóÓòÒǒǑōŌúÚùÙǔǓüÜǘǗǜǛǚǙǖǕūŪ]+$")
        if not pinyin_re.fullmatch(pinyin):
            hsk_issues[char] = f"Unexpected chars in pinyin: {pinyin}"

        # Collect characters with frequency = 'n'
        freq_n_chars = [e["char"] for e in entries if e["frequency"].lower() == "n"]

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
        dupes = [c for c, lines in duplicate_characters.items() if len(lines) > 1]
        md.write(f"- Duplicate characters: {len(dupes)}\n")
    else:
        md.write("- No duplicate characters found ✅\n")

    if error_characters:
        md.write(f"- Lines with missing or malformed fields: {len(error_characters)}\n")
    else:
        md.write("- All lines have 6 complete fields ✅\n")

    invalid_pinyin = [c for c, val in hsk_issues.items() if "Unexpected chars in pinyin" in val]
    if invalid_pinyin:
        md.write(f"- Unexpected characters in pinyin: {len(invalid_pinyin)} ({' '.join(sorted(invalid_pinyin))})\n")
    else:
        md.write("- All pinyin fields valid ✅\n")
    md.write("\n")

    # --- REST OF REPORT ---
    if variant_characters:
        md.write(f"## [ {len(variant_characters)} ] Variant Characters\n")
        md.write("\n".join(f"- {v} → {variant_map[v]}" for v in sorted(variant_characters)) + "\n\n")

    if capital_pinyin_chars:
        md.write(f"## [ {len(capital_pinyin_chars)} ] Characters with Capitalized Pinyin\n")
        md.write("  " + " ".join(sorted(capital_pinyin_chars)) + "\n\n")

    if frequency_issues:
        md.write(f"## [ {len(frequency_issues)} ] Frequency Issues\n")
        for char, val in sorted(frequency_issues.items()):
            md.write(f"- Character '{char}': Frequency not numeric: {val}\n")
        md.write("\n")

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

    if freq_n_chars:
        md.write(f"## [ {len(freq_n_chars)} ] MetH characters not included in Jun Da corpus\n")
        md.write("  " + " ".join(sorted(freq_n_chars)) + "\n\n")

# --- JUN DA CORPUS CHECK ---
jun_da_path = "../sources/JunDa/JunDa_modern_chars_original_order.txt"
try:
    with open(jun_da_path, "r", encoding="utf-8") as j:
        jun_da_text = j.read()

    # Extract Chinese characters (U+4E00 to U+9FFF) preserving order
    jun_da_chars = []
    for c in jun_da_text:
        if '\u4e00' <= c <= '\u9fff' and c not in jun_da_chars:
            jun_da_chars.append(c)

    # Compare against MteH characters
    missing_from_mteh = [c for c in jun_da_chars if c not in characters_set]
    top_missing = missing_from_mteh[:100]

    with open(output_md, "a", encoding="utf-8") as md:
        md.write(f"## [ {len(top_missing)} ] Characters in Jun Da corpus not in MteH\n")
        if top_missing:
            md.write("  " + " ".join(top_missing) + "\n\n")
        else:
            md.write("All top Jun Da characters are present in MteH ✅\n\n")

except FileNotFoundError:
    with open(output_md, "a", encoding="utf-8") as md:
        md.write("## Jun Da Corpus Check\n\n⚠️ File not found: ../sources/JunDa/JunDa_chars_original_order.txt\n\n")

print(f"Markdown debug report written to {output_md}")

