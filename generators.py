from __future__ import print_function


def wait_for(x):
    print("waiting for", x)
    yield
    print(x[0])


nothing_yet = []


g = wait_for(nothing_yet)
next(g)
nothing_yet.append(3)
next(g)
