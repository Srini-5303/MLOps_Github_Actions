# test/test_calculator_unittest.py
"""
Unittest tests for calculator module.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import add, sub, mul, combo, divide, power, modulo

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)
    
    def test_sub(self):
        """Test subtraction function."""
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-3, -5), 2)
        self.assertEqual(sub(100, 50), 50)
    
    def test_mul(self):
        """Test multiplication function."""
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 100), 0)
        self.assertEqual(mul(7, 8), 56)
    
    def test_combo(self):
        """Test combined function."""
        self.assertEqual(combo(2, 3), 10)
        self.assertEqual(combo(5, 2), 20)
        self.assertEqual(combo(0, 0), 0)
    
    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5)
        
        # Test division by zero
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertTrue("Cannot divide by zero" in str(context.exception))
    
    def test_power(self):
        """Test power function."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertAlmostEqual(power(3, -1), 1/3)
        self.assertEqual(power(10, 2), 100)
    
    def test_modulo(self):
        """Test modulo function."""
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 5), 0)
        self.assertEqual(modulo(7, 4), 3)
        
        # Test modulo by zero
        with self.assertRaises(ValueError) as context:
            modulo(10, 0)
        self.assertTrue("Cannot perform modulo by zero" in str(context.exception))
    
    def test_edge_cases(self):
        """Test edge cases."""
        # Test with large numbers
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(mul(1000, 1000), 1000000)
        
        # Test with negative numbers
        self.assertEqual(sub(-10, -5), -5)
        self.assertEqual(mul(-5, -5), 25)
        
        # Test with floats
        self.assertAlmostEqual(divide(1, 3), 0.3333333, places=6)
        self.assertEqual(power(2.5, 2), 6.25)

if __name__ == '__main__':
    unittest.main()