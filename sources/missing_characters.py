#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from opencc import OpenCC

from datetime import datetime

run_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

repo_base_url = "https://github.com/becky82/mteh/tree/main/sources"

# ---------------- Configuration ----------------
MTEH_SNAPSHOT = "../versions/v0.1.1/mteh_v0.1.1.txt"
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
REPORT_FILE = "missing_chars_report.md"
CORPUS_BASE = "./"  # Adjust if running from /sources/

# ---------------- Functions ----------------
def load_mteh_chars(file_path):
    chars = set()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            ch = line.split()[0]
            chars.add(ch)
    return chars

def load_corpus_chars(file_path):
    chars = set()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chars.add(line)
    return chars

# ---------------- Main ----------------
def main():
    mteh_chars = load_mteh_chars(MTEH_SNAPSHOT)
    cc = OpenCC('t2s')

    report_lines = [
        "# MteH Missing Characters Report\n",
        f"**Report generated on:** {run_date}\n",
        f"This report checks all listed corpus files against **MteH snapshot:** `{MTEH_SNAPSHOT}`\n",
        "### Notes:\n",
        "- **Missing simplified**: characters not in MteH after conversion to simplified Chinese.\n",
        "- **Missing traditional-only**: characters that differ from their simplified form and are missing in MteH.\n",
        "- Classification uses [OpenCC](https://github.com/BYVoid/OpenCC) and may be imperfect.\n",
        "- Python script written by ChatGPT (GPT-5-mini).\n"
    ]

    for relative_path in CORPUS_FILES:
        corpus_path = os.path.join(CORPUS_BASE, relative_path)
        if not os.path.exists(corpus_path):
            print(f"Warning: {corpus_path} not found, skipping.")
            continue
        
        corpus_chars = load_corpus_chars(corpus_path)
        total_chars = len(corpus_chars)
        missing_simplified = set()
        missing_traditional_only = set()

        for ch in corpus_chars:
            ch_s = cc.convert(ch)
            if ch not in mteh_chars:
                if ch == ch_s:
                    missing_simplified.add(ch)
                else:
                    missing_traditional_only.add(ch)

        present_in_mteh = corpus_chars.intersection(mteh_chars)

        # Counts
        total_chars = len(corpus_chars)
        present_count = len(corpus_chars) - len(missing_simplified) - len(missing_traditional_only)
        simplified_missing_count = len(missing_simplified)
        traditional_missing_count = len(missing_traditional_only)

        # Sanity check
        if total_chars != present_count + simplified_missing_count + traditional_missing_count:
            print(f"ERROR: Count mismatch in {relative_path}!")
            print(f"Total characters: {total_chars}")
            print(f"Present in MteH: {present_count}")
            print(f"Missing simplified: {simplified_missing_count}")
            print(f"Missing traditional-only: {traditional_missing_count}")


        folder_name = os.path.dirname(relative_path)  # e.g., 'HSK1.0'
        file_name = os.path.basename(relative_path)  # e.g., 'HSK1.0_chars.txt'
        folder_url = f"{repo_base_url}/{folder_name}"

        report_lines.append(f"## [{relative_path}]({folder_url})")
        report_lines.append(f"- Total characters in file: {total_chars}")
        report_lines.append(f"- Characters present in MteH: {len(present_in_mteh)}")
        report_lines.append(f"- Simplified characters not in MteH ({len(missing_simplified)}): {' '.join(sorted(missing_simplified)) if missing_simplified else 'None'}")
        report_lines.append(f"- Traditional-only characters not in MteH ({len(missing_traditional_only)}): {' '.join(sorted(missing_traditional_only)) if missing_traditional_only else 'None'}")
        report_lines.append("")

    report_path = os.path.join(CORPUS_BASE, REPORT_FILE)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"Report generated: {report_path}")

if __name__ == "__main__":
    main()

