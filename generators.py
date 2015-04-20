from __future__ import print_function


def one_two_three_four(base):
    yield base + 1
    yield base + 2
    yield base + 3
    yield base + 4


for value in one_two_three_four(7):
    print("iterated", value)
"""
iterated 8
iterated 9
iterated 10
iterated 11
"""