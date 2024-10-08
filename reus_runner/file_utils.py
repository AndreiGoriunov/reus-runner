import sys
from os import path
from ast import literal_eval


def parse_properties(file_path: str) -> dict[str, object]:
    """Parses .properties file with contents in 'key = value' format.
    Ignores lines starting with '#'.

    Args:
        file_path (str): The path to the .properties file.

    Returns a dictionary.
    """
    properties: dict[str, object] = {}
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                value = value.strip()
                try:
                    # Try to evaluate the value as a Python literal
                    value = literal_eval(value)
                except (ValueError, SyntaxError):
                    # If evaluation fails, keep the value as a string
                    value = value.strip('"').strip("'")
                properties[key.strip()] = value
    return properties


def _find_root_dir(current_dir: str) -> str:
    """
    Recursively searches for a directory containing the .root file,
    indicating the root directory of the project.
    """
    if path.exists(path.join(current_dir, ".root")):
        # .root file found, current_dir is the root directory
        return current_dir
    else:
        parent_dir = path.dirname(current_dir)
        if parent_dir == current_dir:
            # Reached the filesystem root without finding a .root file
            raise FileNotFoundError(
                "Root directory with .root not found. Please ensure the project contains a .root file at the root."
            )
        return _find_root_dir(parent_dir)


def get_root_dir() -> str:
    """Returns the project root directory path."""
    if getattr(sys, "frozen", False):
        # The script is running inside a PyInstaller bundle
        print("Running inside a PyInstaller bundle")
        return path.dirname(sys.executable)
    else:
        # The script is running in a normal Python environment
        print("Running from .py file")
        script_path = path.abspath(__file__)
        script_dir = path.dirname(script_path)
        return _find_root_dir(script_dir)
