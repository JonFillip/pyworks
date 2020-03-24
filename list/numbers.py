"""
Numbers are often used in programming to keep scores in a game, represent data in visualizations, store information in
web applications and so on. In python numbers are stored in several different ways like: Integers & Floats. In this
script we'll be looking at simple arithmetic operations and how to used integers and floats
"""

# Integers and Arithmetic operations
# Integers are whole numbers like: 5, 3, 1000, 1736. They can be added (+), subtracted (-), multiplied (*) & divided (/)
a = 2 + 8
b = 25 * 1185
c = 5 - 6
d = 4/2

print(a, b, c, d)  # Multiple Assignment


"""
In a terminal session. Python simply returns the result of the operation. Python uses two multiplication symbols to 
represent exponents or raise to the power
"""
print(2**3)
print(100**5)

"""
Python also supports the order of operation too, so you can use multiple operations in one expression. You can also use
parentheses to modify the order of operations so python can evaluate the expression in the order you specified. E.g
"""
print(2 * 4 + 3)  # Will be different
# Result equals 11
print(2 * (4 + 3))
# Result equals 14

"""
The spacing in these examples has no effect on how python evaluates the expressions; it simply helps you more quickly 
spot the operations that have priority wen you're reading through code
"""
"""
Python calls any number with a decimal point a float. This term is used in most programming languages, and it refers to
the fact  that a decimal point can appear at any position in a number. Every programming language must be carefully 
designed to properly manage decimal numbers so numbers behave appropriately no matter where the decimal point appears
"""
# Floats and arithmetic operations
print(0.5 + 0.9)
print(2.3 - 0.66)
# Result equals 1.6399999997
print(9.8 * 0.8)
# Result equals 7.840000000000001
print(5.5 / 2.5)

# Be aware that you can sometimes get arbitrary number of decimal places in your answers like print(2.3 - 0.66)
# # Result equals 1.6399999997. This happens in all languages and is of little concern

# Integers and floats can also be used together
print(8 + 0.9)  # Equals 8.9
print(2 - 2.6)  # Equals -0.6000000000000001
print(2 ** 0.5)  # Equals 1.4142135623730951

# Note: If you use an integer with a float in any operation you'll get a float as well.

# Underscores in numbers
"""
When writing long numbers, you can group digits using underscores to make large numbers more readable. Python will 
ignore the underscore when printing or storing these values. Also regardless on how you group these values
1_000 is the same as 10_00 to python and it will print the value 1000. For example:
"""

earth_age = 4_500_000_000
print(earth_age)

# Multiple Assignment
"""
You can assign values to more than one variable using just one line. This can help shorten your programs and make them
easier to read; this technique is often used when initializing a set of numbers. For example:
"""
x, y, z = 10.5, 4.8, 6.0
print(x, y, z)

# CONSTANTS
"""
A constant is like a variable whose values stays the same throughout the life of a program. Python doesn't have built-in
constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant 
and never be changed:
"""
GRAVITY = 9.8


