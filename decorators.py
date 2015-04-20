from __future__ import print_function


def logged(function):
    print("Starting", function)
    try:
        function()
    finally:
        print("Ending", function)


def hello():
    print("Hello!")

logged(hello)
"""
Starting <function hello at 0x7f4800ba47d0>
Hello!
Ending <function hello at 0x7f4800ba47d0>
"""
