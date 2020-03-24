import unittest
from testing_code.survey_class import AnonymousSurvey

"""
In 'testing_class.py' I created a new instance of AnonymousSurvey in each test
method, and I created new responses in each method. The unittest.TestCase class 
has a setup() method that allows me to create these objects once and then use 
them in each of my test methods. When one includes a setup() method in a 
TestCase class, Python runs the setup() method before running each method 
starting with test_. Any object created in the setup() method are then available
in each test method you write.
    For instance, I'll use setup() to create a survey instance and set of 
responses that can be used in test_store_single() and 
test_store_multiple_responses():
"""


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods"""
        question = "What was the first programming language you learned?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['python', 'c', 'c++', 'java', 'javascript', 'swift']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[1])
        self.assertIn('c', self.my_survey.responses)

    def test_store_multiple_responses(self):
        """Test that three responses can be stored properly."""

        for response in self.responses[1: 4]:
            self.my_survey.store_response(response)
        for response in self.responses[1: 4]:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
