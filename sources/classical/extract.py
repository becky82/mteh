# -*- coding: utf-8 -*-
# Convert classical Chinese corpus (one character per line) to simplified,
# sort, remove duplicates, and list all traditional characters mapping to the same simplified form.

from opencc import OpenCC
from collections import defaultdict

# Input and output filenames
input_file = "classical_top2000_original_order.txt"
output_file = "classical_top2000_simplified_unicode_order.txt"

# Step 1: Load characters
with open(input_file, "r", encoding="utf-8") as f:
    chars = [line.strip() for line in f if line.strip()]

# Step 2: Convert to simplified
converter = OpenCC("t2s")
trad_to_simp = {ch: converter.convert(ch) for ch in chars}

# Step 3: Collect mapping (many-to-one)
simp_to_trad = defaultdict(set)
for trad, simp in trad_to_simp.items():
    simp_to_trad[simp].add(trad)

# Step 4: Simplified characters (sorted, deduplicated)
simplified_chars = sorted(set(trad_to_simp.values()))

# Step 5: Write simplified characters to file
with open(output_file, "w", encoding="utf-8") as f:
    for ch in simplified_chars:
        f.write(ch + "\n")

# Step 6: Print many-to-one mappings and summary
print("=== Multiple Traditional Characters → Same Simplified Character ===")
dup_count = 0
trad_involved = 0

for simp, trads in sorted(simp_to_trad.items()):
    if len(trads) > 1:
        dup_count += 1
        trad_involved += len(trads)
        print(f"{simp}: {''.join(sorted(trads))}")

print()
print(f"Total simplified characters with duplicates: {dup_count}")
print(f"Total traditional characters involved: {trad_involved}")
print("\n✅ Simplified list written to:", output_file)

