#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from opencc import OpenCC

INPUT_FILE = "ChineseSE_character_frequency.txt"
OUTPUT_FILE = "ChineseSE_character_frequency_simplified.txt"

cc = OpenCC('t2s')  # traditional -> simplified

counter = Counter()

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        char, count = line.strip().split("\t")
        count = int(count)

        simplified = cc.convert(char)

        # In rare cases conversion returns multiple characters
        # (very uncommon for single CJK characters, but safe to check)
        if len(simplified) == 1:
            counter[simplified] += count
        else:
            # If conversion expanded (rare), count each char
            for c in simplified:
                counter[c] += count

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for char, count in counter.most_common():
        f.write(f"{char}\t{count}\n")

print("Done.")

