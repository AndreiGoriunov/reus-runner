import logging
from os import path

from reus_runner import GlobalProperties, constants
from reus_runner.file_utils import parse_properties, get_root_dir
from reus_runner.utils import get_cmdline_args_as_dict, config_logger


def initialize():
    """Initializes Reus Runner."""
    root_dir: str = get_root_dir()

    cmdline_props: dict[str, str] = get_cmdline_args_as_dict()
    config_props: dict[str, str] = parse_properties(
        path.join(root_dir, constants.CONFIG_PROPERTIES_PATH)
    )

    properties: dict[str, str] = config_props | cmdline_props

    GlobalProperties.initialize(properties)
    GlobalProperties.log_file = path.join(root_dir, GlobalProperties.log_file_name)  # type: ignore
    config_logger()
    GlobalProperties.root_dir = root_dir  # type: ignore
    logging.info(f"Root directory is set to: '{root_dir}'")
