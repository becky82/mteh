import json
import os
import genanki

# --- File paths ---
MTEH_FILE = "../mteh.txt"
GRAPHICS_FILE = "graphics.txt"
OUTPUT_APKG = "../mteh_anki_deck.apkg"

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

# --- Load graphics.txt ---
if not os.path.isfile(GRAPHICS_FILE):
    raise FileNotFoundError(
        f"'{GRAPHICS_FILE}' not found.\n"
        "Please download it from the Make Me a Hanzi project:\n"
        "https://github.com/skishore/makemeahanzi"
    )

graphics_dict = {}
with open(GRAPHICS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        entry = json.loads(line)
        graphics_dict[entry["character"]] = entry

# --- Prepare Anki deck ---
deck = genanki.Deck(
    2059400110,
    "More than enough Hanzi (MteH)"
)

model = genanki.Model(
    1607392319,
    "SVG Model",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Character"},
        {"name": "Pinyin"},
        {"name": "Hint"},
        {"name": "HSK_level"},
        {"name": "Structure"},
    ],
    templates=[{
        "name": "Card 1",
        "qfmt": '''
<style>
svg {
  width: 90%;
  height: auto;
  max-width: 700px;
}
div { text-align: center; }
</style>
{{Front}}''',
        "afmt": '''
<style>
svg {
  width: 90%;
  height: auto;
  max-width: 700px;
}
div { text-align: center; }
</style>
{{Back}}''',
    }]
)

# --- Step: Build all cards in memory ---
for line in open(MTEH_FILE, encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue

    parts = line.split()
    if len(parts) < 6:
        continue

    char = parts[0]
    pinyin = parts[1]
    example = parts[2]
    rank_str = parts[3]
    hsk = parts[4]
    enclosure_index = parts[5]
    enclosure_char = enclosure_map.get(enclosure_index, "⿻")

    if char not in graphics_dict:
        print(f"Warning: character {char} not found in graphics.txt")
        continue
    char_data = graphics_dict[char]

    # --- Frequency bar height ---
    try:
        rank = int(rank_str)
    except ValueError:
        rank = MAX_RANK
    freq_height = ((MAX_RANK - rank) / MAX_RANK) * 1024

    # --- HSK label ---
    hsk_text = "" if hsk in ["n", ""] else hsk

    # --- SVG stroke paths ---
    paths_svg = "\n".join(
        f'      <path d="{path_d}" fill="black"></path>'
        for path_d in char_data["strokes"]
    )

    # --- Generate SVG markup (back) ---
    svg_back = f'''<svg viewBox="-300 -200 1624 2024" xmlns="http://www.w3.org/2000/svg">
  <rect x="-300" y="-200" width="1624" height="2024" fill="white"/>
  <rect x="0" y="-124" width="60" height="{freq_height}" fill="gray" transform="scale(1, -1) translate(0, -900)"/>
  <rect width="1024" height="1024" fill="none" stroke="black" stroke-width="10"/>
  <text x="900" y="160" font-family="Arial" font-size="180" text-anchor="north" fill="gray">{hsk_text}</text>
  <g transform="scale(1, -1) translate(0, -900)">
{paths_svg}
  </g>
  <text x="512" y="1160" font-family="Arial" font-size="120" text-anchor="middle" fill="black">{pinyin}</text>
  <text x="512" y="1650" font-family="Arial" font-size="350" text-anchor="middle" fill="black">{example}</text>
</svg>'''

    # --- Generate SVG markup (front) ---
    example_front = example.replace(char, enclosure_char)
    svg_front = f'''<svg viewBox="-300 -200 1624 2024" xmlns="http://www.w3.org/2000/svg">
  <rect x="-300" y="-200" width="1624" height="2024" fill="white"/>
  <rect x="0" y="-124" width="60" height="{freq_height}" fill="gray" transform="scale(1, -1) translate(0, -900)"/>
  <rect width="1024" height="1024" fill="none" stroke="black" stroke-width="10"/>
  <text x="900" y="160" font-family="Arial" font-size="180" text-anchor="north" fill="gray">{hsk_text}</text>
  <text x="512" y="1160" font-family="Arial" font-size="120" text-anchor="middle" fill="black">{pinyin}</text>
  <text x="512" y="1650" font-family="Arial" font-size="350" text-anchor="middle" fill="black">{example_front}</text>
</svg>'''

    # Center in card
    front_html = f'<div style="text-align:center;">{svg_front}</div>'
    back_html = f'<div style="text-align:center;">{svg_back}</div>'

    note = genanki.Note(
        model=model,
        fields=[front_html, back_html, char, pinyin, example, hsk, enclosure_char],
    )
    deck.add_note(note)

# --- Save the deck ---
package = genanki.Package(deck)
package.write_to_file(os.path.abspath(OUTPUT_APKG))
print(f"✅ Anki deck created: {OUTPUT_APKG}")

