#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unicodedata
from collections import defaultdict, Counter
from datetime import datetime
from itertools import chain, combinations
import matplotlib.pyplot as plt
import numpy as np

# -----------------------
# Configuration
# -----------------------
INITIALS = [
    'zh','ch','sh','b','p','m','f','d','t','n','l',
    'g','k','h','j','q','x','r','z','c','s','y','w','∅'
]

TONE_MARKS = {
    'ā':'1','á':'2','ǎ':'3','à':'4',
    'ē':'1','é':'2','ě':'3','è':'4',
    'ī':'1','í':'2','ǐ':'3','ì':'4',
    'ō':'1','ó':'2','ǒ':'3','ò':'4',
    'ū':'1','ú':'2','ǔ':'3','ù':'4',
    'ǖ':'1','ǘ':'2','ǚ':'3','ǜ':'4'
}

input_file = "../versions/v0.1.3/mteh_v0.1.3.txt"
output_file = "mteh_syllables_all_combinations.md"
tone_plot_file = "tone_distribution.png"
initial_plot_file = "initial_distribution.png"
final_plot_file = "final_distribution.png"
new_syllables_plot_file = "new_syllables_per_hsk.png"

# -----------------------
# Functions
# -----------------------
def split_pinyin(pinyin):
    """Return initial, final, tone for a pinyin syllable."""
    tone = '5'  # default neutral
    for char in pinyin:
        if char in TONE_MARKS:
            tone = TONE_MARKS[char]
            break

    base = ''.join(c for c in unicodedata.normalize('NFD', pinyin)
                   if not unicodedata.combining(c))
    base = base.lower().replace('v', 'ü')

    initial = ''
    final = base
    for ini in sorted(INITIALS, key=len, reverse=True):
        if base.startswith(ini):
            initial = ini
            final = base[len(ini):]
            break
    return initial, final, tone

def all_subsets(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1)))

def write_section(md, subset_name, mapping, _):
    md.write(f"## MteH characters with the same pinyin: {subset_name}\n\n")
    group_total = sum(len(chars) for chars in mapping.values())
    for key in sorted(mapping.keys()):
        chars = sorted(mapping[key])
        md.write(f"- **{key} ({len(chars)})**: {' '.join(chars)}\n")
    md.write(f"\n**Total # chars for this group:** {group_total}\n")
    counter = Counter({k: len(v) for k,v in mapping.items()})
    top10 = counter.most_common(10)
    md.write("\n**Top 10 most common keys:**\n\n")
    for rank, (k, count) in enumerate(top10, 1):
        md.write(f"{rank}. {k}: {count}\n\n")
    md.write("\n---\n\n")

def hsk_new_syllables(entries, hsk_levels):
    """
    Count new syllables introduced at each HSK level:
    - With tone (initial+final+tone)
    - Toneless (initial+final only)
    """
    hsk_order = ['1','2','3','4','5','6','7-9','n']
    seen_syllables = set()
    seen_toneless = set()
    new_counts = {level: {'with_tone':0, 'toneless':0} for level in hsk_order}

    for level in hsk_order:
        for char, ini, fin, tone in entries:
            char_level = hsk_levels.get(char, 'n')  # default to non-HSK
            if char_level != level:
                continue

            syllable = f"{ini}{fin}{tone}"
            toneless = f"{ini}{fin}"

            if syllable not in seen_syllables:
                new_counts[level]['with_tone'] += 1
                seen_syllables.add(syllable)
            if toneless not in seen_toneless:
                new_counts[level]['toneless'] += 1
                seen_toneless.add(toneless)

    return new_counts

