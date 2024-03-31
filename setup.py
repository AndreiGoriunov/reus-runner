from setuptools import setup, find_packages

setup(
    name="reus_runner",
    version="1.0.0",
    packages=find_packages(),
    install_requires=['pyinstaller>=6.4.0'],
    author="AndreiGoriunov",
    license="MIT",
    keywords="Python Template Runner",
    url="https://github.com/AndreiGoriunov/reus-runner",
    entry_points={"console_scripts": ["reus-runner-create = reus_runner.cli:create"]},
)
