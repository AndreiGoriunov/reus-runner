from utilities import parse_properties
from helpers import config_constants


def main():
    properties: dict = parse_properties(config_constants.CONFIG_PROPERTIES_PATH)
    print(properties)


if __name__ == "__main__":
    main()
