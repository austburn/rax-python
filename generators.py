from __future__ import print_function


def one_two_three_four():
    yield 1
    yield 2
    yield 3
    yield 4


for value in one_two_three_four():
    print("iterated", value)
"""
iterated 1
iterated 2
iterated 3
iterated 4
"""