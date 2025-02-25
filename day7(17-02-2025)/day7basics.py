# 17-02-2025

print("Hello")

# Unit Testing

import unittest
import calc as c

# Unit test class
class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(c.add(3, 5), 8)
        self.assertEqual(c.add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(c.subtract(10, 5), -5)
        self.assertEqual(c.subtract(0, 5), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            c.divide(10, 0)

# Run the tests
if __name__ == "__main__":
    unittest.main()
