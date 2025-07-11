import math


def product_1_to_100():
    """Calculates the product of numbers from 1 to 100 (100!)."""
    return math.factorial(100)


def my_product(n):
    """Calculates the product of numbers from 1 to n (n!)."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n == 0 or n == 1:
        return 1
    return math.factorial(n)


def my_product_iterative(n):
    """Calculates the product of numbers from 1 to n using iterative approach."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # Calculate and display the product of 1 to 100
    result = product_1_to_100()
    print(f"Product of numbers from 1 to 100: {result}")
    print(f"Number of digits: {len(str(result))}")
    
    # Test with smaller numbers
    print(f"\nTest cases:")
    print(f"Product of 1 to 5: {my_product(5)}")  # Should be 120
    print(f"Product of 1 to 10: {my_product(10)}")  # Should be 3628800