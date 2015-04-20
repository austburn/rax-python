from __future__ import print_function


def logged(function):
    def a_logged_thing():
        print("Starting", function)
        try:
            function()
        finally:
            print("Ending", function)
    return a_logged_thing


@logged
def hello():
    print("Hello!")


hello()
"""
Starting <function hello at 0x7fbc034b47d0>
Hello!
Ending <function hello at 0x7fbc034b47d0>
"""
