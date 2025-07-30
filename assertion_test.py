def add_positive_numbers(a, b):
    """Adds two positive numbers."""
    assert a >= 0 and b >= 0, "Both numbers must be non-negative"
    return a + b


def eat_junk(food):
    """Simulates eating junk food."""
    assert food in ["chips", "candy", "soda"], "Food must be junk food"
    return f"Eating {food}"



print(add_positive_numbers(-5, 10))  # Should raise an AssertionError
print(eat_junk("chips"))  # Should return "Eating chips"
