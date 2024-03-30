import logging
import sys

from .global_properties import GlobalProperties


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
