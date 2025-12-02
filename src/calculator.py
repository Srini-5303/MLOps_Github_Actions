# src/calculator.py
"""
Calculator module with basic arithmetic operations.
"""

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def combo(x, y):
    return add(x, y) + sub(x, y) + mul(x, y)

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulo by zero")
    return x % y