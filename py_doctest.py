# command to run doctests in Python files
# python -m doctest -v .\py_doctest.py

def add(x, y):
    """
    Adds together two numbers.
    >>> add(2, 3)
    5
    >>> add(5, 0)
    5

    >>> add(8, 'hi')
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    """
    return x + y

def double(values):
    """
    Doubles each value in a list.
    >>> double([1, 2, 3])
    [2, 4, 6]
    >>> double([0])
    [0]
    >>> double([-1, -2, -3])
    [-2, -4, -6]
    >>> double([True, None])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
    """
    return [x * 2 for x in values]

def say_hi():
    """
    Returns a greeting.
    >>> say_hi()
    "Hello, world!"
    """
    return "Hello, world!"

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)