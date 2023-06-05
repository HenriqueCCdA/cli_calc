import pytest

from src.calc.operation import (
    InvalidOperation,
    add,
    div,
    mult,
    sub,
)


@pytest.mark.parametrize(
    "a,b,r",
    [
        (4, 5, 9),
        (4.0, 0.0, 4.0),
        (4.0, 1.1, 5.1),
    ],
)
def test_add(a, b, r):
    assert add(a, b) == r


@pytest.mark.parametrize(
    "a,b,r",
    [
        (4, 5, -1),
        (5, 4, 1),
        (4.0, 0.0, 4.0),
        (4.0, 1.1, 2.9),
    ],
)
def test_sub(a, b, r):
    assert sub(a, b) == r


@pytest.mark.parametrize(
    "a,b,r",
    [
        (4, 5, 20),
        (5, 4, 20),
        (4.0, 0.0, 0.0),
        (4.0, 1.1, 4.4),
    ],
)
def test_mult(a, b, r):
    assert mult(a, b) == r


@pytest.mark.parametrize(
    "a,b,r",
    [
        (4, 5, 0.8),
        (5, 4, 1.25),
        (0, 4, 0.0),
        (4.0, 1.5, 2.6666),
    ],
)
def test_div(a, b, r):
    assert div(a, b) == pytest.approx(r, abs=1.0e-4)


def test_div_by_zero():
    with pytest.raises(InvalidOperation):
        div(5, 0)
