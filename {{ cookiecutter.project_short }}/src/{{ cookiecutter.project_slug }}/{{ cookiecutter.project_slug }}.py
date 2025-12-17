"""[A one-line summary of the module or program, ended with a period].

{{ cookiecutter.project_slug }}.py Copyright {{ cookiecutter.year }} {{ cookiecutter.full_name }}

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in
compliance with the License.

You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License
is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied. See the License for the specific language governing permissions and limitations under the
License.


Description:

This module serves only to ensure that python unit testing can go ahead.

Typical usage example:

poetry run python -m pytest tests/unit

"""

from typing import Any


class X:
    """Summary of class.

    Longer class information

    Attributes:
        thing_a:
        thing_b:
    """

    def __init__(self):
        """Initiate an X object.

        Args:
            thing_a: description of thing_a
            thing_b: description of thing_b

        Returns:
            object X
        """
        self.thing_a: Any = None
        self.thing_b: Any = None

    def public_function(self, my_var: str) -> int | None:
        """The summary of the function and it must end with a period followed by a blank line.

        A deeper description if necessary but only if the information is useful. One should not
        need to describe easy-to-understand algorithms but perhaps the reason for it.

        Args:
            my_var: the value to send back.

        Returns:
            A tail call returning the string case as an integer or None. Yes, the programmer is
            aware that this is Python.
        """
        try:
            return int(my_var)
        except ValueError:
            return None

if __name__ == "__main__":
    x = X()
    return public_function(5)

