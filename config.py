import logging
import sys
from os import path
from threading import Lock
from typing import Any


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


def config_logger(level: int = logging.INFO, log_file: str | None = None) -> None:
    """Set up logging."""
    if not log_file:
        _log_file: str = GlobalProperties.log_file  # type: ignore
    else:
        _log_file: str = log_file

    log_format: str = GlobalProperties.log_format  # type: ignore
    logging.basicConfig(level=level, format=log_format, filename=_log_file, filemode="a")  # type: ignore


def get_cmdline_args_as_dict() -> dict[str, str]:
    """Parses command line arguments in the format: --key=value.

    Returns a dictionary.
    """
    properties: dict[str, str] = {}
    for arg in sys.argv[1:]:  # Skip the script name
        if arg.startswith("--"):
            key_value = arg[2:].split(
                "=", 1
            )  # Remove '--' and split by '=', limit split to 1
            if len(key_value) == 2:
                key, value = key_value
                properties[key] = value

    return properties


class GlobalProperties:
    _instance = None
    _lock = Lock()
    _is_initialized: bool = False

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(GlobalProperties, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, properties: dict[str, Any]) -> Any:
        with cls._lock:
            if not cls._is_initialized:
                for key, value in properties.items():
                    setattr(cls, key, value)
                cls._is_initialized = True
            else:
                print("GlobalProperties is already initialized.")

    @classmethod
    def get_all(cls):
        return {
            k: v
            for k, v in cls.__dict__.items()
            if not k.startswith("_") and not callable(getattr(cls, k))
        }

    @classmethod
    def add(cls, key: str, value: Any):
        if " " in key:
            print(
                f"Attempt to add key '{key}' with white space. White space will be replaced with '_'."
            )
            key.replace(" ", "_")
        setattr(cls, key, value)

    @classmethod
    def get(cls, key: str, default: Any = None):
        """
        Safely retrieve a configuration value.

        :param key: The attribute name to retrieve.
        :param default: The default value to return if the attribute does not exist.
        :return: The attribute value if it exists, otherwise the default value.
        """
        return getattr(cls, key, default)
