# -*- coding: utf-8 -*-
from opencc import OpenCC

input_file = "JunDa_modern_top3500_unicode_order.txt"
output_file = "JunDa_traditional_chars.txt"

cc = OpenCC('t2s')  # Traditional → Simplified

traditional_chars = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        char = line.strip()
        if not char:
            continue
        simplified = cc.convert(char)
        if simplified != char:
            # Character is traditional
            traditional_chars.append(char)

with open(output_file, "w", encoding="utf-8") as f_out:
    for char in traditional_chars:
        f_out.write(char + "\n")

print(f"Found {len(traditional_chars)} traditional characters → {output_file}")

