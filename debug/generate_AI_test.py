import os

# CONFIG
INPUT_FILE = "../versions/v0.1.3/mteh_v0.1.3.txt"
OUTPUT_DIR = "ai_batches"
BATCH_SIZE = 100
PLACEHOLDER = "＿"  # character to replace missing answer

# mapping of structure code to Unicode characters
STRUCT_MAP = {
    "0": "none",        # none
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
    "12": "⿻"
}

# ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# read all non-comment lines
entries = []
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 6:
            continue  # skip malformed lines
        char, pinyin, hint, freq, hsk, struct_code = parts[:6]
        cloze_hint = hint.replace(char, PLACEHOLDER)
        struct_char = STRUCT_MAP.get(struct_code, "")
        entries.append({
            "char": char,
            "pinyin": pinyin,
            "cloze": cloze_hint,
            "freq": freq,
            "hsk": hsk,
            "struct": struct_char
        })

# split into batches
for batch_num, i in enumerate(range(0, len(entries), BATCH_SIZE), start=1):
    batch_entries = entries[i:i+BATCH_SIZE]
    filename = f"batch_{batch_num:02}.txt"  # zero-padded
    output_file = os.path.join(OUTPUT_DIR, filename)
    with open(output_file, "w", encoding="utf-8") as f:

        # Write AI instructions / prompt for “fill in the hint” mode
        f.write("```\n")
        f.write("以下是中文填空题，每个短语中有一个缺失的汉字，用 '＿' 表示。\n")
        f.write("有时同一个汉字可能在短语中出现多次，会有多个空格，但每条题目只有一个目标汉字。\n")
        f.write("频率最大值为 7000，数字越大表示越生僻。\n\n")
        f.write(
            "请根据上下文补全每条短语中的缺失部分（用 '＿' 表示的空格），生成完整短语。\n"
        )
        f.write(
            "输出编号和对应短语，每行包含 10 条短语，总共 100 条，分 10 行，严格按照编号顺序。\n"
        )
        f.write(
            "请将答案包在一个 Markdown 代码块中，用三条反引号开头和结尾，只输出代码块内容，不要添加解释或其他内容。\n"
        )
        f.write("```\n\n")

        # Write numbered cloze entries
        for idx, e in enumerate(batch_entries, start=1):
            f.write(
                f"{idx}. {e['cloze']} "
                f"(pinyin: {e['pinyin']}, freq: {e['freq']}, HSK:{e['hsk']}, struct:{e['struct']})\n"
            )
    print(f"Batch {batch_num:02} written: {len(batch_entries)} entries -> {output_file}")

