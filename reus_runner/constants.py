CONFIG_PROPERTIES_PATH: str = "./config.properties"

DEFAULT_CONFIG_PROPERTIES: str = r"""
log_file_name = log.log
log_format = "[%(asctime)s] [%(levelname)s] in %(name)s: %(message)s"
"""

BUILD_SCRIPT_PS1: str = r"""$exeName = "reus-runner.exe"

# Directories to remove
$directories = @("dist", "build", "release")

# Remove dist, build, and release directories if they exist
foreach ($dir in $directories) {
    if (Test-Path $dir) {
        Remove-Item -Recurse -Force $dir
    }
}

# Remove all __pycache__ directories
Get-ChildItem -Path . -Filter "__pycache__" -Recurse -Directory | Remove-Item -Force -Recurse

# Run pyinstaller
pyinstaller --onefile main.py

# Create 'release' directory if it doesn't exist
if (-not (Test-Path -Path .\release)) {
    New-Item -Path .\release -ItemType Directory
}

Write-Host "Copying files into 'release' directory..."

# Copy the config file to the release folder
Copy-Item -Path .\config.properties -Destination .\release\config.properties -Force

# Wait for a few seconds (adjust the time as needed)
Start-Sleep -Seconds 3

# Copy and rename the main.exe file to the release folder
Copy-Item -Path ".\dist\main.exe" -Destination ".\release\$exeName" -Force

Write-Host "Complete."
"""

BUILD_SCRIPT_SH: str = r"""#!/bin/bash

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
"""

BUILD_SCRIPT_PY: str = r"""import os
import shutil
import time

from PyInstaller.__main__ import run as pyinstaller_run

# Feel free to change the following values
exe_name = "reus-runner.exe"
main_file = "main.py"


def main():

    # Directories to remove
    directories = ["dist", "build", "release"]

    # Remove dist, build, and release directories if they exist
    for dir_ in directories:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)

    # Remove all __pycache__ directories
    for root, dirs, files in os.walk("."):
        for dir_ in dirs:
            if dir_ == "__pycache__":
                shutil.rmtree(os.path.join(root, dir_))

    # Run pyinstaller programmatically
    pyinstaller_run(["--onefile", main_file])

    # Create 'release' directory if it doesn't exist
    os.makedirs("release", exist_ok=True)

    print("Copying files into 'release' directory...")

    # Copy the config file to the release folder
    shutil.copy("config.properties", os.path.join("release", "config.properties"))

    # Wait for a few seconds (adjust the time as needed)
    time.sleep(3)

    # Copy and rename the main.exe file to the release folder
    shutil.copy(os.path.join("dist", "main.exe"), os.path.join("release", exe_name))

    print("Complete.")


if __name__ == "__main__":
    main()

"""
