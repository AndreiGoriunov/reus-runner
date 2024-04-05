CONFIG_PROPERTIES_PATH: str = "./config.properties"

DEFAULT_CONFIG_PROPERTIES: str = r"""
log_file_name = log.log
log_format = "[%(asctime)s] [%(levelname)s] in %(name)s: %(message)s"
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
