#!/bin/bash
set -e

# Script to download and extract DejaVu fonts for PDF report generation

FONT_DIR="investchecker/output"
ZIP_URL="https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-2.37.zip"
ZIP_FILE="$FONT_DIR/dejavu-fonts-ttf-2.37.zip"

mkdir -p "$FONT_DIR"

echo "Downloading DejaVu fonts..."
curl -L -o "$ZIP_FILE" "$ZIP_URL"

echo "Extracting fonts..."
unzip -o "$ZIP_FILE" -d "$FONT_DIR"

echo "Cleaning up..."
rm "$ZIP_FILE"

echo "DejaVu fonts downloaded and extracted to $FONT_DIR."
