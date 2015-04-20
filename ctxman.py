from contextlib import contextmanager


@contextmanager
def example():
    print("starting!")
    try:
        yield 3
    except ZeroDivisionError:
        print("caught exception")
    finally:
        print("finishing up...")


with example() as something:
    print(something)
    1/0

print("guarded?!")
