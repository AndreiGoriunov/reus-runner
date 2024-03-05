import sys
from os import path
from threading import Lock
from typing import Any
import logging


def get_root_dir() -> str:
    """Should only be called from the root."""
    if getattr(sys, "frozen", False):
        # The script is running inside a PyInstaller bundle
        print("Running inside a PyInstaller bundle")
        return path.dirname(sys.executable)
    else:
        # The script is running in a normal Python environment
        print("Running from .py file")
        script_path = path.abspath(__file__)
        return path.dirname(script_path)


class GlobalProperties:
    _instance = None
    _lock = Lock()
    _is_initialized: bool = False

    properties: dict[str, str] = {}

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
            print(f"Attempt to add key '{key}' with white space. White space will be replaced with '_'.")
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


def config_logger(level: int = logging.INFO, log_file: str | None = None):
    if not log_file:
        log_file = GlobalProperties.log_file  # type: ignore
