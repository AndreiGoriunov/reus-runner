# reus-runner: A Python Project Template

## Overview

`reus-runner` is designed to streamline the setup process for new Python projects by serving as a robust template or boilerplate. This repository eliminates the repetitive tasks associated with configuring a new project from scratch. It is ideal for Python developers looking to jumpstart their script development with a structured, feature-rich foundation. Additionally, `reus-runner` supports packaging Python scripts into executable (.exe) files for easy distribution and use.

## Features

- **Configurable Properties**: Utilizes a `config.properties` file, which is included in the final build as a separate file. This allows for easy modification of settings even after the executable file has been generated.
- **Command-line Arguments**: Supports passing command-line arguments (`--key=value`) to both the `main.py` script and the generated .exe file. These arguments are merged with settings from `config.properties` and are accessible via the `GlobalProperties` singleton.
- **Execution Context Awareness**: The project can distinguish whether it is being run from a terminal as a Python file or from within a PyInstaller bundle, allowing for context-specific configurations.
- **GlobalProperties Singleton**: Features a `GlobalProperties` class that, once initialized in `main.py`, facilitates access to configuration settings and command-line arguments across different modules within the project.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. 
This project has been developed and tested with Python 3.12 (though it should work with 3.9+). 
You will also need PyInstaller to bundle the script into an .exe file, if desired.

### Installation

1. Clone the repository or download it as a zip file and extract it to your local machine.

2. If you plan to bundle the project into an executable (.exe) file, install the required dependency by running:

  ```bash
  pip install -r requirements.txt
  ```
  This step installs PyInstaller, which is used for creating the executable. If you do not require an executable version of your project, you can skip this step.

3. Customize the config.properties file according to your project's needs. This file is crucial for setting up project-specific configurations and can be edited at any time, even after the project has been bundled into an executable.

### Usage

To run your Python script:
```bash
python main.py --key=value
```

To bundle your script into an .exe file, use the provided PowerShell script `build.ps1`. You can change the name of the resulting .exe file by changing the `$exeName` vairable in `build.ps1`.
This script utilizes PyInstaller for packaging. After building, the .exe file and `config.properties` will be available in the `release` directory.

## Built-in Functionalities

- The `config.properties` file allows for easy configuration management and can be edited post-build for flexible settings adjustment.
- Command-line arguments enhance project configurability and are seamlessly integrated into the project's global properties.
- The `GlobalProperties` singleton ensures that configurations and runtime arguments are easily accessible throughout the project, promoting efficient cross-module communication.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This repository is intended for use as a template for personal projects and not for contributing to `reus-runner` itself.

---

Feel free to adjust this template to better fit your project's nuances or specific instructions.
