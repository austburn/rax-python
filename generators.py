from __future__ import print_function


def one_two_three_four(base):
    n = 0
    while n < 4:
        yield base + n
        n = n + 1


for value in one_two_three_four(7):
    print("iterated", value)
"""
iterated 7
iterated 8
iterated 9
iterated 10
"""