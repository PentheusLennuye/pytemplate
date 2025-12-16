#!/usr/bin/env python
"""Create a reference markdown readable to Obsidian from a template."""

from datetime import datetime
import pathlib
import sys

from fpsupport import struct, jinja
from fpsupport.monad import Monad, unwrap

SRC_DIR = pathlib.Path(__file__).resolve().parent
TEMPLATE_DIR = f"{SRC_DIR}/../templates"
REF_TEMPLATE = f"{TEMPLATE_DIR}/reference-book.md.j2"

FEATURES = {
    "time_created": datetime.now().astimezone().isoformat(timespec="minutes"),
    "type": "book",
    "title": "Nothing Time Cannot Handle",
    "subtitle": "A Journey Into Madness",
    # Always family name, comma, given names
    "authors": ["Cummings, George", "Sterescu, Anca", "McLean, Patrick Stuart"],
    "date": "2025-12-15",
    "edition": "2",
    "location": "Montreal",
    "publisher": "Atlas",
    "series": "How to do things",
    "volume": "5",
    "better_bibtex_key": "", 
    "full_title": "",
    "authors_cmos_bibliography": "",
}

def main(features: dict) -> None:
    """Start here."""
    data = unwrap(
        (
            Monad(features)
            >> set_full_title
            >> set_better_bibtex_key
            >> set_authors_cmos_bibliography
        )
    )

    io = struct.IOType()
    result = jinja.render_from_file(Monad(io), REF_TEMPLATE, data)
    if not result:
        print(f"error: {REF_TEMPLATE} not found")
        sys.exit(1)
    print(result)


def set_full_title(f: dict) -> Monad:
    """Create the full title for bibliography and footnotes."""
    if f["subtitle"] is None:
        return Monad(f| {"full_title": f['title']})
    else:
        return Monad(f| {"full_title": ": ".join([f['title'], f['subtitle']])})


def set_better_bibtex_key(f: dict) -> Monad:
    """Create the '@' short form of the citation for Zettelkasten reference links.

    The result would be: @shakespeareTamingOfThe1630
    
    """

    tokens = "".join(filter(alphanumeric_and_spaces, f["title"])).split()
    if tokens[0] == "The":
        tokens.pop(0)
    bibtex_title = "".join(tokens[:min(len(tokens), 3)])

    if "date" in f:
        year = f["date"].split("-")[0]
    elif "date_accessed" in f:
        year = f["date_accessed"].split("-")[0]
    else:
        year = ""

    # Set the initial author's last name in lower
    sn = f["authors"][0].split(",")[0].lower()

    # Create the better bibtex key
    result = f"@{sn}{bibtex_title}{year}"

    return Monad(f|{"better_bibtex_key": result})


def alphanumeric_and_spaces(c: str) -> bool:
    """Returns True if the character is alphanumeric or a space."""
    if c.isalnum() or c == " ":
        return True
    return False


def set_authors_cmos_bibliography(f: dict) -> Monad:
    """Create the author citation in Chicago format for bibliographies.

    The names should already be listed in order of impact with the format: family name, given names

    sn, given names
    sn, given names, given names sn (1), given names sn (2), and given names sn (3)
    sn, given names, gn sn (1), gn sn (2), ..., and gn sn (x)  ( if there are four or more)
    sn, given names, gn sn (x) for x = 1 to 7, et al.  (if > 10 authors)
    """

    if len(f["authors"]) < 1:
        return Monad(f| {"authors_cmos_bibliography": "Anonymous."})

    if len(f["authors"]) == 1:
        return Monad(f| {"authors_cmos_bibliography": f"{f['authors'][0]}."})

    co_authors = list(map(initials_surname, f["authors"][1:]))

    if len(f["authors"]) < 4:
        return Monad("not ready for < 4")

    if len(f["authors"]) < 10:
        co_author_string = ", ".join(co_authors[:-1]) + ", and " + co_authors[-1]
        return Monad(f| {"authors_cms_bibliography": f"{f['authors'][0]}, {co_author_string}."})

    return Monad("not ready for > 10")


def initials_surname(name: str) -> str:
    """From surname, given names return initials surname."""
    sn, given_names = name.split(", ")
    initials = ".".join( [i[0].upper() for i in given_names.split()] ) + "."
    return f"{initials} {sn}"


def invert_name(name: str) -> str:
    """Transform last name, given names to given names last name."""
    sn, given_names = name.split(", ")
    return f"{given_names} {sn}"


if __name__ == "__main__":
    main(FEATURES)
