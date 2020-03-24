"""This is a simple model of a user database and admin console"""


class User:
    """Model of a user database, simulating a user profile"""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize the parameters above."""
        self.first_name = first_name
        self.surname = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        """Display the summary of the user's information"""
        print(f"\nUser name: {self.first_name.title()} {self.surname.title()}")
        print(f"Age: {self.age}\nLocation: {self.location.title()}"
              f"\nOccupation: {self.occupation.title()}")

    def greet_user(self):
        """Display a greeting to the user"""
        print(f"Hi {self.first_name.title()}! Welcome to the iCloud.")

    def sign_in_attempt(self):
        """Display the amount of times the user attempts to log in into their
        account"""
        print(f"User has logged in to account {self.login_attempts} times")

    def increment_login_attempts(self, attempt):
        """Create a function that automatically increases the login attempts
        by 1."""
        if attempt >= self.login_attempts:
            self.login_attempts += attempt

    def reset_login_attempts(self):
        """This function resets the login attempts to 0."""
        self.login_attempts -= self.login_attempts
