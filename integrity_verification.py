# Author: ChatGPT
# Purpose: Parse mteh.txt and verify full formatting of Chinese character entries
# Checks:
# 1. Six fields per line (error if not)
# 2. Character appears in hint (except when hint is 'variant') – warning
# 3. Hint contains 2–4 Chinese characters (except 'variant') – warning
# 4. Hint contains only Chinese characters (warn if punctuation or other symbols; skip 'variant')
# 5. Warn if characters are not in Unicode ascending order
# 6. Warn if a hint is duplicated
# 7. Warn if hint is 'variant' (not an error)
# 8. Validate frequency, HSK level, and structure values – warning
# Additional: Count number of characters per HSK level, hint length, structure
# Additional: Report characters that appear in hints, but not in the "character" field
# Tracks characters causing errors for end-of-file summary
# Structure counts now sorted numerically 1–13, 'none' last

import re
from collections import defaultdict

file_path = "mteh.txt"

entries = []

# Regular expression to match Chinese characters
chinese_char_re = re.compile(r'[\u4e00-\u9fff]')

previous_char_code = None  # Track Unicode code of previous character
seen_hints = set()         # Track all hints to detect duplicates
hsk_counts = defaultdict(int)          # Count characters per HSK level
hint_length_counts = defaultdict(int)  # Count of 2-,3-,4-character hints
structure_counts = defaultdict(int)    # Count characters per structure code
characters_set = set()                  # Characters appearing in first field
hint_characters_set = set()             # All Chinese characters appearing in hints
error_characters = set()                # Track characters that caused errors

# Allowed values
valid_hsk = set(["1","2","3","4","5","6","+","n"])
valid_structure = set([str(i) for i in range(1,14)] + ["none"])

with open(file_path, "r", encoding="utf-8") as f:
    for line_no, line in enumerate(f, 1):
        line = line.strip()
        
        # Skip blank lines or comments
        if not line or line.startswith("#"):
            continue
        
        parts = line.split()
        
        # Check for exactly six fields
        if len(parts) != 6:
            print(f"Line {line_no}: ERROR - Character '{parts[0] if parts else '?'}': Incorrect number of fields ({len(parts)} instead of 6)")
            if parts:
                error_characters.add(parts[0])
            continue
        
        char, pinyin, hint, freq, hsk, structure = parts
        characters_set.add(char)
        
        # Validate frequency (warning)
        if not freq.isdigit():
            print(f"Line {line_no}: WARNING - Character '{char}': Frequency '{freq}' is not numeric")
        
        # Validate HSK level (warning)
        if hsk not in valid_hsk:
            print(f"Line {line_no}: WARNING - Character '{char}': HSK level '{hsk}' is unexpected")
        hsk_counts[hsk] += 1
        
        # Validate structure (warning)
        if structure not in valid_structure:
            print(f"Line {line_no}: WARNING - Character '{char}': Structure code '{structure}' is unexpected")
        structure_counts[structure] += 1
        
        # Check Unicode order (warning)
        char_code = ord(char)
        if previous_char_code is not None and char_code < previous_char_code:
            print(f"Line {line_no}: WARNING - Character '{char}': Unicode order out of sequence (U+{char_code:X})")
        previous_char_code = char_code
        
        # Special case: 'variant' hints (warning)
        if hint.lower() == "variant":
            print(f"Line {line_no}: WARNING - Character '{char}': Hint is 'variant' (special case)")
        else:
            # Check that the character appears in the hint (warning)
            if char not in hint:
                print(f"Line {line_no}: WARNING - Character '{char}': not found in hint '{hint}'")
            
            # Collect all Chinese characters from the hint
            chinese_chars_in_hint = chinese_char_re.findall(hint)
            for c in chinese_chars_in_hint:
                hint_characters_set.add(c)
            
            hint_len = len(chinese_chars_in_hint)
            
            # Track hint length counts for 2,3,4
            if hint_len in (2,3,4):
                hint_length_counts[hint_len] += 1
            
            if not (2 <= hint_len <= 4):
                print(f"Line {line_no}: WARNING - Character '{char}': Hint '{hint}' contains {hint_len} Chinese characters (expected 2–4)")
            
            # Warn if there are any non-Chinese characters in the hint
            non_chinese_chars = [c for c in hint if not chinese_char_re.match(c)]
            if non_chinese_chars:
                print(f"Line {line_no}: WARNING - Character '{char}': Hint '{hint}' contains non-Chinese characters or punctuation: {''.join(non_chinese_chars)}")
        
        # Warn if hint is duplicated (skip duplicates of 'variant')
        if hint.lower() != "variant":
            if hint in seen_hints:
                print(f"Line {line_no}: WARNING - Character '{char}': Duplicate hint detected: '{hint}'")
            else:
                seen_hints.add(hint)
        
        # Add entry to list
        entries.append({
            "char": char,
            "pinyin": pinyin,
            "hint": hint,
            "frequency": freq,
            "hsk": hsk,
            "structure": structure
        })

# Total number of characters processed
total_chars = len(entries)
print(f"\nParsed {total_chars} characters successfully.\n")

# Print statistics per HSK level
print("HSK level counts:")
for level in sorted(hsk_counts.keys()):
    print(f"  HSK {level}: {hsk_counts[level]} characters")

# Print hint length statistics
print("\nHint length counts (number of Chinese characters):")
for length in sorted(hint_length_counts.keys()):
    print(f"  {length}-character hints: {hint_length_counts[length]}")

# Print structure statistics (numeric order 1–13, then 'none')
print("\nCharacter structure counts:")
numeric_structs = [s for s in structure_counts.keys() if s.isdigit()]
numeric_structs_sorted = sorted(numeric_structs, key=int)
for struct in numeric_structs_sorted:
    print(f"  Structure {struct}: {structure_counts[struct]} characters")
if 'none' in structure_counts:
    print(f"  Structure none: {structure_counts['none']} characters")

# Find characters that appear in hints but not in main characters
extra_hint_chars = hint_characters_set - characters_set
if extra_hint_chars:
    print("\nCharacters appearing in hints but not in the 'character' field:")
    print("  " + " ".join(sorted(extra_hint_chars)))
else:
    print("\nAll hint characters also appear in the main 'character' field.")

# List characters that caused errors
if error_characters:
    print("\nCharacters that caused ERRORS (need proofreading):")
    print("  " + " ".join(sorted(error_characters)))
else:
    print("\nNo characters caused errors.")

