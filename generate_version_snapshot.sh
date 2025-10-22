#!/bin/bash

# Set your version manually
VERSION="0.1.1"

# Create version directory
VERSION_DIR="./versions/v$VERSION"
mkdir -p "$VERSION_DIR"

# List of files to snapshot
FILES=(
    "./mteh.txt"
    "./latex/mteh_all_answers.pdf"
    "./latex/mteh_HSK5_answers.pdf"
    "./latex/mteh_HSK6_answers.pdf"
    "./latex/mteh_HSK7-9_answers.pdf"
    "./latex/mteh_all_noanswers.pdf"
    "./latex/mteh_HSK5_noanswers.pdf"
    "./latex/mteh_HSK6_noanswers.pdf"
    "./latex/mteh_HSK7-9_noanswers.pdf"
)

# Copy files with version appended
for FILE in "${FILES[@]}"; do
    if [ -f "$FILE" ]; then
        BASENAME=$(basename "$FILE")
        EXT="${BASENAME##*.}"
        NAME="${BASENAME%.*}"
        cp "$FILE" "$VERSION_DIR/${NAME}_v${VERSION}.${EXT}"
    else
        echo "Warning: $FILE does not exist, skipping."
    fi
done

echo "Snapshot v$VERSION created in $VERSION_DIR"

