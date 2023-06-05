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


def sum_even_numbers(numbers: list[int]) -> int:
    """Given a list of integers, return the sum of all even numbers in the list."""
    return sum(num for num in numbers if num % 2 == 0)
