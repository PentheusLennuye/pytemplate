#!/usr/bin/env python
"""Using the enchant-2 module, check the spelling of a file or directory.

{{ cookiecutter.project_slug }}/setup/scripts/spellcheck.py Copyright {{ cookiecutter.year }} {{ cookiecutter.full_name }}

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied. See the License for the specific language governing permissions and limitations under the
License.

Usage:
   spellcheck.py [-d <language>] [-p <personal dictionary>,...] <path>

"""

import argparse
import enchant

DEFAULT_LANG = "en_CA"

def main() -> None:
    """Start here."""
    parser = argparse.ArgumentParser(
        prog="spellcheck.py",
        description="Check the spelling on files using the enchant-2 library",
    )
    parser.add_argument(
        '-d',
        '--dictionary',
        type=str,
        required=False,
        help="The language available on your system.", default=DEFAULT_LANG
    )
    parser.add_argument(
        '-p',
        '--personal-dictionaries',
        type=str,
        required=False,
        help="A comma-delimited list of word files to supplement the main language dictionary"
    )
    parser.add_argument(
        'path',
        type=str,
        required=False,
        help="A space-delimited list of files and paths to inspect"
    )
    parser.parse_args()


if __name__ == "__main__":
    main()
