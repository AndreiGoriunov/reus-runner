#!/bin/bash

# Define the executable name
exeName="reus-runner"

# Directories to remove
directories=("dist" "build" "release")

# Remove directories if they exist
for dir in "${directories[@]}"; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"
    fi
done

# Remove all __pycache__ directories
find . -name "__pycache__" -type d -exec rm -rf {} \;

# Run pyinstaller
pyinstaller --onefile main.py

# Create 'release' directory if it doesn't exist
if [ ! -d "release" ]; then
    mkdir "release"
fi

echo "Copying files into 'release' directory..."

# Copy the config file to the release folder
cp config.properties release/config.properties

# Wait for a few seconds (adjust the time as needed)
sleep 3

# Copy and rename the main.exe file to the release folder
cp dist/main.exe release/$exeName

echo "Complete."