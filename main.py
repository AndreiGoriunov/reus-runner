import logging
from os import path

from config import get_root_dir
from utilities import GlobalProperties, get_cmdline_args_as_dict, config_logger
from config_constants import CONFIG_PROPERTIES_PATH
from utilities import parse_properties


def reus_init():
    root_dir: str = get_root_dir()

    cmdline_props: dict[str, str] = get_cmdline_args_as_dict()
    config_props: dict[str, str] = parse_properties(
        path.join(root_dir, CONFIG_PROPERTIES_PATH)
    )

    properties: dict[str, str] = config_props | cmdline_props

    GlobalProperties.initialize(properties)
    GlobalProperties.log_file = path.join(root_dir, GlobalProperties.log_file_name)  # type: ignore
    config_logger()
    GlobalProperties.root_dir = root_dir  # type: ignore
    logging.info(f"Root directory is set to: '{root_dir}'")


def main():
    reus_init()
    # Your code goes here


if __name__ == "__main__":
    main()
