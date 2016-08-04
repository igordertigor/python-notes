#!/usr/bin/env python
from __future__ import print_function, absolute_import, unicode_literals, division

import functools
import itertools
import numpy as np


def groupby(A, keyfunc):
    return itertools.groupby(sorted(A, key=keyfunc), keyfunc)


def keyfromcols(row, columns):
    return tuple(row[i] for i in columns)


if __name__ == "__main__":
    A = 8.+np.random.poisson(.2, size=(200, 4))

    # Group by columns [0, 1, 2]
    getkey = functools.partial(keyfromcols, columns=[0, 1, 2])

    print('Get lengths of the different groups')
    for grp in groupby(A, getkey):
        print(grp[0], len(list(grp[1])))

    print('Get mean of last element over the different groups')
    for grp in groupby(A, getkey):
        print(grp[0], np.mean([v[-1] for v in grp[1]])))
