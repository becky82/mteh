#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This script was generated with the help of ChatGPT (OpenAI GPT-5).
# Purpose: Convert Chinese character study note entries from LaTeX-style
# \character{...}{...}{...}{...}{...} format into a human-readable format.
# - Replaces \square{N} with the corresponding character.
# - Adds the index N as the final column.
# - Skips commented lines (starting with %).
# - If "variant" is found in the third field, prints a warning but not an error.
# - If no or inconsistent \square{N} found, prints an error and marks the line as "error".
#
# Input:  4000chars_modified_input.txt
# Output: 4000chars_modified_input_github.txt
#
# Example:
#   Input:  \character{冉}{rǎn}{\square{13}\square{13}升起}{3070}{}
#   Output: 冉 rǎn 冉冉升起 3070 n 13
#

import re

input_file = "4000chars_modified_input.txt"
output_file = "4000chars_modified_input_github.txt"

pattern = re.compile(
    r"^\\character\{(.+?)\}\{(.+?)\}\{(.+?)\}\{(.+?)\}\{(.*?)\}"
)
square_pattern = re.compile(r"\\square\{(\d+)\}")

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for lineno, line in enumerate(f_in, 1):
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        match = pattern.match(line)
        if not match:
            print(f"Line {lineno}: Format error — {line}")
            continue

        char, pinyin, example, num, flag = match.groups()
        flag = flag if flag else "n"

        # Handle "variant" lines
        if example.strip() == "variant":
            print(f"⚠️ Warning on line {lineno}: 'variant' entry for {char} (no \\square expected).")
            f_out.write(f"{char} {pinyin} variant {num} {flag}\n")
            continue

        # Find all \square{N}
        matches = square_pattern.findall(example)
        if not matches:
            print(f"❌ Error on line {lineno}: No \\square{{}} found for {char} → {line}")
            f_out.write(f"{char} {pinyin} {example} {num} {flag} error\n")
            continue
        if len(set(matches)) > 1:
            print(f"❌ Error on line {lineno}: Inconsistent \\square indices ({matches}) for {char} → {line}")
            f_out.write(f"{char} {pinyin} {example} {num} {flag} error\n")
            continue

        index = matches[0]

        # Replace all \square{N} with the character
        example_replaced = square_pattern.sub(char, example)

        f_out.write(f"{char} {pinyin} {example_replaced} {num} {flag} {index}\n")

print("✅ Conversion complete. Warnings and errors printed above.")

