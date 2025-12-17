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
.
├── CHANGELOG.md            A description of changes per version
├── docs                    Project documentation, in mkdocs format
├── Makefile                Automated tasks like environment setup, linting, and spellchecking
├── mkdocs.yml              The configuration file for the docs/ directory
├── poetry.lock
├── pyproject.toml
├── setup                   Environment support files
│   ├── dictionaries
│   ├── githooks
│   ├── githook_setup.sh
│   ├── preferences         Local preferences, see setup/preferences/examples/README.md
│   └── scripts
├── src
│   ├── {{ cookiecutter.project_slug }} This project
│   ├── data                Supporting files such as json, text, toml, etc.
│   └── examples            How to use the code
└── tests
    ├── functional          BDD tests
    └── unit                Unit tests
```

## Development

A Python development environment is encoded within this repository. To use it, execute:

```bash
make setup
```

### Unit and Functional Tests

```bash
make tests
```

If you want to know why coverage failed, you can run down the details.

```bash
make detail
```

Of course, since you are using test-driven development as a discipline, you won't need it that
much, will you?

### Spell Checking

```bash
make spellcheck
```

If you disagree with the spell checker, add words to `setup/dictionaries/whitelist`.

### Linting

```bash
make lint
```

### Committing and Pushing Changes

The prehooks will ensure you have run static checks before pushing to a repository.