def hsk_new_syllable_lists(entries, hsk_levels):
    """
    Return a dictionary of new syllables (with tone and toneless) per HSK level.
    Each entry is a sorted list of unique syllables.
    """
    hsk_order = ['1','2','3','4','5','6','7-9','n']
    seen_syllables = set()
    seen_toneless = set()
    syllable_lists = {level: {'with_tone':[], 'toneless':[]} for level in hsk_order}

    for level in hsk_order:
        for char, ini, fin, tone in entries:
            char_level = hsk_levels.get(char, 'n')
            if char_level != level:
                continue

            syllable = f"{ini}{fin}{tone}"
            toneless = f"{ini}{fin}"

            if syllable not in seen_syllables:
                syllable_lists[level]['with_tone'].append(syllable)
                seen_syllables.add(syllable)

            if toneless not in seen_toneless:
                syllable_lists[level]['toneless'].append(toneless)
                seen_toneless.add(toneless)

        # Sort alphabetically
        syllable_lists[level]['with_tone'].sort()
        syllable_lists[level]['toneless'].sort()

    return syllable_lists

# -----------------------
# Read entries and HSK levels
# -----------------------
entries = []
total_chars = 0
hsk_levels = {}
with open(input_file, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 5:
            continue

        char, pinyin = parts[0], parts[1]
        initial, final, tone = split_pinyin(pinyin)
        if initial == '':
            initial = '∅'
        entries.append((char, initial, final, tone))

        # HSK level from 5th column
        level_raw = parts[4]
        if level_raw == '+':
            level = '7-9'
        elif level_raw == 'n':
            level = 'n'
        else:
            level = level_raw
        hsk_levels[char] = level

# -----------------------
# Build mappings for all subsets
# -----------------------
COMPONENTS = ['initial','final','tone']
subsets = all_subsets(COMPONENTS)
mappings = {}
for subset in subsets:
    mapping = defaultdict(list)
    for char, ini, fin, tone in entries:
        key = ''.join([{'initial':ini,'final':fin,'tone':tone}[c] for c in subset])
        mapping[key].append(char)
    mappings[subset] = mapping

# -----------------------
# Histograms for tones, initials, finals
# -----------------------
# Tones
tone_counter = Counter(tone for _, _, _, tone in entries)
tones_sorted = ['1','2','3','4','5']
counts = [tone_counter.get(t,0) for t in tones_sorted]

plt.figure(figsize=(6,4))
plt.bar(tones_sorted, counts, color='skyblue')
plt.xlabel("Tone")
plt.ylabel("Number of characters")
plt.title("Tone Distribution in MteH")
plt.tight_layout()
plt.savefig(tone_plot_file, dpi=150)
plt.close()

# Initials
initial_counter = Counter(ini for _, ini, _, _ in entries)
initials_sorted = INITIALS
initial_counts = [initial_counter.get(i,0) for i in initials_sorted]

plt.figure(figsize=(10,4))
plt.bar(initials_sorted, initial_counts, color='lightgreen')
plt.xlabel("Initial")
plt.ylabel("Number of characters")
plt.title("Initial Distribution in MteH")
plt.tight_layout()
plt.savefig(initial_plot_file, dpi=150)
plt.close()

# Finals
final_counter = Counter(fin for _, _, fin, _ in entries)
finals_sorted = sorted(final_counter.keys())
final_counts = [final_counter[f] for f in finals_sorted]

plt.figure(figsize=(12,4))
plt.bar(finals_sorted, final_counts, color='lightcoral')
plt.xlabel("Final")
plt.ylabel("Number of characters")
plt.title("Final Distribution in MteH")
plt.tight_layout()
plt.savefig(final_plot_file, dpi=150)
plt.close()

# -----------------------
# Write Markdown
# -----------------------
with open(output_file, "w", encoding="utf-8") as md:
    md.write(f"# MteH syllables: all component combinations\n\n")
    md.write(f"*Date: {datetime.now().strftime('%Y-%m-%d')}*\n\n")
    md.write(f"*Source file: {input_file}*\n\n")
    md.write(f"*Generated using Python code written by ChatGPT*\n\n")
    md.write(f"This report is automatically generated from the pinyin in the mteh file listed above.  There are two issues:\n\n")
    md.write(f" - MetH does not account for 多音字 (polyphones); each character is ascribed a single pronunciation.\n\n")
    md.write(f" - In some cases, pinyin does not accurately reflect actual pronunciation, e.g. chu → ㄔㄨ and qu → ㄑㄩ have different finals (u vs ü).\n\n")

    # Embed plots
    md.write("## Tone Distribution Plot\n\n")
    md.write(f"![Tone Distribution]({tone_plot_file})\n\n")

    md.write("## Initial Distribution Plot\n\n")
    md.write(f"![Initial Distribution]({initial_plot_file})\n\n")

    md.write("## Final Distribution Plot\n\n")
    md.write(f"![Final Distribution]({final_plot_file})\n\n")

    # Write subsets
    for subset in subsets:
        title = " + ".join(subset)
        write_section(md, title, mappings[subset], total_chars)

# -----------------------
# HSK New Syllables Section (Counts)
# -----------------------
new_syllables_counts = hsk_new_syllables(entries, hsk_levels)

with open(output_file, "a", encoding="utf-8") as md:
    md.write("## New Syllables by HSK Level\n\n")
    md.write("Counts are shown both **with tone** (full syllable) and **toneless** (initial+final only)\n\n")
    for level in ['1','2','3','4','5','6','7-9','n']:
        counts = new_syllables_counts[level]
        label = level if level != 'n' else 'non-HSK'
        md.write(f"- **HSK {label}**: {counts['with_tone']} new syllables (with tone), {counts['toneless']} new toneless syllables\n")
    md.write("\n---\n\n")

# -----------------------
# HSK New Syllables Section (Exhaustive Lists)
# -----------------------
syllable_lists = hsk_new_syllable_lists(entries, hsk_levels)

with open(output_file, "a", encoding="utf-8") as md:
    md.write("## Exhaustive New Syllables by HSK Level\n\n")
    md.write("### With Tone\n\n")
    for level in ['1','2','3','4','5','6','7-9','n']:
        label = level if level != 'n' else 'non-HSK'
        md.write(f"**HSK {label} ({len(syllable_lists[level]['with_tone'])} syllables)**:\n\n")
        md.write(', '.join(syllable_lists[level]['with_tone']) + "\n\n")

    md.write("### Toneless (Initial + Final only)\n\n")
    for level in ['1','2','3','4','5','6','7-9','n']:
        label = level if level != 'n' else 'non-HSK'
        md.write(f"**HSK {label} ({len(syllable_lists[level]['toneless'])} syllables)**:\n\n")
        md.write(', '.join(syllable_lists[level]['toneless']) + "\n\n")
    md.write("\n---\n\n")

# -----------------------
# Plot new syllables per HSK
# -----------------------
labels = ['1','2','3','4','5','6','7-9','n']
with_tone_counts = [new_syllables_counts[l]['with_tone'] for l in labels]
toneless_counts = [new_syllables_counts[l]['toneless'] for l in labels]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(10,4))
plt.bar(x - width/2, with_tone_counts, width, label='With Tone', color='orchid')
plt.bar(x + width/2, toneless_counts, width, label='Toneless', color='skyblue')
plt.xticks(x, labels)
plt.xlabel("HSK Level")
plt.ylabel("Number of new syllables")
plt.title("New MteH Syllables per HSK Level (With Tone vs Toneless)")
plt.legend()
plt.tight_layout()
plt.savefig(new_syllables_plot_file, dpi=150)
plt.close()

# Append plot to Markdown
with open(output_file, "a", encoding="utf-8") as md:
    md.write(f"![New Syllables by HSK Level]({new_syllables_plot_file})\n\n")

# -----------------------
print(f"Report generated: {output_file}")
print(f"Tone plot saved: {tone_plot_file}")
print(f"Initial plot saved: {initial_plot_file}")
print(f"Final plot saved: {final_plot_file}")
print(f"New syllables per HSK plot saved: {new_syllables_plot_file}")

