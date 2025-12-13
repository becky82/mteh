# compare_side_by_side.py

answers_file = "ChatGPT_answers_v0.1.2.txt"
corpus_file = "../../versions/v0.1.2/mteh_v0.1.2.txt"

# Load corpus phrases into a list, preserving order
corpus_phrases_lines = []
with open(corpus_file, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        corpus_phrases_lines.append(line)

# Load ChatGPT answers
with open(answers_file, encoding="utf-8") as f:
    answers = [line.strip() for line in f if line.strip()]

# Compare line by line
print(f"{'Line':<6} {'ChatGPT Answer':<12} {'Corpus Line'}")
print("-"*80)
for i, (chatgpt, corpus_line) in enumerate(zip(answers, corpus_phrases_lines), 1):
    if chatgpt != corpus_line.split()[2]:  # compare to phrase in corpus
        print(f"{i:<6} {chatgpt:<12} {corpus_line}")

