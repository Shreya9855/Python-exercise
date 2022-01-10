# Please raise a RuntimeError exception.

def example():
    try:
        var = int("AVV")
    except ValueError as e:
        raise RuntimeError('An error occured') from e

example()