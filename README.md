# PyTemplate

This is a cookie cutter template for Python projects. It is highly opinionated.

## Features

- A `pyproject.toml` with strict linting
- A Makefile
  - Whose `setup` target will ensure Python development packages for testing, linting, and documentation are installed and available in the virtual environment
  - That is usable in NixOS systems using `poetry` instead of the native NixOS way of Python development
- Scripts for spell checking
- A docs/ directory with boilerplate documentation
- A mkdocs configuration usable right away
