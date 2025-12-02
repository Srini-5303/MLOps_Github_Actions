# test/test_calculator_pytest.py
"""
Pytest tests for calculator module.
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import add, sub, mul, combo, divide, power, modulo

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(100, 200) == 300

def test_sub():
    """Test subtraction function."""
    assert sub(5, 3) == 2
    assert sub(0, 5) == -5
    assert sub(-3, -5) == 2
    assert sub(100, 50) == 50

def test_mul():
    """Test multiplication function."""
    assert mul(2, 3) == 6
    assert mul(-2, 3) == -6
    assert mul(0, 100) == 0
    assert mul(7, 8) == 56

def test_combo():
    """Test combined function."""
    assert combo(2, 3) == 10 
    assert combo(5, 2) == 20  
    assert combo(0, 0) == 0

def test_divide():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(-10, 2) == -5
    
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_power():
    """Test power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, -1) == 1/3
    assert power(10, 2) == 100

def test_modulo():
    """Test modulo function."""
    assert modulo(10, 3) == 1
    assert modulo(20, 5) == 0
    assert modulo(7, 4) == 3
    
    with pytest.raises(ValueError, match="Cannot perform modulo by zero"):
        modulo(10, 0)

# Parametrized tests for more comprehensive testing
@pytest.mark.parametrize("x,y,expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, -1, -2),
    (100, -100, 0),
])
def test_fun1_parametrized(x, y, expected):
    """Parametrized test for addition."""
    assert add(x, y) == expected

@pytest.mark.parametrize("x,y,expected", [
    (10, 5, 2),
    (9, 3, 3),
    (20, 4, 5),
    (100, 10, 10),
])
def test_divide_parametrized(x, y, expected):
    """Parametrized test for division."""
    assert divide(x, y) == expected