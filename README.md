# reus-runner: A Python Project Template

# Overview

`reus-runner` is designed to streamline the setup process for new Python projects by serving as a robust template or
boilerplate. This repository eliminates the repetitive tasks associated with configuring a new project from scratch. It
is ideal for Python developers looking to jumpstart their script development with a structured, feature-rich foundation.
Additionally, `reus-runner` supports packaging Python scripts into executable (.exe) files for easy distribution and
use.

---

# Quickstart Guide

## Use as Package

```bash
pip install git+https://github.com/AndreiGoriunov/reus-runner.git@v1.1.0
```

To create the default necessary files, run `reus-runner-create`. This will create the `config.properties` and `.root`.

To use the package, import `reus_runner` and run `initialize()`.  After this, you will be able to use `GlobalProperties` to access
project-specific settings from `config.properties` and command-line arguments.

## Use as Template

Download the zip or clone this repository's branch `template` to your local machine to get started. 
It includes a `main.py` script and a `config.properties` file.
As well as a `build.py` script to package the project into an executable (.exe) file.

```bash
git clone https://github.com/AndreiGoriunov/reus-runner.git@template
```

# CLI Commands

- `reus-runner-create`: Creates the necessary files for the project setup. Asks for user confirmation to create the
  files. If confirmed, it creates `.root` and `config.properties` files with default log settings.
- `reus-runner-build`: Creates a template file `build.py` in the current directory. You can use it to build your project
  into executable. Modify it if needed.

# Features

- **Configurable Properties**
  - Utilizes a `config.properties` file, which is included in the final build as a separate
    file. This allows for easy modification of settings even after the executable file has been generated.

- **Command-line Arguments**
  - Supports passing command-line arguments (`--key=value`) to both the `main.py` script and
    the generated .exe file. These arguments override and are merged with settings from `config.properties` and are
    accessible via the `GlobalProperties` singleton.

- **Execution Context Awareness**
  - The project can distinguish whether it is being run from a terminal as a Python file
    or from within a PyInstaller bundle, allowing for context-specific configurations.

- **GlobalProperties Singleton**
  - Features a `GlobalProperties` class that, once initialized in `main.py` with `reus_runner.initialize()`, 
    facilitates access to configuration settings and command-line arguments across different modules within the project.
  - You can also use `GlobalProperties` as cache for any other data that needs to be shared across modules.

# Prerequisites

- Python 3.12 (though it should work with 3.9+).

- PyInstaller to bundle the script into an .exe file, if desired.

  `pip install pyinstaller`

# Usage

1. Run `reus-runner-create` to create the necessary files:

    ```bash
    reus-runner-create
    ```
2. Initialize the project by running `reus_runner.initialize()`.
    
    Example:
    ```python
    from reus_runner import initialize, GlobalProperties
    
    def main():
        initialize()
    
    if __name__ == "__main__":
        main()
    ```

3. (Optional) Run `reus-runner-build` to create the build script (if you are planning to create an executable file):

    ```bash
    reus-runner-build
    ```

    To bundle your script into an .exe file, use the created python script `build.py`. You can change the name of the
    resulting .exe file by changing the `exe_name` variable in `build.py`.
    This script utilizes PyInstaller for packaging. After building, the .exe file and `config.properties` will be available
    in the `release` directory.

    ```bash
    python build.py
    ```

## Built-in Functionalities

- The `config.properties` file allows for easy configuration management and can be edited post-build for flexible
  settings adjustment.
- Command-line arguments enhance project configurability and are seamlessly integrated into the project's global
  properties.
- The `GlobalProperties` singleton ensures that configurations and runtime arguments are easily accessible throughout
  the project, promoting efficient cross-module communication.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This repository is intended for use as a template or as a package with starter utilities for personal projects and not for contributing to `reus-runner`
itself.
