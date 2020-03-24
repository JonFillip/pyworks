import unittest
from testing_code.city_function import city_location


class CityTestCase(unittest.TestCase):
    """Test case for 'city_function.py'."""

    def test_city_country(self):
        """Test instances with just city and country names given."""
        formatted_location = city_location("lagos", "nigeria")
        self.assertEqual(formatted_location, "Lagos, Nigeria.")

    def test_city_country_population(self):
        """Test instances when city, country and populations values are
        given. """
        formatted_location = city_location("lagos", "nigeria",
                                           population=16000000)
        self.assertEqual(formatted_location, "Lagos, Nigeria - Population "
                                             "16000000.")


if __name__ == '__main__':
    unittest.main()
