# Generates the LaTeX code mteh_input.txt from ../mteh.txt

# Open the input and output files
with open("../mteh.txt", "r", encoding="utf-8") as f_in, open("./mteh_input.txt", "w", encoding="utf-8") as f_out:
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
        if hsk.lower() == "n":
            hsk = ""
        
        # Replace all occurrences of the character in the hint
        hint_latex = hint.replace(char, f"\\square{{{structure}}}")
        
        # Write the LaTeX line
        f_out.write(f"\\character{{{char}}}{{{pinyin}}}{{{hint_latex}}}{{{freq}}}{{{hsk}}}\n")

