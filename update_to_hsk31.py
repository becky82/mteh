from pathlib import Path

BASE = Path("sources/HSK3.1")
INPUT_FILE = Path("mteh.txt")
OUTPUT_FILE = Path("mteh_hsk31.txt")

# ------------------------------------------------------------
# 1. Build char → HSK level mapping (lowest level wins)
# ------------------------------------------------------------

char_level = {}

for level in range(1, 7):
    path = BASE / f"HSK3.1_chars_level{level}.txt"
    if not path.exists():
        continue
    for line in path.read_text(encoding="utf-8").splitlines():
        ch = line.strip()
        if not ch:
            continue
        char_level[ch] = min(char_level.get(ch, level), level)

# HSK 7–9 → "+"
path_79 = BASE / "HSK3.1_chars_level7-9.txt"
if path_79.exists():
    for line in path_79.read_text(encoding="utf-8").splitlines():
        ch = line.strip()
        if not ch:
            continue
        # only assign "+" if the character wasn't already 1–6
        char_level.setdefault(ch, "+")

# ------------------------------------------------------------
# 2. Rewrite mteh.txt with updated column 5
# ------------------------------------------------------------

out_lines = []

for line in INPUT_FILE.read_text(encoding="utf-8").splitlines():
    if line.startswith("#") or not line.strip():
        out_lines.append(line)
        continue

    parts = line.split()
    if len(parts) < 6:
        # malformed line — leave untouched
        out_lines.append(line)
        continue

    ch = parts[0]
    parts[4] = str(char_level.get(ch, "n"))
    out_lines.append(" ".join(parts))

OUTPUT_FILE.write_text("\n".join(out_lines) + "\n", encoding="utf-8")

