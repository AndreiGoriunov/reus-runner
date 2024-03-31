from constants import DEFAULT_LOG_FILE_NAME, DEFAULT_LOG_FORMAT


def setup():
    confirm: str = input(
        "Setup will create 2 necessary files.\n- config.properties\n- .root\n\nCreate the files? (Y/N): "
    )

    if confirm.lower() != "y":
        return

    with open(".root", "w") as f:
        f.write("A file marking the root of the project")

    with open("config.properties", "w") as f:
        f.write(f"log_file_name = {DEFAULT_LOG_FILE_NAME}")
        f.write(f"log_format = '{DEFAULT_LOG_FORMAT}'")

    print("Setup complete. Necessary files have been created.")
