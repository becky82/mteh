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
    "TOCFL/TOCFL_chars.txt",
    "通用规范汉字表/通用规范汉字表_chars_unicode_order.txt",
    "现代汉语常用字表/现代汉语常用字表_chars_unicode_order.txt",
    "primary_school/primary_school_2016_unicode_order.txt",
    "Heisig/Heisig_chars_unicode_order.txt",
    "Hoenig/Hoenig_chars_unicode_order.txt",
    "JunDa/JunDa_modern_top4500_simplified_unicode_order.txt",
    "SUBTLEX/SUBTLEX_chars_top4500_simplified_unicode_order.txt",
    "Tsai/Tsai_chars_top4500_simplified_unicode_order.txt",
    "Wikipedia/Wikipedia_chars_top4500_simplified_unicode_order.txt",
    "THUOCL/THUOCL_741docs_chars_unicode_order.txt",
    "K-5/K5_chars_unicode_order.txt",
    "Leeds/Leeds_30000words_chars_unicode_order.txt",
    "BLCU/BLCU_30000words_chars_simplified_unicode_order.txt",
    "LWC/LWC_40000words_chars_unicode_order.txt",
    "surnames/surname_all_chars_unicode_order.txt",
    "names/CNC_chars_unicode_order.txt",
    "city-geo/city-geo_chars_unicode_order.txt"
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
report_lines.append("\n## Summary Table\n")

# First row: headers
headers = ["# Corpora"] + [str(i) for i in range(0, num_corpora+1)]
report_lines.append("| " + " | ".join(headers) + " |")

# Second row: separators
report_lines.append("|" + "|".join(["---"] * len(headers)) + "|")

# Third row: values
values = ["# Characters"] + [str(histogram.get(i,0)) for i in range(0, num_corpora+1)]
report_lines.append("| " + " | ".join(values) + " |")


# ---------------- Full data ----------------
report_lines.append("\n## MteH Full Character List\n")
report_lines.append("\n")
report_lines.append("The MteH characters that belong to X corpora, as X varies.\n\n")

for i in range(0, num_corpora+1):
    chars_list = ''.join(sorted(chars_by_count.get(i, [])))
    report_lines.append(f"### Characters in {i} corpora ({len(chars_by_count.get(i, []))})\n")
    report_lines.append(chars_list + "\n")

# Append chapter checksum
total_full = sum(len(chars_by_count.get(i, [])) for i in range(0, num_corpora+1))
report_lines.append(f"**Total {total_full} chars.**\n")

# ---------------- Non-MteH character summary ----------------
print("Summarizing non-MteH characters...")

# 1. Build corpus-wide counts for all chars
all_char_counts = defaultdict(int)
for relative_path in CORPUS_FILES:
    corpus_path = os.path.join(CORPUS_BASE, relative_path)
    if not os.path.exists(corpus_path):
        continue
    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus_chars = set(line.strip() for line in f if line.strip())
    for ch in corpus_chars:
        all_char_counts[ch] += 1

# 2. Filter & group non-MteH chars
non_mteh_by_count = defaultdict(list)
for ch, count in all_char_counts.items():
    if ch not in mteh_chars:
        non_mteh_by_count[count].append(ch)

# 3. Append compact summary (20 → 1)
report_lines.append("\n## Non-MteH Character Summary\n")
report_lines.append("\n")
report_lines.append("The non-MteH characters that belong to X corpora, as X varies.  (Note that many computer-generated corpora contain traditional characters, which are excluded from MteH since it only contains simplified characters.)\n\n")

for i in range(20, 0, -1):
    chars_list = ''.join(sorted(non_mteh_by_count.get(i, [])))
    if chars_list:
        report_lines.append(f"### Non-MteH characters in {i} corpora ({len(chars_list)})\n")
        report_lines.append(chars_list + "\n")

# Append chapter checksum
total_non_mteh = sum(len(non_mteh_by_count.get(i, [])) for i in range(1, 21))
report_lines.append(f"**Total {total_non_mteh} chars.**\n")

print("Non-MteH character summary appended.")

# ---------------- Unique MteH characters per corpus ----------------
print("Calculating unique MteH characters for each corpus...")

# Load all corpus sets once
corpus_sets = {}
for relative_path in CORPUS_FILES:
    corpus_path = os.path.join(CORPUS_BASE, relative_path)
    if not os.path.exists(corpus_path):
        continue
    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus_sets[relative_path] = set(line.strip() for line in f if line.strip())

# Compute unique MteH chars per corpus
unique_mteh_per_corpus = {}
for name, chars in corpus_sets.items():
    # MteH chars in this corpus only
    other_chars = set().union(*(v for k, v in corpus_sets.items() if k != name))
    unique_chars = (chars & mteh_chars) - other_chars
    if unique_chars:
        unique_mteh_per_corpus[name] = sorted(unique_chars)

# Append to report
report_lines.append("\n## Corpus-specific unique MteH characters\n")
report_lines.append("\n")
report_lines.append("MteH characters that belong to exactly 1 corpora.\n\n")

for name, chars in unique_mteh_per_corpus.items():
    report_lines.append(f"### {name} — {len(chars)} unique MteH characters\n")
    report_lines.append(''.join(chars) + "\n")

# Append chapter checksum
total_unique = sum(len(chars) for chars in unique_mteh_per_corpus.values())
report_lines.append(f"**Total {total_unique} chars.**\n")

print("Unique MteH character summary appended.")


# Write report
with open(os.path.join(CORPUS_BASE, REPORT_FILE), "w", encoding="utf-8") as f:
    f.write('\n'.join(report_lines))

print(f"Markdown report generated: {REPORT_FILE}")
print(f"Histogram plot saved as: {plot_file}")

