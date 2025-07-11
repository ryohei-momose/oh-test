import unittest
import math
from product_function import product_1_to_100, my_product, my_product_iterative


class TestProductFunction(unittest.TestCase):
    """Test cases for product functions."""

    def test_product_1_to_100(self):
        """Test the product of 1 to 100."""
        result = product_1_to_100()
        expected = math.factorial(100)
        self.assertEqual(result, expected)
        
        # Verify it's a very large number (100! has 158 digits)
        self.assertEqual(len(str(result)), 158)

    def test_my_product_small_numbers(self):
        """Test my_product with small numbers."""
        self.assertEqual(my_product(0), 1)  # 0! = 1
        self.assertEqual(my_product(1), 1)  # 1! = 1
        self.assertEqual(my_product(2), 2)  # 2! = 2
        self.assertEqual(my_product(3), 6)  # 3! = 6
        self.assertEqual(my_product(4), 24)  # 4! = 24
        self.assertEqual(my_product(5), 120)  # 5! = 120

    def test_my_product_larger_numbers(self):
        """Test my_product with larger numbers."""
        self.assertEqual(my_product(10), 3628800)  # 10!
        self.assertEqual(my_product(12), 479001600)  # 12!

    def test_my_product_iterative_small_numbers(self):
        """Test my_product_iterative with small numbers."""
        self.assertEqual(my_product_iterative(0), 1)
        self.assertEqual(my_product_iterative(1), 1)
        self.assertEqual(my_product_iterative(5), 120)
        self.assertEqual(my_product_iterative(10), 3628800)

    def test_both_methods_consistency(self):
        """Test that both methods give the same results."""
        for n in range(0, 15):
            self.assertEqual(my_product(n), my_product_iterative(n))

    def test_error_handling_my_product(self):
        """Test error handling for my_product."""
        with self.assertRaises(ValueError):
            my_product(-1)
        with self.assertRaises(ValueError):
            my_product(-10)
        with self.assertRaises(TypeError):
            my_product(5.5)
        with self.assertRaises(TypeError):
            my_product("5")

    def test_error_handling_my_product_iterative(self):
        """Test error handling for my_product_iterative."""
        with self.assertRaises(ValueError):
            my_product_iterative(-1)
        with self.assertRaises(ValueError):
            my_product_iterative(-10)
        with self.assertRaises(TypeError):
            my_product_iterative(5.5)
        with self.assertRaises(TypeError):
            my_product_iterative("5")

    def test_large_factorial(self):
        """Test with larger factorials."""
        # Test that 100! is calculated correctly
        result_100 = my_product(100)
        expected_100 = math.factorial(100)
        self.assertEqual(result_100, expected_100)
        
        # Test that both methods work for 100!
        self.assertEqual(my_product(100), my_product_iterative(100))


if __name__ == '__main__':
    unittest.main()