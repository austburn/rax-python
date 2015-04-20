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
@logged
def hello():
    print("Hello!")


hello()
"""
Starting <function a_logged_thing at 0x7fe25a42e848>  NASTY!
Starting <function hello at 0x7fe25a42e7d0>
Hello!
Ending <function hello at 0x7fe25a42e7d0>
Ending <function a_logged_thing at 0x7fe25a42e848>
"""
