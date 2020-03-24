import unittest
from testing_code.employee_class import Employee


class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """Create a database of employees with their first and last names as
        well as their annual salaries """
        self.john = Employee('john', 'phillip', 180554)

    def test_give_default_raise(self):
        """Test the give_raise() method with the default raise value works
        properly"""
        self.john.give_raise()
        self.assertEqual(self.john.annual_salary, 185554)

    def test_give_custom_raise(self):
        """Test the give_raise method with a custom raise value of $10000 to
        make sure the method works properly """
        self.john.give_raise(amount=10000)
        self.assertEqual(self.john.annual_salary, 190554)

