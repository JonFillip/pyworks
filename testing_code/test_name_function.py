import unittest
from testing_code.testing_function import get_fullname

# N.B:
# Unit Tests and Test Cases
"""
The module unittest from the  Python Standard Library provides the tools for 
testing code. A 'unit test' verifies that one specific aspect of a function's 
behavior is correct. 
    A 'test case' is a collection of unit tests that together prove that a 
function behaves as it's supposed to, within the full range of situations you 
expect it to handle. A good test case considers all the possible kinds of input
a function could receive and includes tests to represent each of these 
situations.
"""

# A Passing Test
"""
To write a test case for a function, first import the unittest module and then
import the function you want to test. Then create a class that inherits from the 
unittest.TestCase, and write a series of methods to test different aspects of 
your function's behaviour.
    For example, creating a test case with one method that tests the function 
get_fullname() works correctly when given a first and last name:
"""


class NameTestCase(unittest.TestCase):
    """Tests for 'testing_function.py'."""

    def test_first_last_name(self):
        """Test name inputs like 'John Spacey' work"""
        formatted_name = get_fullname("john", "spacey")
        self.assertEqual(formatted_name, "John Spacey")

    def test_first_last_middle_name(self):
        """Test if inputs in middle names work. Like John Fred Kennedy"""
        formatted_name = get_fullname('john', 'fred', 'kennedy')
        self.assertEqual(formatted_name, "John Kennedy Fred")


if __name__ == '__main__':
    unittest.main()
