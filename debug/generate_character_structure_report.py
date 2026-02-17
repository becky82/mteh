"""
MteH Character Structure Report Generator
Written by ChatGPT
"""

import datetime
import os

# Input/output files
mteh_file = '../mteh.txt'
char_struct_file = './char_structures.txt'
output_file = 'character_structure_report.md'

# Mapping: first character of decomposition → structure code and icon
structure_map = {
    "⿰": (1, "⿰"),
    "⿱": (2, "⿱"),
    "⿲": (3, "⿲"),
    "⿳": (4, "⿳"),
    "⿴": (5, "⿴"),
    "⿵": (6, "⿵"),
    "⿶": (7, "⿶"),
    "⿷": (8, "⿷"),
    "⿸": (9, "⿸"),
    "⿹": (10, "⿹"),
    "⿺": (11, "⿺"),
    "⿻": (12, "⿻"),
    "0": (0, "None"),   # simple / single-component character
    "？": (0, "None"),  # col 2 no-structure
}

# Reverse map: number -> icon for MteH
number_to_icon = {v[0]: v[1] for k, v in structure_map.items() if v[0] != 0}

# Map importance levels to exclamation marks
importance_icons = {
    "Low": "❗",
    "Medium": "❗❗",
    "High": "❗❗❗"
}

def normalize(char, mteh_code):
    """Return tuple (code, icon) with normalization for missing structures"""
    if char == "？" or (len(char) == 1 and mteh_code == 0):
        return (0, "None")
    return structure_map.get(char, (None, "None"))

def format_col(icon, code):
    """Return 'icon [code]' or 'None' if missing"""
    if code == 0 or icon == "None" or code is None:
        return "None"
    return f"{icon} [{code}]"

# Read char_structures.txt
char_struct = {}
with open(char_struct_file, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        char, dict_first, ids_first = line.split('\t')
        char_struct[char] = (dict_first, ids_first)

# Collect mismatches
mismatches = []
total_chars = 0

with open(mteh_file, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        if len(fields) < 6:
            continue
        char = fields[0]
        total_chars += 1
        try:
            mteh_code = int(fields[5])
        except ValueError:
            continue
        if char not in char_struct:
            continue
        dict_first, ids_first = char_struct[char]
        dict_code, dict_icon = normalize(dict_first, mteh_code)
        ids_code, ids_icon = normalize(ids_first, mteh_code)
        
        # Lookup MteH icon from number
        mteh_icon = number_to_icon.get(mteh_code, "None")
        
        if mteh_code != dict_code or mteh_code != ids_code:
            # Determine importance
            mteh_vs_dict = mteh_code != dict_code
            mteh_vs_ids = mteh_code != ids_code
            dict_vs_ids = dict_code != ids_code
            
            if (mteh_vs_dict + mteh_vs_ids) == 1:
                importance = "Low"
            elif (mteh_vs_dict + mteh_vs_ids) == 2:
                if dict_vs_ids:
                    importance = "Medium"
                else:
                    importance = "High"
            else:
                importance = "Low"  # fallback
            
            mismatches.append({
                "Character": char,
                "MteH_Code": mteh_code,
                "MteH_Icon": mteh_icon,
                "Dict_Code": dict_code,
                "Dict_Icon": dict_icon,
                "IDs_Code": ids_code,
                "IDs_Icon": ids_icon,
                "Importance": importance_icons[importance]
            })

consistent_count = total_chars - len(mismatches)

# Output report
with open(output_file, 'w', encoding='utf-8') as f:
    # Header
    f.write("# MteH Character Structure Report\n\n")
    f.write(f"Report generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}; Python script written by ChatGPT.\n\n")
    f.write(f"Checking MteH: {os.path.basename(mteh_file)}\n\n")
    f.write(f"## [{len(mismatches)}] Character structure consistency\n\n")  # Updated title
    
    # Table
    f.write("| Character | MteH | Make me a Hanzi | cjkvi-ids | Importance |\n")
    f.write("|-----------|-----------------|-----------------|----------------|------------|\n")
    for m in mismatches:
        f.write(f"| {m['Character']} | "
                f"{format_col(m['MteH_Icon'], m['MteH_Code'])} | "
                f"{format_col(m['Dict_Icon'], m['Dict_Code'])} | "
                f"{format_col(m['IDs_Icon'], m['IDs_Code'])} | "
                f"{m['Importance']} |\n")
    
    # Summary
    f.write(f"\n**Consistent characters:** {consistent_count}\n")
    f.write(f"**Inconsistent characters:** {len(mismatches)}\n")

print(f"Report written to {output_file} ({len(mismatches)} mismatches, {consistent_count} consistent characters)")

