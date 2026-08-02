"""Tests for main.py."""

from main import add


def test_add():
    """Test addition."""
    assert add(10, 5) == 15, "Expected 10 + 5 to equal 15"
