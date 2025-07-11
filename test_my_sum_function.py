import unittest
from my_sum_function import my_sum


class TestMySumFunction(unittest.TestCase):
    """Test cases for my_sum function."""

    def test_positive_numbers(self):
        """Test with positive integers."""
        self.assertEqual(my_sum(1), 1)
        self.assertEqual(my_sum(5), 15)  # 1+2+3+4+5 = 15
        self.assertEqual(my_sum(10), 55)  # 1+2+...+10 = 55
        self.assertEqual(my_sum(100), 5050)  # 1+2+...+100 = 5050

    def test_zero_and_negative(self):
        """Test with zero and negative numbers."""
        self.assertEqual(my_sum(0), 0)
        self.assertEqual(my_sum(-1), 0)
        self.assertEqual(my_sum(-10), 0)

    def test_type_error(self):
        """Test that TypeError is raised for non-integer inputs."""
        with self.assertRaises(TypeError):
            my_sum(5.5)
        with self.assertRaises(TypeError):
            my_sum("5")
        with self.assertRaises(TypeError):
            my_sum([5])
        with self.assertRaises(TypeError):
            my_sum(None)

    def test_large_numbers(self):
        """Test with large numbers."""
        self.assertEqual(my_sum(1000), 500500)
        self.assertEqual(my_sum(9999), 49995000)

    def test_edge_cases(self):
        """Test edge cases."""
        # Test with 1 (smallest valid positive input)
        self.assertEqual(my_sum(1), 1)
        
        # Test mathematical correctness with known values
        self.assertEqual(my_sum(3), 6)   # 1+2+3 = 6
        self.assertEqual(my_sum(4), 10)  # 1+2+3+4 = 10


if __name__ == '__main__':
    unittest.main()