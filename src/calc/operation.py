class InvalidOperation(Exception):
    ...


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise InvalidOperation("Denominator must be not null!")
