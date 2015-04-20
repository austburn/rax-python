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
    return 3


print(hello(world="Austin") + 4)
"""
Starting <function hello at 0x7f1509b30a28> () {'world': 'Austin'}
Starting <function hello at 0x7f1509b309b0> () {'world': 'Austin'}
Hello! Austin
Ending <function hello at 0x7f1509b309b0> () {'world': 'Austin'}
Ending <function hello at 0x7f1509b30a28> () {'world': 'Austin'}
Traceback (most recent call last):
  File "decorators.py", line 25, in <module>
    print(hello(world="Austin") + 4)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
"""
