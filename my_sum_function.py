def my_sum(n):
    """Calculates the sum of numbers from 1 to n."""
    if n < 1:
        return 0  # Handle invalid input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    return n * (n + 1) // 2