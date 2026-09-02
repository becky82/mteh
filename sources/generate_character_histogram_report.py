#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from collections import Counter, defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import spearmanr

# ---------------- Configuration ----------------
MTEH_FILE = "../versions/v0.1.3/mteh_v0.1.3.txt"
JUNDA_ORDER_FILE = "JunDa/JunDa_modern_chars_original_order.txt"
CORPUS_BASE = "./"
CORPUS_FILES = [
    "HSK1.0/HSK1.0_chars.txt",
    "HSK2.0/HSK2.0_chars.txt",
    "HSK3.0/HSK3.0_chars.txt",
    "HSK3.1/HSK3.1_chars.txt",
    "TOCFL/TOCFL_simplified_chars_unicode_order.txt",
    "K-5/K5_chars_unicode_order.txt",
    "通用规范汉字表/通用规范汉字表_chars_unicode_order.txt",
    "通用规范汉字表/通用规范汉字表_level2_chars_unicode_order.txt",
    "通用规范汉字表/通用规范汉字表_level3_chars_unicode_order.txt",
    "现代汉语常用字表/现代汉语常用字表_chars_unicode_order.txt",
    "现代汉语常用字表/现代汉语通用字表1988_unicode_order.txt",
    "普通话水平测试/普通话水平测试_chars_level1_unicode_order.txt",
    "普通话水平测试/普通话水平测试_chars_level2_unicode_order.txt",
    "TaiwanMoE/TaiwanMoE_simplified_unicode_order.txt",
    "primary_school/primary_school_Zhang_et_al_2024_unicode_order.txt",
    "语文/语文_level1_unicode_order.txt",
    "语文/语文_level2_unicode_order.txt",
    "Singapore_primary_school/Singapore_chars_unicode_order.txt",
    "age_of_acquisition/age_of_acquisition_chars.txt",
    "psycholinguistic/psycholinguistic_simplified_unicode_order.txt",
    "Heisig/Heisig_chars_unicode_order.txt",
    "Hoenig/Hoenig_chars_unicode_order.txt",
    "JunDa/JunDa_modern_top4500_simplified_unicode_order.txt",
    "SUBTLEX/SUBTLEX_chars_top4500_simplified_unicode_order.txt",
    "Tsai/Tsai_chars_top4500_simplified_unicode_order.txt",
    "CKIP/CKIP_chars_unicode_order.txt",
    "Wikipedia/Wikipedia_chars_top4500_simplified_unicode_order.txt",
    "ChineseSE/ChineseSE_5000_chars_unicode_order.txt",
    "classical/classical_top2000_simplified_unicode_order.txt",
    "THUOCL/THUOCL_741docs_chars_unicode_order.txt",
    "Leeds/Leeds_chars_frequency_order.txt",
    "BLCU/BLCU_5000_chars_unicode_order.txt",
    "LWC/LWC_chars_top5000_unicode_order.txt",
    "food/wainshine_food_chars_unicode_order.txt",
    "species/wainshine_species_chars_unicode_order.txt",
    "surnames/surname_all_chars_unicode_order.txt",
    "names/CNC_character_chars_unicode_order.txt",
    "city-geo/city-geo_chars_unicode_order.txt",
    "company/wainshine_company_chars_unicode_order.txt",
    "med-orgs/wainshine_med-orgs_chars_unicode_order.txt",
    "MCT/MCT_chars_unicode_order.txt",
    "BCT/BCT_chars_unicode_order.txt",
    "chengyu_convention/chengyu_convention_chars.txt",
    "Xinhua/Xinhua_chars.txt"
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

# ---------------- Plot histogram ----------------
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
headers = ["# Corpora"] + [str(i) for i in range(0, num_corpora+1)]
report_lines.append("| " + " | ".join(headers) + " |")
report_lines.append("|" + "|".join(["---"] * len(headers)) + "|")
values = ["# Characters"] + [str(histogram.get(i,0)) for i in range(0, num_corpora+1)]
report_lines.append("| " + " | ".join(values) + " |")

# ---------------- Full MteH character list ----------------
report_lines.append("\n## MteH Full Character List\n")
report_lines.append("The MteH characters that belong to X corpora, as X varies.\n\n")
for i in range(0, num_corpora+1):
    chars_list = ''.join(sorted(chars_by_count.get(i, [])))
    report_lines.append(f"### Characters in {i} corpora ({len(chars_list)})\n")
    report_lines.append(chars_list + "\n")
total_full = sum(len(chars_by_count.get(i, [])) for i in range(0, num_corpora+1))
report_lines.append(f"**Total {total_full} chars.**\n")

# ---------------- Non-MteH character summary ----------------
print("Summarizing non-MteH characters...")
all_char_counts = defaultdict(int)
for relative_path in CORPUS_FILES:
    corpus_path = os.path.join(CORPUS_BASE, relative_path)
    if not os.path.exists(corpus_path):
        continue
    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus_chars = set(line.strip() for line in f if line.strip())
    for ch in corpus_chars:
        all_char_counts[ch] += 1

non_mteh_by_count = defaultdict(list)
for ch, count in all_char_counts.items():
    if ch not in mteh_chars:
        non_mteh_by_count[count].append(ch)

report_lines.append("\n## Non-MteH Character Summary\n")
report_lines.append("The non-MteH characters that belong to X corpora, as X varies.\n\n")
for i in range(20, 0, -1):
    chars_list = ''.join(sorted(non_mteh_by_count.get(i, [])))
    if chars_list:
        report_lines.append(f"### Non-MteH characters in {i} corpora ({len(chars_list)})\n")
        report_lines.append(chars_list + "\n")
total_non_mteh = sum(len(non_mteh_by_count.get(i, [])) for i in range(1, 21))
report_lines.append(f"**Total {total_non_mteh} chars.**\n")
print("Non-MteH character summary appended.")

# ---------------- Unique MteH characters per corpus ----------------
print("Calculating unique MteH characters for each corpus...")
corpus_sets = {}
for relative_path in CORPUS_FILES:
    corpus_path = os.path.join(CORPUS_BASE, relative_path)
    if not os.path.exists(corpus_path):
        continue
    with open(corpus_path, "r", encoding="utf-8") as f:
        corpus_sets[relative_path] = set(line.strip() for line in f if line.strip())

unique_mteh_per_corpus = {}
for name, chars in corpus_sets.items():
    other_chars = set().union(*(v for k, v in corpus_sets.items() if k != name))
    unique_chars = (chars & mteh_chars) - other_chars
    if unique_chars:
        unique_mteh_per_corpus[name] = sorted(unique_chars)

report_lines.append("\n## Corpus-specific unique MteH characters\n")
report_lines.append("MteH characters that belong to exactly 1 corpora.\n\n")
for name, chars in unique_mteh_per_corpus.items():
    report_lines.append(f"### {name} — {len(chars)} unique MteH characters\n")
    report_lines.append(''.join(chars) + "\n")
total_unique = sum(len(chars) for chars in unique_mteh_per_corpus.values())
report_lines.append(f"**Total {total_unique} chars.**\n")
print("Unique MteH character summary appended.")

# ---------------- JunDa scatter plot with trend line ----------------
print("Generating JunDa scatter plot with trend line...")
if os.path.exists(JUNDA_ORDER_FILE):
    with open(JUNDA_ORDER_FILE, "r", encoding="utf-8") as f:
        junda_order = [line.strip() for line in f if line.strip()]
    junda_rank = {ch: idx+1 for idx, ch in enumerate(junda_order)}

    x_vals, y_vals = [], []
    for ch in mteh_chars:
        if ch in junda_rank:
            x_vals.append(char_counts.get(ch,0))
            y_vals.append(junda_rank[ch])

    if x_vals and y_vals:
        rho, pval = spearmanr(x_vals, y_vals)
        print(f"Spearman correlation: {rho:.4f} (p={pval:.3g})")

        plt.figure(figsize=(10,6))
        plt.scatter(x_vals, y_vals, alpha=0.4, s=8, label='MteH chars')

        coeffs = np.polyfit(x_vals, y_vals, 1)
        trend_y = np.polyval(coeffs, x_vals)
        plt.plot(x_vals, trend_y, color='red', linewidth=2, label='Trend line')

        plt.xlabel("Number of corpora")
        plt.ylabel("JunDa frequency rank")
        plt.title(f"MteH Corpus Count vs JunDa Rank (Spearman ρ={rho:.3f})")
        plt.legend()
        plt.tight_layout()
        scatter_file_trend = "mteh_vs_junda_rank_scatter_trend.png"
        plt.savefig(os.path.join(CORPUS_BASE, scatter_file_trend))
        plt.close()

        report_lines.append("\n## JunDa Rank vs Corpus Count (with trend line)\n")
        report_lines.append(f"Spearman correlation coefficient ρ = {rho:.3f} (p = {pval:.3g})\n")
        report_lines.append(f"![Scatter Plot with Trend]({scatter_file_trend})\n")

        for N in range(0, num_corpora+1):
            chars_in_N = [ch for ch in mteh_chars if char_counts.get(ch,0) == N and ch in junda_rank]
            if not chars_in_N:
                continue
            # Sort by JunDa rank (smaller rank = more frequent)
            sorted_by_rank = sorted(chars_in_N, key=lambda ch: junda_rank[ch])
            top3 = sorted_by_rank[:3]
            bottom3 = sorted_by_rank[-3:]
            report_lines.append(f"- Characters in {N} corpora ({len(chars_in_N)}): most frequent {''.join(top3)} least frequent {''.join(bottom3)}\n")

else:
    print(f"Warning: {JUNDA_ORDER_FILE} not found, skipping JunDa scatter plot.")

# ---------------- Write report ----------------
with open(os.path.join(CORPUS_BASE, REPORT_FILE), "w", encoding="utf-8") as f:
    f.write('\n'.join(report_lines))

print(f"Markdown report generated: {REPORT_FILE}")
print(f"Histogram plot saved as: {plot_file}")
print(f"JunDa scatter plot saved as: {scatter_file_trend if x_vals else 'N/A'}")

