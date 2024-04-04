from .constants import DEFAULT_LOG_FILE_NAME, DEFAULT_LOG_FORMAT


def create():
    """
    A function to create necessary files for the project setup.
    Asks for user confirmation to create the files.
    If confirmed, it creates .root and config.properties files with default log settings.
    """
    confirm: str = input(
        "Setup will create 2 necessary files.\n- config.properties\n- .root\n\nCreate the files? (Y/N): "
    )

    if confirm.lower() != "y":
        return

    try:
        with open(".root", "w") as f:
            f.write("A file marking the root of the project")
    except Exception as e:
        print(f"Failed to create .root file: {e}")

    with open("config.properties", "w") as f:
        f.write(f"{DEFAULT_LOG_FILE_NAME}\n")
        f.write(f"{DEFAULT_LOG_FORMAT}\n")

    print("Setup complete. Necessary files have been created.")
