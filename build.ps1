$exeName = "reus-runner.exe"

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