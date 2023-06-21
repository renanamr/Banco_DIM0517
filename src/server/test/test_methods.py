import pytest

def add(a, b):
    return a + b

def test_add():
    result = add(2, 3)
    assert result == 5

    result = add(-1, 1)
    assert result == 0

