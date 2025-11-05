import json
import os

# --- File paths ---
MTEH_FILE = "../mteh.txt"
GRAPHICS_FILE = "graphics.txt"
OUTPUT_DIR = "flashcard_svgs"

# --- Constants ---
MAX_RANK = 7238  # For frequency bar calculation

# --- Enclosure mapping ---
enclosure_map = {
    "0": "⿻",
    "1": "⿰",
    "2": "⿱",
    "3": "⿲",
    "4": "⿳",
    "5": "⿴",
    "6": "⿵",
    "7": "⿶",
    "8": "⿷",
    "9": "⿸",
    "10": "⿹",
    "11": "⿺",
    "12": "⿻",
}

# --- Load graphics ---
if not os.path.isfile(GRAPHICS_FILE):
    raise FileNotFoundError(
        f"'{GRAPHICS_FILE}' not found.\n"
        "Please download it from the Make Me a Hanzi project:\n"
        "https://github.com/skishore/makemeahanzi"
    )

with open(GRAPHICS_FILE, "r", encoding="utf-8") as f:
    graphics_lines = f.readlines()

graphics_dict = {}
for line in graphics_lines:
    entry = json.loads(line)
    graphics_dict[entry["character"]] = entry

# --- Prepare output directory ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Process characters ---
with open(MTEH_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Parse columns
        parts = line.split()
        char = parts[0]
        pinyin = parts[1]
        example = parts[2]
        rank_str = parts[3]
        hsk = parts[4]
        enclosure_index = parts[5] if len(parts) > 5 else "0"
        enclosure_char = enclosure_map.get(enclosure_index, "⿻")

        # Handle rank
        if rank_str.isdigit():
            rank = int(rank_str)
        else:
            rank = int(parts[4])
        freq_height = ((MAX_RANK - rank) / MAX_RANK) * 1024

        # HSK text
        hsk_text = ""
        if hsk == "n":
            hsk_text = ""
        elif hsk == "+":
            hsk_text = "+"
        else:
            hsk_text = hsk

        # Get graphics
        if char not in graphics_dict:
            print(f"Warning: character {char} not found in graphics.txt")
            continue
        char_data = graphics_dict[char]

        # --- Back SVG (unchanged) ---
        paths_svg = ""
        for path_d in char_data["strokes"]:
            paths_svg += f'      <path d="{path_d}" fill="black"></path>\n'

        svg_back = f'''<svg viewBox="-300 -200 1624 2024" xmlns="http://www.w3.org/2000/svg">

  <!-- Background; frequency; box; HSK level -->
  <rect x="-300" y="-200" width="1624" height="2024" fill="white"/>
  <rect x="0" y="-124" width="60" height="{freq_height}" fill="gray" transform="scale(1, -1) translate(0, -900)"/>
  <rect width="1024" height="1024" fill="none" stroke="black" stroke-width="10"/>
  <text x="900" y="160" font-family="Arial" font-size="180" text-anchor="north" fill="gray">{hsk_text}</text>

  <!-- Make Me a Hanzi character data -->
  <g transform="scale(1, -1) translate(0, -900)">
{paths_svg}  </g>

  <!-- Pinyin; Hint -->
  <text x="512" y="1160" font-family="Arial" font-size="120" text-anchor="middle" fill="black">{pinyin}</text>
  <text x="512" y="1650" font-family="Arial" font-size="350" text-anchor="middle" fill="black">{example}</text>
</svg>'''

        filename_back = os.path.join(OUTPUT_DIR, f"{char}_back.svg")
        with open(filename_back, "w", encoding="utf-8") as f_out:
            f_out.write(svg_back)

        # --- Front SVG ---
        # Replace occurrences of the character in example with enclosure_char
        example_front = example.replace(char, enclosure_char)

        svg_front = f'''<svg viewBox="-300 -200 1624 2024" xmlns="http://www.w3.org/2000/svg">

  <!-- Background; frequency; box; HSK level -->
  <rect x="-300" y="-200" width="1624" height="2024" fill="white"/>
  <rect x="0" y="-124" width="60" height="{freq_height}" fill="gray" transform="scale(1, -1) translate(0, -900)"/>
  <rect width="1024" height="1024" fill="none" stroke="black" stroke-width="10"/>
  <text x="900" y="160" font-family="Arial" font-size="180" text-anchor="north" fill="gray">{hsk_text}</text>

  <!-- Pinyin; Hint -->
  <text x="512" y="1160" font-family="Arial" font-size="120" text-anchor="middle" fill="black">{pinyin}</text>
  <text x="512" y="1650" font-family="Arial" font-size="350" text-anchor="middle" fill="black">{example_front}</text>
</svg>'''

        filename_front = os.path.join(OUTPUT_DIR, f"{char}_front.svg")
        with open(filename_front, "w", encoding="utf-8") as f_out:
            f_out.write(svg_front)

