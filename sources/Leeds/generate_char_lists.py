#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from opencc import OpenCC

cc = OpenCC('t2s')  # traditional → simplified

def process_file(input_file, output_file):
    chars = set()
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = cc.convert(line.strip())
            for ch in line:
                if '\u4e00' <= ch <= '\u9fff':  # only Chinese chars
                    chars.add(ch)
    sorted_chars = sorted(chars)
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write('\n'.join(sorted_chars))
    print(f"{len(sorted_chars)} unique simplified chars written to {output_file}")

process_file("Leeds_words_original_order.txt", "Leeds_all_chars_unicode_order.txt")
process_file("Leeds_30000words_original_order.txt", "Leeds_30000words_chars_unicode_order.txt")

