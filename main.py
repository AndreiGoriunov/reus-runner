import logging
from os import path

from reus_runner import (
    GlobalProperties,
    config_logger,
    constants,
    get_cmdline_args_as_dict,
    parse_properties,
    get_root_dir,
)


def reus_runner_init():
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
    print(GlobalProperties.get_all())


def main():
    reus_runner_init()
    # Your code goes here
    input()  # (Optional) Wait for input to close the program


if __name__ == "__main__":
    main()
