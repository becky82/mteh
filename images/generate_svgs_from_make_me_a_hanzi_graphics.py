import json
import os
import sys

GRAPHICS_FILE = "graphics.txt"
MTEH_FILE = "../mteh.txt"
OUTPUT_DIR = "."

# --- Step 0: Check if graphics.txt exists ---
if not os.path.isfile(GRAPHICS_FILE):
    print(f"Error: '{GRAPHICS_FILE}' not found.")
    print("Please download it from: https://github.com/skishore/makemeahanzi")
    sys.exit(1)

# --- Step 1: Load characters from ../mteh.txt ---
mteh_chars = set()
with open(MTEH_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        char = line.split()[0]
        mteh_chars.add(char)

print(f"Loaded {len(mteh_chars)} characters from {MTEH_FILE}")

# --- Step 2: Prepare output directory ---
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- SVG templates ---
SVG_TEMPLATE = """<svg viewBox="0 0 1024 1024">
  <rect width="1024" height="1024" fill="white" stroke="black" stroke-width="10"/>
  <g transform="scale(1, -1) translate(0, -900)">
{paths}
  </g>
</svg>
"""
PATH_TEMPLATE = '      <path d="{d}" fill="black"></path>'

# --- Step 3: Generate SVGs directly ---
graphics_chars = set()
found_count = 0

with open(GRAPHICS_FILE, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            char = obj.get("character")
            if not char:
                continue
            graphics_chars.add(char)

            # Only generate for characters in mteh.txt
            if char not in mteh_chars:
                continue

            strokes = obj.get("strokes", [])
            path_elements = "\n".join(PATH_TEMPLATE.format(d=s) for s in strokes)
            svg_content = SVG_TEMPLATE.format(paths=path_elements)

            filename = f"{char}.svg"
            out_path = os.path.join(OUTPUT_DIR, filename)

            with open(out_path, "w", encoding="utf-8") as out:
                out.write(svg_content)

            found_count += 1
            print(f"✅ Saved {char} ({filename})")

        except json.JSONDecodeError:
            print(f"⚠️ Skipped malformed JSON on line {line_num}")
        except Exception as e:
            print(f"⚠️ Error on line {line_num}: {e}")

# --- Step 4: Report summary ---
print(f"\n✅ Generated SVGs for {found_count} characters.")
missing_chars = sorted(mteh_chars - graphics_chars)
if missing_chars:
    print(f"⚠️ {len(missing_chars)} characters not found in {GRAPHICS_FILE}:")
    print(" ".join(missing_chars))

