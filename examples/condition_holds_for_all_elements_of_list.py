from __future__ import absolute_import, division, unicode_literals, print_function


def ispositive(x):
    return x > 0


def iseven(x):
    return (x % 2) == 0


def true_for_all(condition, thelist):
    return all(map(condition, thelist))


if __name__ == "__main__":
    thelist = [2, 34, -2]
    print('All elements of {} are positive: {}'.format(
        thelist,
        true_for_all(ispositive, thelist),
    ))

    print('All elements of {} are even: {}'.format(
        thelist,
        true_for_all(iseven, thelist),
    ))
