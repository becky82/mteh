# Generates multiple LaTeX code files from ../mteh.txt
# Output:
#   ./mteh_input_HSK5.txt
#   ./mteh_input_HSK6.txt
#   ./mteh_input_HSK7-9.txt
#   ./mteh_input.txt   (complete)

# Define output files
outputs = {
    "HSK5": open("./mteh_input_HSK5.txt", "w", encoding="utf-8"),
    "HSK6": open("./mteh_input_HSK6.txt", "w", encoding="utf-8"),
    "HSK7-9": open("./mteh_input_HSK7-9.txt", "w", encoding="utf-8"),
    "ALL": open("./mteh_input.txt", "w", encoding="utf-8"),
}

# Keep counts for each output file
counts = {key: 0 for key in outputs}

with open("../mteh.txt", "r", encoding="utf-8") as f_in:
    for line in f_in:
        line = line.strip()
        # Skip empty lines or comments
        if not line or line.startswith("#"):
            continue

        # Split the line into fields
        parts = line.split(maxsplit=5)
        if len(parts) != 6:
            print("Skipping malformed line:", line)
            continue

        char, pinyin, hint, freq, hsk, structure = parts

        # Leave HSK blank if it's "n"
        hsk_display = "" if hsk.lower() == "n" else hsk

        # Replace all occurrences of the character in the hint
        hint_latex = hint.replace(char, f"\\square{{{structure}}}")

        # Generate the LaTeX line
        latex_line = f"\\character{{{char}}}{{{pinyin}}}{{{hint_latex}}}{{{freq}}}{{{hsk_display}}}\n"

        # Always write to the full version
        outputs["ALL"].write(latex_line)
        counts["ALL"] += 1

        # Determine inclusion by HSK level
        hsk_upper = hsk.upper()
        if hsk_upper in ["1", "2", "3", "4", "5"]:
            for k in ["HSK5", "HSK6", "HSK7-9"]:
                outputs[k].write(latex_line)
                counts[k] += 1
        elif hsk_upper == "6":
            for k in ["HSK6", "HSK7-9"]:
                outputs[k].write(latex_line)
                counts[k] += 1
        elif hsk_upper == "+":
            outputs["HSK7-9"].write(latex_line)
            counts["HSK7-9"] += 1

# Close all files
for f in outputs.values():
    f.close()

# Print summary
print("\n✅ Generation complete. Files created:")
print(f"  ./mteh_input_HSK5.txt    ({counts['HSK5']} entries)")
print(f"  ./mteh_input_HSK6.txt    ({counts['HSK6']} entries)")
print(f"  ./mteh_input_HSK7-9.txt  ({counts['HSK7-9']} entries)")
print(f"  ./mteh_input.txt         ({counts['ALL']} entries)")

