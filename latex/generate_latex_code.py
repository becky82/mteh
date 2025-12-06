# Generates multiple LaTeX code files from ../mteh.txt
# Output:
#   ./mteh_input_HSK5.txt
#   ./mteh_input_HSK6.txt
#   ./mteh_input_HSK7-9.txt
#   ./mteh_input_HSK5+.txt
#   ./mteh_input_HSK6+.txt
#   ./mteh_input_HSK7-9+.txt
#   ./mteh_input_nonHSK.txt
#   ./mteh_input.txt   (complete)

# Define output files
outputs = {
    "HSK5": open("./mteh_input_HSK5.txt", "w", encoding="utf-8"),
    "HSK6": open("./mteh_input_HSK6.txt", "w", encoding="utf-8"),
    "HSK7-9": open("./mteh_input_HSK7-9.txt", "w", encoding="utf-8"),
    "HSK5+": open("./mteh_input_HSK5+.txt", "w", encoding="utf-8"),
    "HSK6+": open("./mteh_input_HSK6+.txt", "w", encoding="utf-8"),
    "HSK7-9+": open("./mteh_input_HSK7-9+.txt", "w", encoding="utf-8"),
    "NON-HSK": open("./mteh_input_nonHSK.txt", "w", encoding="utf-8"),
    "ALL": open("./mteh_input.txt", "w", encoding="utf-8"),
}

counts = {key: 0 for key in outputs}

with open("../mteh.txt", "r", encoding="utf-8") as f_in:
    for line in f_in:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split(maxsplit=5)
        if len(parts) != 6:
            print("Skipping malformed line:", line)
            continue

        char, pinyin, hint, freq, hsk, structure = parts

        # Replace missing freq with max value
        if freq.lower() == "n":
            freq = "7000"

        hsk = hsk.lower()
        is_non_hsk = (hsk == "n")

        # For LaTeX display: blank for non-HSK, otherwise the level
        hsk_display = "" if is_non_hsk else hsk

        # Replace character with □ in hint
        hint_latex = hint.replace(char, f"\\square{{{structure}}}")

        latex_line = (
            f"\\character{{{char}}}{{{pinyin}}}"
            f"{{{hint_latex}}}{{{freq}}}{{{hsk_display}}}\n"
        )

        # ----- Write to ALL -----
        outputs["ALL"].write(latex_line)
        counts["ALL"] += 1

        # ---- Interpret HSK levels ----
        is_hsk1_4 = hsk in ["1","2","3","4"]
        is_hsk5   = (hsk == "5")
        is_hsk6   = (hsk == "6")
        is_hsk7_9 = (hsk == "7-9") or (hsk == "+")  # allow + as 7-9 marker

        # ================================================
        #   CUMULATIVE SETS — up to a level (HSK5,6,7-9)
        # ================================================
        if is_hsk1_4 or is_hsk5:
            outputs["HSK5"].write(latex_line)
            counts["HSK5"] += 1
        if is_hsk1_4 or is_hsk5 or is_hsk6:
            outputs["HSK6"].write(latex_line)
            counts["HSK6"] += 1
        if is_hsk1_4 or is_hsk5 or is_hsk6 or is_hsk7_9:
            outputs["HSK7-9"].write(latex_line)
            counts["HSK7-9"] += 1

        # ================================================
        #   PLUS SETS — level *or above*
        # ================================================
        if is_hsk5 or is_hsk6 or is_hsk7_9 or is_non_hsk:
            outputs["HSK5+"].write(latex_line)
            counts["HSK5+"] += 1
        if is_hsk6 or is_hsk7_9 or is_non_hsk:
            outputs["HSK6+"].write(latex_line)
            counts["HSK6+"] += 1
        if is_hsk7_9 or is_non_hsk:
            outputs["HSK7-9+"].write(latex_line)
            counts["HSK7-9+"] += 1

        # ================================================
        #   NON-HSK ONLY
        # ================================================
        if is_non_hsk:
            outputs["NON-HSK"].write(latex_line)
            counts["NON-HSK"] += 1

# Close files
for f in outputs.values():
    f.close()

# Summary
print("\n✅ Generation complete. Files created:")
for key in outputs:
    print(f"  ./mteh_input_{key}.txt   ({counts[key]} entries)")

