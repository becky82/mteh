# Usage example:
#
# python3 check_website_non_mteh.py [URL]

#!/usr/bin/env python3
import requests
import re
import sys
from collections import Counter
from bs4 import BeautifulSoup
from opencc import OpenCC

# Initialize Traditional → Simplified converter
cc = OpenCC('t2s')

# Load MteH characters
mteh_chars = set()
with open("../mteh.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        mteh_chars.add(line.split()[0])

# Define strokes to ignore
strokes = set("丨丿㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉")

# Get URL
if len(sys.argv) < 2:
    print("Usage: python check_all_chars.py <URL>")
    sys.exit(1)
url = sys.argv[1]

# Fetch page
try:
    r = requests.get(url)
    r.raise_for_status()
except Exception as e:
    print(f"Error fetching URL: {e}")
    sys.exit(1)

# Parse HTML and extract visible text
soup = BeautifulSoup(r.text, "html.parser")
for tag in soup(["script", "style"]):
    tag.decompose()
visible_text = soup.get_text(separator=" ")

# Convert to simplified
simplified_text = cc.convert(visible_text)

# Extract Chinese characters, ignoring single-stroke characters
chinese_chars = [c for c in re.findall(r'[\u4e00-\u9fff]', simplified_text) if c not in strokes]
print(f"Total Chinese characters found on page (excluding strokes): {len(chinese_chars)}\n")

# Count all characters
all_counter = Counter(chinese_chars)
print("All Chinese characters (char:freq):")
print(" ".join(f"{char}:{freq}" for char, freq in all_counter.most_common()))
print()

# Count non-MteH characters
non_mteh_chars = [c for c in chinese_chars if c not in mteh_chars]
if non_mteh_chars:
    non_counter = Counter(non_mteh_chars)
    print("Non-MteH characters (char:freq):")
    print(" ".join(f"{char}:{freq}" for char, freq in non_counter.most_common()))
else:
    print("All characters on this page are in MteH ✅")

