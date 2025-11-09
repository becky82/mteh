#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from opencc import OpenCC
from collections import defaultdict

# Initialize OpenCC (Traditional → Simplified)
cc = OpenCC('t2s')

input_file = "TOCFL_chars_original.txt"
output_file = "TOCFL_simplified_chars.txt"

simplified_chars = set()
mapping = defaultdict(list)

# Read file and process lines
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        # Handle cases like 台／臺
        variants = line.split('／')
        for var in variants:
            sim = cc.convert(var)
            simplified_chars.add(sim)
            mapping[sim].append(var)

# Write sorted simplified characters to file
with open(output_file, 'w', encoding='utf-8') as f:
    for char in sorted(simplified_chars):
        f.write(char + '\n')

print(f"Simplified characters written to {output_file}")

# Print traditional characters that map to the same simplified
print("\n=== Traditional duplicates (map to same simplified) ===")
duplicate_count = 0
total_traditional_duplicates = 0
for sim_char, trad_list in mapping.items():
    if len(trad_list) > 1:
        print(f"{sim_char}: {', '.join(trad_list)}")
        duplicate_count += 1
        total_traditional_duplicates += len(trad_list)

print(f"\nNumber of simplified characters with multiple traditional forms: {duplicate_count}")
print(f"Total number of traditional characters involved in duplicates: {total_traditional_duplicates}")

