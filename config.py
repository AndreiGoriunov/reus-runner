import sys
from os import path


def get_root_dir() -> str:
    """Returns a root directory path."""
    if getattr(sys, "frozen", False):
        # The script is running inside a PyInstaller bundle
        print("Running inside a PyInstaller bundle")
        return path.dirname(sys.executable)
    else:
        # The script is running in a normal Python environment
        print("Running from .py file")
        script_path = path.abspath(__file__)
        return path.dirname(script_path)
