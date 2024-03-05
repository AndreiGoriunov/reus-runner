def parse_properties(file_path: str) -> dict[str, str]:
    properties: dict[str, str] = {}
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                value: str = value.strip()
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                properties[key.strip()] = value
    return properties
