#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from collections import Counter, defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

# ---------------- Configuration ----------------
MTEH_FILE = "../versions/v0.1.1/mteh_v0.1.1.txt"
CORPUS_BASE = "./"
CORPUS_FILES = [
    "HSK1.0/HSK1.0_chars.txt",
    "HSK2.0/HSK2.0_chars.txt",
    "HSK3.0/HSK3.0_chars.txt",
    "Heisig/Heisig_chars_unicode_order.txt",
    "Hoenig/Hoenig_unicode_order.txt",
    "TOCFL/TOCFL_chars.txt",
    "JunDa/JunDa_modern_top3500_unicode_order.txt",
    "SUBTLEX/SUBTLEX_chars_top3500_unicode_order.txt",
    "Tsai/Tsai_top3500_unicode_order.txt",
    "K-5/K5_chars_unicode_order.txt",
    "Leeds/Leeds_20000words_chars_unicode_order.txt",
    "BLCU/BLCU_20000words_chars_unicode_order.txt",
    "LWC/LWC_20000words_chars_unicode_order.txt",
    "Wikipedia/Chinese_Wikipedia_3500chars_unicode_order.txt",
    "通用规范汉字表/通用规范汉字表_chars_unicode_order.txt",
    "现代汉语常用字表/现代汉语常用字表_3500chars.txt",
    "primary_school/primary_school_2016_unicode_order.txt",
    "surnames/surnames_unicode_order.txt"
]
REPORT_FILE = "mteh_char_corpus_histogram_full.md"

# ---------------- Load MteH characters ----------------
with open(MTEH_FILE, "r", encoding="utf-8") as f:
    mteh_chars = set(line.split()[0] for line in f if line.strip() and not line.startswith("#"))

# ---------------- Count appearances ----------------
char_counts = {ch: 0 for ch in mteh_chars}
chars_by_count = defaultdict(list)

for relative_path in CORPUS_FILES:
    corpus_path = os.path.join(CORPUS_BASE, relative_path)
    if not os.path.exists(corpus_path):
        print(f"Warning: {corpus_path} not found, skipping.")
        continue
    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus_chars = set(line.strip() for line in f if line.strip())
    for ch in mteh_chars:
        if ch in corpus_chars:
            char_counts[ch] += 1

# Build mapping from count -> characters
for ch, count in char_counts.items():
    chars_by_count[count].append(ch)

# ---------------- Histogram & checksum ----------------
histogram = Counter(char_counts.values())
num_corpora = len(CORPUS_FILES)
total_chars = len(mteh_chars)
checksum = sum(histogram.values())

if checksum != total_chars:
    print(f"ERROR: checksum mismatch! Sum of frequencies {checksum} != total characters {total_chars}")

# ---------------- Plot ----------------
plt.figure(figsize=(12,6))
plt.bar(histogram.keys(), histogram.values(), color='skyblue')
plt.xlabel('Number of corpora')
plt.ylabel('Number of MteH characters')
plt.title('MteH Character Occurrence Histogram')
plt.xticks(range(0, num_corpora+1))
plt.tight_layout()
plot_file = "mteh_char_corpus_histogram.png"
plt.savefig(os.path.join(CORPUS_BASE, plot_file))
plt.close()

# ---------------- Markdown report ----------------
run_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report_lines = [
    "# MteH Character Occurrence Histogram\n",
    f"**Report generated on:** {run_date}; Python script written by ChatGPT (GPT-5-mini).\n",
    f"**Checking MteH snapshot:** `{MTEH_FILE}`\n",
    f"**Number of corpora checked:** {num_corpora}\n",
    f"![Histogram]({plot_file})\n"
]

# ---------------- Horizontal summary table ----------------
report_lines.append("\n## Summary Table (Horizontal)\n")

# First row: headers
headers = ["# Corpora"] + [str(i) for i in range(0, num_corpora+1)]
report_lines.append("| " + " | ".join(headers) + " |")

# Second row: separators
report_lines.append("|" + "|".join(["---"] * len(headers)) + "|")

# Third row: values
values = ["# Characters"] + [str(histogram.get(i,0)) for i in range(0, num_corpora+1)]
report_lines.append("| " + " | ".join(values) + " |")


# ---------------- Full data ----------------
report_lines.append("\n## Full Character Lists\n")
for i in range(0, num_corpora+1):
    chars_list = ''.join(sorted(chars_by_count.get(i, [])))
    report_lines.append(f"### Characters in {i} corpora ({len(chars_by_count.get(i, []))})\n")
    report_lines.append(chars_list + "\n")

# Write report
with open(os.path.join(CORPUS_BASE, REPORT_FILE), "w", encoding="utf-8") as f:
    f.write('\n'.join(report_lines))

print(f"Markdown report generated: {REPORT_FILE}")
print(f"Histogram plot saved as: {plot_file}")

