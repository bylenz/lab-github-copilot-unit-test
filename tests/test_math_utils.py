import pytest

from math_utils import generate_fibonacci, factorial


def test_generate_fibonacci_empty():
    assert generate_fibonacci(0) == []


def test_generate_fibonacci_single():
    assert generate_fibonacci(1) == [0]


def test_generate_fibonacci_five():
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]


def test_generate_fibonacci_seven():
    assert generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_generate_fibonacci_negative_raises():
    with pytest.raises(ValueError, match="non-negative"):
        generate_fibonacci(-1)


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_one():
    assert factorial(1) == 1


def test_factorial_positive():
    assert factorial(5) == 120


def test_factorial_negative_raises():
    with pytest.raises(ValueError, match="not defined for negative"):
        factorial(-3)
