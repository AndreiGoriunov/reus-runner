from .constants import BUILD_SCRIPT_PY, DEFAULT_CONFIG_PROPERTIES


def create() -> None:
    """
    A function to create necessary files for the project setup.
    Asks for user confirmation to create the files.
    If confirmed, it creates .root and config.properties files with default log settings.
    """
    confirm: str = input(
        """Reus Runner will create 2 files for your project in the current directory:
            - config.properties
            - .root
            
        Create the files? (Y/N): """
    )

    if confirm.lower() != "y":
        return

    # Create .root file ===================================================
    with open(".root", "w") as f:
        f.write("A file marking the root of the project")

    # Create config.properties file =======================================
    with open("config.properties", "w") as f:
        f.write(f"{DEFAULT_CONFIG_PROPERTIES}")

    print("Necessary project files have been created.")


def build() -> None:
    """
    A function to create a template file "build.py" in the current directory.
    You can use it to build your project into executable. Modify it if needed.
    """
    confirm: str = input(
        """Reus Runner will create a template file "build.py" in the current directory.
        You can use it to build your project into executable. Modify it if needed.
        
        Create the file? (Y/N): """
    )

    if confirm.lower() != "y":
        return

    # Create build.py file ================================================
    with open("build.py", "w") as f:
        f.write(BUILD_SCRIPT_PY)

    print("File build.py has been created.")
