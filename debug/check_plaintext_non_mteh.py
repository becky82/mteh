# Usage example:
#
# python3 check_plaintext_non_mteh.py [filename]

#!/usr/bin/env python3
import re
import sys
from collections import Counter
from opencc import OpenCC

# Initialize Traditional → Simplified converter
cc = OpenCC('t2s')

# Load MteH characters
mteh_chars = set()
with open("../mteh.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        mteh_chars.add(line.split()[0])

# Define strokes to ignore
strokes = set("丨丿㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉")

# Get input file from command line
if len(sys.argv) < 2:
    print("Usage: python check_plaintext_non_mteh.py <text_file>")
    sys.exit(1)
filename = sys.argv[1]

# Read file
try:
    with open(filename, encoding="utf-8") as f:
        text = f.read()
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# Convert to simplified
simplified_text = cc.convert(text)

# Extract Chinese characters, ignoring strokes
chinese_chars = [c for c in re.findall(r'[\u4e00-\u9fff]', simplified_text) if c not in strokes]
print(f"Total Chinese characters found in file (excluding strokes): {len(chinese_chars)}\n")

# Count all characters
all_counter = Counter(chinese_chars)
print("All Chinese characters (char:freq):")
print(" ".join(f"{char}:{freq}" for char, freq in all_counter.most_common()))
print()

# Count non-MteH characters
non_mteh_chars = [c for c in chinese_chars if c not in mteh_chars]
if non_mteh_chars:
    non_counter = Counter(non_mteh_chars)
    print("Non-MteH characters (char:freq):")
    print(" ".join(f"{char}:{freq}" for char, freq in non_counter.most_common()))
else:
    print("All characters in this file are in MteH ✅")

