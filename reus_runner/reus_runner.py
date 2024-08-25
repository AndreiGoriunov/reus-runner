import logging
from os import path

from reus_runner import GlobalProperties, constants
from reus_runner.file_utils import parse_properties, get_root_dir
from reus_runner.utils import get_cmdline_args_as_dict, config_logger


def initialize():
    """Initializes Reus Runner.

    This function should be called in the entry script.
    """
    root_dir: str = get_root_dir()

    cmdline_props: dict[str, str] = get_cmdline_args_as_dict()
    config_props: dict[str, object] = parse_properties(
        path.join(root_dir, constants.CONFIG_PROPERTIES_PATH)
    )
    properties: dict[str, object] = config_props | cmdline_props

    GlobalProperties.initialize(properties)
    GlobalProperties.root_dir = root_dir  # type: ignore

    GlobalProperties.log_file = path.join(root_dir, GlobalProperties.log_file_name)  # type: ignore
    config_logger()

    logging.info(f"Global properties: {GlobalProperties.get_all()}")


def get_path_from_root(*paths: str) -> str:
    return path.join(GlobalProperties.get("root_dir", "./"), *paths)   # type: ignore
