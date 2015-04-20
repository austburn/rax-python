from __future__ import print_function

from pkg_resources import resource_stream

def some_func():
    with resource_stream(__name__.split(".")[0], "something.data") as f:
        print("hello, entry points!", f.read())
