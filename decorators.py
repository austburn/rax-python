from __future__ import print_function
from functools import wraps


def logged(function):
    @wraps(function)
    def a_logged_thing(*args, **kwargs):
        print("Starting", function,
              args, kwargs)
        try:
            function(*args, **kwargs)
        finally:
            print("Ending", function,
                  args, kwargs)
    return a_logged_thing


@logged
@logged
def hello(world):
    print("Hello!", world)


hello("Austin")
"""
Starting <function hello at 0x7f28c0752aa0> ('Austin',) {}
Starting <function hello at 0x7f28c0752a28> ('Austin',) {}
Hello! Austin
Ending <function hello at 0x7f28c0752a28> ('Austin',) {}
Ending <function hello at 0x7f28c0752aa0> ('Austin',) {}
"""
