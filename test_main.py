"""Tests for main.py."""

from main import add, subtract


def test_add():
    """Test addition."""
    assert add(10, 5) == 15, "Expected 10 + 5 to equal 15"


def test_subtract():
    """Test subtraction."""
    assert subtract(10, 5) == 5, "Expected 10 - 5 to equal 5"
