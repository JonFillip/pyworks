# The Python Standard Library
"""The Python Standard Library is a set of modules included with every python
installation. To use any functions or class in the standard library by including
 a simple import statement at the top of the file. For example, the python
 module, random, which can be useful for modelling many real world situations.

 One interesting function from the random module is randint(). This function
 takes two integer arguments and returns a randomly select between and including
 those numbers.
    Here's how to generate a random number between 1 to 10:
 """
from random import randint, choice

print(randint(1, 10))

"""Another useful function is choice(). This function take in a list or tuple
and returns a randomly chosen element"""

fortune_companies = ["gucci", "coca-cola", "apple", "microsoft", "amazon"]
first_company = choice(fortune_companies)
print(first_company)
