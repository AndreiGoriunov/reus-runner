from setuptools import setup, find_packages

setup(
    name="reus_runner",
    version="1.1.0",
    packages=find_packages(),
    author="AndreiGoriunov",
    license="MIT",
    keywords="Python Template Runner",
    url="https://github.com/AndreiGoriunov/reus-runner",
    entry_points={
        "console_scripts": [
            "reus-runner-create = reus_runner.cli:create",
            "reus-runner-build = reus_runner.cli:build",
        ]
    },
)
