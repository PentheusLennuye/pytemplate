---
date: {{ cookiecutter.today_iso }}
tags: {{ cookiecutter.tags }}
author: {{ cookiecutter.full_name }}
---

# {{ cookiecutter.project_name }}

This project does this for who.

Why

## Licence

The code and documentation is licensed under the Apache 2.0 licence. See the LICENSE file in the
repository.

## Security

The code security policy, including how to log an issue, is in SECURITY.md in the repository.

## Project layout

```text
mkdocs.yml    # The documentation configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.
examples/     # How to use the library
src/          # The executable and libraries. As it expands, so will the folders
test/         # Unit testing. Functional and integration testing are not applicable.
```

## Development

```bash
make setup
```

