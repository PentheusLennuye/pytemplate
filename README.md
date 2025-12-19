# PyTemplate

This is a cookie cutter template for Python projects. It is highly opinionated.

## Features

- A `pyproject.toml` file with strict linting
- A Makefile
  - Whose `setup` target will ensure Python development packages for testing, linting, and
    documentation are installed and available in the virtual environment
  - That is usable in NixOS systems where the owner opts for using `poetry` instead of the NixOS
    way of Python development.
- Scripts for spell checking
- Git hooks to ensure gitflow, version checks, linting, and unit tests are all done prior to push
- A docs directory pre-filled with boilerplate documentation
- A mkdocs configuration that can be used right away.
- Boilerplate unit tests
