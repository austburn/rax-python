from __future__ import print_function
from functools import wraps


def logged(function):
    @wraps(function)
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
Starting <function hello at 0x7fda3b637a28>
Starting <function hello at 0x7fda3b6379b0>
Hello!
Ending <function hello at 0x7fda3b6379b0>
Ending <function hello at 0x7fda3b637a28>
"""
