#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def process_file(input_file, output_file):
    chars = set()
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            for ch in line:
                if '\u4e00' <= ch <= '\u9fff':  # Chinese character range
                    chars.add(ch)
    sorted_chars = sorted(chars)
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write('\n'.join(sorted_chars))
    print(f"{len(sorted_chars)} unique chars written to {output_file}")

process_file("THUOCL_741docs_words.txt", "THUOCL_741docs_chars_unicode_order.txt")

