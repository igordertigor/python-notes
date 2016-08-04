from __future__ import absolute_import, division, unicode_literals, print_function


def func(*args, **kwargs):
    print('Function was called with args={} and kwargs={}'.format(args, kwargs))


def simpledecorator(decorate_me):

    def decorated(*args, **kwargs):
        print('I was decorated')
        return decorate_me(*args, **kwargs)

    return decorated


@simpledecorator
def func2(*args, **kwargs):
    print('Function that was decorated on construction was called with args={} and kwargs={}'.format(
        args, kwargs))


if __name__ == '__main__':
    func('Hello')
    func2('Hello')

    func = simpledecorator(func)
    func('Hello')
