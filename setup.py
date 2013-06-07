from setuptools import setup

setup(
    name="mdconf.py",
    version="0.0.1",
    author="hit9",
    author_email="nz2324@126.com",
    description=(
        """
        Python implementation for visionmedia's mdconf - Markdown driven configuration
        """
    ),
    license="MIT",
    keywords="mdconf, markdown, configuration",
    url="https://github.com/hit9/mdconf.py",
    py_modules=["mdconf"],
    install_requires=["misaka"]
)
