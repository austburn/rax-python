from contextlib import contextmanager


@contextmanager
def example():
    print("starting!")
    yield 3
    print("finishing up...")


with example() as something:
    print(something)