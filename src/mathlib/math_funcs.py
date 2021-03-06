from math import log


"""
ADDITION
brief: Sum of x and y
param: float x, float y
return: x + y
"""
def add(x, y):
    return x + y


"""
SUBTRACTION
brief: Difference of x and y
param: float x, float y
return: x - y
"""
def sub(x, y):
    return x - y


"""
MULTIPLICATION
brief: Multiplication of x and y
param: float x, float y
return: x * y
"""
def mul(x, y):
    return x * y


"""
DIVISION
brief: Division of x and y
param: float x, float y
return: x / y
"""
def div(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        print("Division by zero")
        return False
    return res


"""
FACTORIAL
brief: Factorial of n, n must be a non-negative integer
param: int n
return: n!
"""
def factorial(n):
    if n < 0 or type(n) is not int:
        print("Invalid parameter")
        return False
    res = 1
    for i in range(n):
        res *= i + 1
    return res 


"""
POWER WITH n >= 0
brief: Number x raised to the power of n
param: float x, int n
return: x^n
"""
def pow_n(x, n):
    if n < 0 or type(n) is not int:
        print("Exponent is not a natural number")
        return False
    return x ** n


"""
NTH ROOT
brief: Nth root of number x
param: float x, float n
return: x^(1/n)
"""
def nth_root(x, n):
    if x < 0 and n % 2 == 0:
        print("Invalid parameter")
        return False
    if n <= 0:
        print("Negative exponent") 
        return False
    return x ** (1 / n)


"""
LOGARITHM
brief: Logarithm of x with base b
param: float x, float b
return: float log(x, b)
"""
def logx(x, b):
    try:
        res = log(x, b)
    except ValueError:
        print("Invalid parameters")
        return False
    except ZeroDivisionError:
        print("Invalid parameters")
        return False
    return res