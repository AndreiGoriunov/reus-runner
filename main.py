from os import path

from config import get_root_dir, GlobalProperties
from config_constants import CONFIG_PROPERTIES_PATH
from utilities import parse_properties

def main():
    root_dir:str = get_root_dir()

    properties: dict[str, str] = parse_properties(
        path.join(root_dir, CONFIG_PROPERTIES_PATH)
    )

    GlobalProperties.initialize(properties)
    GlobalProperties.root_dir = root_dir # type: ignore
    GlobalProperties.log_file = path.join(root_dir, GlobalProperties.log_file_path) # type: ignore

    print(GlobalProperties.get("root_dir")) # type: ignore

if __name__ == "__main__":
    main()
