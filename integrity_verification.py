# Author: ChatGPT (patched)
# Purpose: Parse mteh.txt and verify full formatting of Chinese character entries
import re
from collections import defaultdict

file_path = "mteh.txt"

entries = []

# Regular expression to match Chinese characters (basic CJK Unified Ideographs)
chinese_char_re = re.compile(r'[\u4e00-\u9fff]')

previous_char_code = None
seen_hints = set()
hsk_counts = defaultdict(int)
hint_length_counts = defaultdict(int)
structure_counts = defaultdict(int)
characters_set = set()
hint_characters_set = set()
error_characters = set()
variant_characters = set()
two_char_hint_chars = set()

unicode_out_of_order = []

# Allowed values
valid_hsk = set(["1","2","3","4","5","6","+","n"])
valid_structure = set([str(i) for i in range(1,14)] + ["none"])

# helper: robust variant detection (accept variant, Variant, (variant), 变体, etc.)
def is_variant_hint(hint: str) -> bool:
    if not hint:
        return False
    h = hint.strip()
    # exact Chinese common word
    if h == "变体":
        return True
    # word boundary search for 'variant' ignoring case, also allow parentheses etc.
    if re.search(r'\bvariant\b', h, flags=re.IGNORECASE):
        return True
    # allow short markers like "variant:" or "(variant)"
    if h.lower().startswith("variant"):
        return True
    return False

with open(file_path, "r", encoding="utf-8") as f:
    for line_no, line in enumerate(f, 1):
        raw = line
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split()

        # Allow 5-field "variant" lines by appending structure='none'
        if len(parts) == 5 and parts[2].lower() == "variant":
            parts.append("none")

        if len(parts) != 6:
            print(f"Line {line_no}: ERROR - Character '{parts[0] if parts else '?'}': Incorrect number of fields ({len(parts)} instead of 6)")
            if parts:
                error_characters.add(parts[0])
            continue

        char, pinyin, hint, freq, hsk, structure = parts
        characters_set.add(char)

        # Validate frequency
        if not freq.isdigit():
            print(f"Line {line_no}: WARNING - Character '{char}': Frequency '{freq}' is not numeric")

        # Validate HSK level
        if hsk not in valid_hsk:
            print(f"Line {line_no}: WARNING - Character '{char}': HSK level '{hsk}' is unexpected")
        hsk_counts[hsk] += 1

        # Validate structure
        if structure not in valid_structure:
            print(f"Line {line_no}: WARNING - Character '{char}': Structure code '{structure}' is unexpected")
        structure_counts[structure] += 1

        # Detect variant hints robustly
        if is_variant_hint(hint):
            print(f"Line {line_no}: WARNING - Character '{char}': Hint indicates variant ('{hint}')")
            variant_characters.add(char)
            skip_unicode_check = True
        else:
            skip_unicode_check = False

            # Check character appears in hint
            if char not in hint:
                print(f"Line {line_no}: ERROR - Character '{char}': not found in hint '{hint}'")
                error_characters.add(char)

            # Collect Chinese characters in hint
            chinese_chars_in_hint = chinese_char_re.findall(hint)
            for c in chinese_chars_in_hint:
                hint_characters_set.add(c)

            hint_len = len(chinese_chars_in_hint)
            if hint_len in (2,3,4):
                hint_length_counts[hint_len] += 1

            if not (2 <= hint_len <= 4):
                print(f"Line {line_no}: WARNING - Character '{char}': Hint '{hint}' contains {hint_len} Chinese characters (expected 2–4)")


            if hint_len == 2:
                print(f"Line {line_no}: WARNING - Character '{char}': Hint contains exactly 2 Chinese characters")
                two_char_hint_chars.add(char)

            # Warn for non-Chinese characters
            non_chinese_chars = [c for c in hint if not chinese_char_re.match(c)]
            sample = ''.join(non_chinese_chars).strip()
            if sample:
                print(f"Line {line_no}: WARNING - Character '{char}': Hint '{hint}' contains non-Chinese characters or punctuation: {sample}")

            # Duplicate hint check
            if hint in seen_hints:
                print(f"Line {line_no}: WARNING - Character '{char}': Duplicate hint detected: '{hint}'")
            else:
                seen_hints.add(hint)

        # Unicode order check (skip variants)
        if not skip_unicode_check:
            try:
                char_code = ord(char)
                if previous_char_code is not None and char_code < previous_char_code:
                    print(f"Line {line_no}: WARNING - Character '{char}': Unicode order out of sequence (U+{char_code:X})")
                    unicode_out_of_order.append(char)  # <-- store it
                previous_char_code = char_code  # Only update for non-variant
            except TypeError:
                print(f"Line {line_no}: WARNING - Character '{char}': cannot determine Unicode code point")

        # Add entry to list
        entries.append({
            "char": char,
            "pinyin": pinyin,
            "hint": hint,
            "frequency": freq,
            "hsk": hsk,
            "structure": structure
        })


# Totals and stats
total_chars = len(entries)
print(f"\nParsed {total_chars} characters successfully.\n")

print("HSK level counts:")
for level in sorted(hsk_counts.keys()):
    print(f"  HSK {level}: {hsk_counts[level]} characters")

print("\nHint length counts (number of Chinese characters):")
for length in sorted(hint_length_counts.keys()):
    print(f"  {length}-character hints: {hint_length_counts[length]}")

print("\nCharacter structure counts:")
numeric_structs = [s for s in structure_counts.keys() if s.isdigit()]
numeric_structs_sorted = sorted(numeric_structs, key=int)
for struct in numeric_structs_sorted:
    print(f"  Structure {struct}: {structure_counts[struct]} characters")
if 'none' in structure_counts:
    print(f"  Structure none: {structure_counts['none']} characters")

# Variant characters summary
if variant_characters:
    print("\nCharacters marked as variants:")
    print("  " + " ".join(sorted(variant_characters)))
else:
    print("\nNo variant characters found.")

# Find characters that appear in hints but not in main characters
extra_hint_chars = hint_characters_set - characters_set
if extra_hint_chars:
    print("\nCharacters appearing in hints but not in the 'character' field:")
    print("  " + " ".join(sorted(extra_hint_chars)))
else:
    print("\nAll hint characters also appear in the main 'character' field.")

# List characters that were out of Unicode order
if unicode_out_of_order:
    print("\nCharacters with Unicode order issues:")
    print("  " + " ".join(unicode_out_of_order))
else:
    print("\nNo characters had Unicode order issues.")

# Characters with 2-character hints
if two_char_hint_chars:
    print("\nCharacters with exactly 2-character hints:")
    print("  " + " ".join(sorted(two_char_hint_chars)))
else:
    print("\nNo characters had exactly 2-character hints.")

# List characters that caused errors
if error_characters:
    print("\nCharacters that caused ERRORS (need proofreading):")
    print("  " + " ".join(sorted(error_characters)))
else:
    print("\nNo characters caused errors.")

