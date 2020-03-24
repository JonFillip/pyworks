import unittest
from testing_code.survey_class import AnonymousSurvey

# Testing a Class
"""
A variety of Assert Methods

    Python provides a variety of assert methods in the unittest.TestCase
class. assert methods test whether a condition you believe in is True at
a specific point in your code is indeed true. If the condition is true as
expected, your assumption about how that part of the program behaves is
confirmed; one can then be confident that no errors exist. If the condition you
assume is true and is actually not true, Python raises an exception.

    There are 6 commonly used assert methods. With these methods one can verify
that the returned values equal or don't have equal expected values, that values
are True of False, and that values are in or not in a given list. One can use
these methods only in a class that inherits the unittest.TestCase. The 6
commonly used assert methods are:

    Method                      Use
assertEqual(a, b)           Verify that a == b
assertNotEqual(a, b)        Verify that a != b
assertTrue(x)               Verify that x is True
assertFalse(x)              Verify that x is False
assertIn(item, list)        Verify that item is in list
assertNotIn(item, list)     Verify that item is not in list
"""

# Testing the AnonymousSurvey class
"""
I'll test one aspect AnonymousSurvey class behaviour. The test will verify a 
single response to the survey question is stored properly. We'll use the 
assertIn() method to verify that the response is in the list of responses after
it's been stored:
"""


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What was the first programming language you learned?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('python')
        self.assertIn('python', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three responses can be stored properly."""
        question = "What was the first programming language you learned?"
        my_survey = AnonymousSurvey(question)
        responses = ['python', 'java', 'javascript']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == "__main__":
    unittest.main()
