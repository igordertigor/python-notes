#!/usr/bin/env python

from __future__ import print_function, absolute_import, division, unicode_literals

import itertools


def lists_concat(list_of_lists):
    return list(itertools.chain(*list_of_lists))


if __name__ == "__main__":
    list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]

    print(lists_concat(list_of_lists))
