import logging
import sys
from os import path

from .global_properties import GlobalProperties


def config_logger(level: int = logging.INFO, log_file: str | None = None) -> None:
    """Set up basic logging configuration."""

    # If log_file is None, get the log_file_name from GlobalProperties
    if not log_file:
        if not GlobalProperties.get("log_file_name"):
            print("log_file_name property is not set. Logging won't be enabled.")
            return
        else:
            log_file = path.join(GlobalProperties.root_dir, GlobalProperties.log_file_name)  # type: ignore
            GlobalProperties.log_file = log_file

    log_format: str = GlobalProperties.log_format  # type: ignore
    if not log_format:
        print("log_format property is not set. Logging won't be enabled.")
        return

    # Set up basic logging configuration
    logging.basicConfig(level=level, format=log_format, filename=log_file, filemode="a")  # type: ignore


def get_cmdline_args_as_dict() -> dict[str, str]:
    """Parses command line arguments in the format: --key=value.

    Returns a dictionary as {key: value}.
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
