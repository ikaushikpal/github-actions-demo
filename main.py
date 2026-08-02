"""Simple calculator module."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the subtract of two numbers."""
    return a - b


if __name__ == "__main__":
    print(f"Adding 2 + 3 = {add(2, 3)}")
    print(f"Subtracting 2 - 3 = {subtract(2, 3)}")
