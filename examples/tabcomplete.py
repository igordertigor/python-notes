#!/usr/bin/env python
"""
This file needs argcomplete to be installed:

    pip install argcomplete

In addition, no would need to register the file for zsh:

    autoload bashcompinit
    bashcompinit
    eval "$(register-python-argcomplete tabcomplete.py)"

(for bash, you only need the last line).
"""

import argparse
import argcomplete

ELEMENTS = [
    'long_entry_that_could_be_chosen',
    'other_long_entry_that_is_difficult_to_remember',
    'yet_another_entry_that_we_do_not_want_to_type',
]


def parse_cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('element', choices=ELEMENTS)
    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    print(args.element)


if __name__ == "__main__":
    parse_cmd()
