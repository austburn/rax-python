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
def hello(world="test"):
    print("Hello!", world)


hello(world="Austin")
"""
Starting <function hello at 0x7f4ed1454aa0> () {'world': 'Austin'}
Starting <function hello at 0x7f4ed1454a28> () {'world': 'Austin'}
Hello! Austin
Ending <function hello at 0x7f4ed1454a28> () {'world': 'Austin'}
Ending <function hello at 0x7f4ed1454aa0> () {'world': 'Austin'}
"""
