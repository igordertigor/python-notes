#!/usr/bin/env python
from __future__ import print_function, absolute_import, unicode_literals, division

import functools
import operator

if __name__ == "__main__":
    dictionary = {'a': -1, 'b': 5, 'c': 1, 'd': 2}

    keyfunc = functools.partial(operator.getitem, dictionary)

    for key in sorted(dictionary, key=keyfunc):
        print(key, dictionary[key])
