"""
Character Structure Histogram Report
Written by ChatGPT
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend so PNGs can be saved
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import os
import numpy as np

# --- Configuration ---
mteh_file = '../versions/v0.1.3/mteh_v0.1.3.txt'
report_md = 'character_structure_histogram_report.md'
output_dir = os.getcwd()  # save images in current directory

# Mapping MteH code → readable label
structure_labels = {
    0: "None",
    1: "Left-Right",
    2: "Top-Bottom",
    3: "Left-Middle-Right",
    4: "Top-Middle-Bottom",
    5: "Enclosure",
    6: "Bottom Enclosure",
    7: "Left Enclosure",
    8: "Upper-Right Enclosure",
    9: "Upper-Left Enclosure",
    10: "Bottom-Right Enclosure",
    11: "Bottom-Left Enclosure",
    12: "Overlapping"
}

# HSK mapping for display
hsk_labels = {
    "1": "HSK1",
    "2": "HSK2",
    "3": "HSK3",
    "4": "HSK4",
    "5": "HSK5",
    "6": "HSK6",
    "+": "HSK7-9",
    "n": "Non-HSK"
}

# --- Collect data ---
all_codes = []
hsk_structures = {k: [] for k in hsk_labels.keys()}

with open(mteh_file, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        if len(fields) < 6:
            continue
        try:
            code = int(fields[5])
        except ValueError:
            continue
        hsk = fields[4]
        all_codes.append(code)
        if hsk in hsk_structures:
            hsk_structures[hsk].append(code)

# --- Function to plot simple histogram ---
def plot_histogram(codes, title, filename):
    counts_dict = Counter(codes)
    labels = [structure_labels[c] for c in range(0, 13)]
    counts = [counts_dict.get(c, 0) for c in range(0, 13)]
    total = sum(counts)

    plt.figure(figsize=(12,6))
    bars = plt.bar(labels, counts, color='skyblue')
    plt.title(title, fontsize=16)
    plt.xlabel('Structure')
    plt.ylabel('Number of characters')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Annotate percentages
    for bar, count in zip(bars, counts):
        if count > 0:
            percent = count / total * 100
            plt.text(bar.get_x() + bar.get_width()/2,
                     bar.get_height() + 0.5,
                     f"{percent:.1f}%",
                     ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Histogram saved to {filename}")
    return filename

def plot_hsk_structure_proportion(hsk_structures, title, filename):
    levels = ["1","2","3","4","5","6","+","n"]
    structures = list(range(0,13))
    labels = [structure_labels[s] for s in structures]

    # Build a 2D list: rows = structures, columns = HSK levels
    data = []
    for s in structures:
        row = []
        for lvl in levels:
            codes = hsk_structures.get(lvl, [])
            count = codes.count(s)
            row.append(count)
        data.append(row)

    # Convert counts to proportions per HSK level
    data = np.array(data, dtype=float)
    column_sums = data.sum(axis=0)
    column_sums[column_sums == 0] = 1  # avoid division by zero
    data /= column_sums

    # Plot
    plt.figure(figsize=(12,6))
    bottom = np.zeros(len(levels))
    colors = plt.cm.tab20.colors  # enough distinct colors
    for i, row in enumerate(data):
        plt.bar(levels, row, bottom=bottom, color=colors[i % len(colors)], label=labels[i])
        bottom += row

    plt.title(title, fontsize=16)
    plt.xlabel("HSK Level")
    plt.ylabel("Proportion of characters")
    plt.ylim(0,1)

    # Replace "+" and "n" with desired labels
    display_labels = ["1","2","3","4","5","6","7-9","non-HSK"]
    plt.xticks(levels, display_labels)

    plt.legend(bbox_to_anchor=(1.05,1), loc='upper left')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Stacked proportion histogram saved to {filename}")
    return filename

# --- Prepare Markdown report ---
with open(report_md, 'w', encoding='utf-8') as md:
    md.write(f"# Character Structure Histogram Report\n\n")
    md.write(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}; Python script written by ChatGPT\n\n")
    md.write(f"Checking MteH file: {mteh_file}\n\n")

    # Full histogram
    full_file = os.path.join(output_dir, 'MteH_structure_histogram.png')
    plot_histogram(all_codes, 'Full MteH Character Structure Distribution', full_file)
    md.write(f"## Full MteH Character Structure Distribution\n\n")
    md.write(f"![Full MteH Histogram](MteH_structure_histogram.png)\n\n")

    # Per HSK histograms
    for hsk, codes in hsk_structures.items():
        if not codes:
            continue
        filename = os.path.join(output_dir, f'HSK{hsk}_structure_histogram.png')
        plot_histogram(codes, f'{hsk_labels[hsk]} Character Structure Distribution', filename)
        md.write(f"## {hsk_labels[hsk]} Character Structure Distribution\n\n")
        md.write(f"![{hsk_labels[hsk]} Histogram](HSK{hsk}_structure_histogram.png)\n\n")

    # Stacked 100% proportion histogram
    stacked_file = os.path.join(output_dir, 'HSK_level_structure_proportion.png')
    plot_hsk_structure_proportion(hsk_structures,
                                  'Character Structure Proportion by HSK Level',
                                  stacked_file)
    md.write(f"## Character Structure Proportion by HSK Level\n\n")
    md.write(f"![HSK Level Structure Proportion](HSK_level_structure_proportion.png)\n\n")

print(f"Markdown report written to {report_md}")

