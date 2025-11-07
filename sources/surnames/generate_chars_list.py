#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

input_path = "./familyname.csv"

chars = set()

with open(input_path, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        surname = row["surname"].strip()
        for ch in surname:
            if ch.strip():
                chars.add(ch)

for ch in sorted(chars):
    print(ch)

