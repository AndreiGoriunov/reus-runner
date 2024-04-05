"""Reus Runner provides a handy set of utilities for writing Python projects.

To use the package, simply import it and call initialize(), preferably in your entry script.

Example:
    from reus_runner import GlobalProperties, initialize

    def main():
        initialize()

    if __name__ == "__main__":
        main()

Use `GlobalProperties` class to access global properties set from `config.properties` file or command-line arguments.
You can also use `GlobalProperties` as cache for any other data that needs to be shared across modules.

For more detailed documentation, please visit:
https://github.com/AndreiGoriunov/reus-runner
"""

from .global_properties import GlobalProperties
from .reus_runner import initialize
