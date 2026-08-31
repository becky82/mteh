#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate a Markdown report comparing a MteH snapshot of characters
against multiple Chinese character corpora.

Features:
- Sorts all character lists by JunDa order.
- Characters not in JunDa order are labelled as "(Non Jun Da chars: ...)".
- Missing characters from MteH are always fully displayed.
- MteH-not-in-corpus list is truncated if too long.
- Python script written by ChatGPT (GPT-5-mini).
"""

import os
from datetime import datetime

# ---------------- Configuration ----------------
MAX_DISPLAY = 100  # max characters to display when truncating
MTEH_SNAPSHOT = "../versions/v0.1.3/mteh_v0.1.3.txt"
CORPUS_FILES = [
    "HSK1.0/HSK1.0_chars.txt",
    "HSK2.0/HSK2.0_chars.txt",
    "HSK3.0/HSK3.0_chars.txt",
    "HSK3.1/HSK3.1_chars.txt",
    "TOCFL/TOCFL_simplified_chars.txt",
    "K-5/K5_chars_unicode_order.txt",
    "通用规范汉字表/通用规范汉字表_chars_unicode_order.txt",
    "通用规范汉字表/通用规范汉字表_level2_chars_unicode_order.txt",
    "通用规范汉字表/通用规范汉字表_level3_chars_unicode_order.txt",
    "现代汉语常用字表/现代汉语常用字表_chars_unicode_order.txt",
    "现代汉语常用字表/现代汉语通用字表1988_unicode_order.txt",
    "普通话水平测试/普通话水平测试_chars_level1_unicode_order.txt",
    "普通话水平测试/普通话水平测试_chars_level2_unicode_order.txt",
    "TaiwanMoE/TaiwanMoE_simplified_unicode_order.txt",
    "primary_school/primary_school_2016_unicode_order.txt",
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
    "ChineseSE/ChineseSE_chars_unicode_order.txt",
    "classical/classical_top2000_simplified_unicode_order.txt",
    "THUOCL/THUOCL_741docs_chars_unicode_order.txt",
    "Leeds/Leeds_30000words_chars_unicode_order.txt",
    "BLCU/BLCU_30000words_chars_simplified_unicode_order.txt",
    "LWC/LWC_40000words_chars_unicode_order.txt",
    "food/wainshine_food_chars_unicode_order.txt",
    "species/wainshine_species_chars_unicode_order.txt",
    "surnames/surname_all_chars_unicode_order.txt",
    "names/CNC_chars_unicode_order.txt",
    "city-geo/city-geo_chars_unicode_order.txt",
    "company/wainshine_company_top_chars_unicode_order.txt",
    "med-orgs/wainshine_med-orgs_chars_unicode_order.txt",
    "MCT/MCT_chars_unicode_order.txt",
    "BCT/BCT_chars_unicode_order.txt",
    "chengyu_convention/chengyu_convention_chars.txt",
    "Xinhua/Xinhua_chars.txt"
]
REPORT_FILE = "missing_chars_report.md"
CORPUS_BASE = "./"  # Adjust if running from /sources/
JUNDA_ORDER_FILE = "JunDa/JunDa_modern_chars_original_order.txt"
REPO_BASE_URL = "https://github.com/becky82/mteh/tree/main/sources"


# ---------------- Utility Functions ----------------
def load_char_set(file_path):
    """Load a file of characters (one per line) into a set."""
    chars = set()
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                chars.add(line.split()[0])
    return chars


def load_order_list(file_path):
    """Load a file of characters into a list to preserve order."""
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def format_sorted_chars(chars, junda_index, truncate=True):
    """
    Sort characters by JunDa order.
    Characters not in JunDa order are appended at the end, labelled as non-Jun Da.
    If truncate=True, limit to MAX_DISPLAY characters and append '(truncated)' if needed.
    """
    in_order = [ch for ch in chars if ch in junda_index]
    not_in_order = [ch for ch in chars if ch not in junda_index]

    # Sort characters in JunDa order
    in_order_sorted = sorted(in_order, key=lambda ch: junda_index[ch])

    # Combine with non-Jun Da characters
    line = ' '.join(in_order_sorted)
    if not_in_order:
        line += ' (Non Jun Da chars: ' + ' '.join(not_in_order) + ')'

    # Truncate if requested
    if truncate and line:
        char_list = line.split()
        if len(char_list) > MAX_DISPLAY:
            line = ' '.join(char_list[:MAX_DISPLAY]) + ' ... (truncated)'

    return line if line else 'None'


# ---------------- Main Processing ----------------
def main():
    # Load MteH snapshot
    mteh_chars = load_char_set(MTEH_SNAPSHOT)

    # Load JunDa order for sorting missing characters
    junda_order = load_order_list(JUNDA_ORDER_FILE)
    junda_index = {ch: i for i, ch in enumerate(junda_order)}

    # Report header
    report_lines = [
        "# MteH Missing Characters Report",
        f"**Report generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**MteH snapshot:** `{MTEH_SNAPSHOT}`",
        "### Notes",
        "- All lists are sorted in JunDa order where available.",
        "- Characters not in JunDa order are labelled as '(Non Jun Da chars: ...)'.",
        "- Missing characters from MteH are always fully displayed.",
        "- Python script written by ChatGPT (GPT-5-mini).",
        ""
    ]

    # Process each corpus
    for relative_path in CORPUS_FILES:
        corpus_path = os.path.join(CORPUS_BASE, relative_path)
        if not os.path.exists(corpus_path):
            print(f"Warning: {corpus_path} not found, skipping.")
            continue

        corpus_chars = load_char_set(corpus_path)

        # Identify missing characters (exact comparison)
        missing_chars = set(ch for ch in corpus_chars if ch not in mteh_chars)

        # MteH characters not in this corpus
        mteh_not_in_corpus = set(ch for ch in mteh_chars if ch not in corpus_chars)

        # Format character lists
        missing_line = format_sorted_chars(missing_chars, junda_index, truncate=False)  # always full
        mteh_line = format_sorted_chars(mteh_not_in_corpus, junda_index, truncate=True)  # may be truncated

        # Add report section
        folder_name = os.path.dirname(relative_path)
        folder_url = f"{REPO_BASE_URL}/{folder_name}"

        report_lines.extend([
            f"## [{relative_path}]({folder_url})",
            f"- Total characters in file: {len(corpus_chars)}",
            f"- Characters present in MteH: {len(corpus_chars) - len(missing_chars)}",
            f"- Characters missing from MteH ({len(missing_chars)}): {missing_line}",
            f"- MteH characters not in corpus ({len(mteh_not_in_corpus)}): {mteh_line}",
            ""
        ])

    # Write report
    report_path = os.path.join(CORPUS_BASE, REPORT_FILE)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"Report generated: {report_path}")


if __name__ == "__main__":
    main()

