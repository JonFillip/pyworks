"""
9-4. Numbered Served: Start with your program from Ex 9-1. Add an attribute
called number_served with a default value of 0. Create an instance called
restaurant from this class. Print the number of customers the restaurant has
served, and then change this value and print it again.
    Add a method called set_number_served() that lets you set the number of \
customers that have been served. Call this method with a new number and print
the value again.
    Add a method called increment_number_served() that lets you increment that
number of customers who've been served. Call this method with any number you
like that could represent how many customers were served in, say, a day of
business.
"""


class Restaurant:
    """Model of a restaurant and its description"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine_type attributes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Displays a description of the restaurant"""
        print(f"{self.name.title()} is a {self.cuisine} restaurant")

    def open_restaurant(self):
        """Displays a message indicating the restaurant is open"""
        print(f"{self.name.title()} opens at 9.a.m")

    def restaurant(self):
        """Print the number of customer in the restaurant"""
        print(f"There are {self.number_served} customers in the restaurant")

    def set_number_served(self, customers):
        """Set the number of customers served and make sure the number cannot
        be rolled back"""
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("Customer tally cannot be rolled back.")

    def increment_number_served(self, served):
        """Adds a given amount to the current customer served."""
        self.number_served += served


eatery = Restaurant("the burger", "fast food")
eatery.describe_restaurant()
eatery.open_restaurant()

eatery.set_number_served(20)
eatery.restaurant()

eatery.increment_number_served(3)
eatery.restaurant()

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class 
from from Ex.9-3. Write method called increment_login_attempts() that increments
the value of login_attempts by 1. Write another method called reset_login_
attempts() that resets the value of login_attempts to 0.
    Make an instance of the User class and call increment_login_attempts() 
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts(). Print 
login_attempts again to make sure it was reset to 0.
"""


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


login = User("john", "phillip", 22, "kiev", "software developer")
login.describe_user()

login.increment_login_attempts(1)
login.sign_in_attempt()

login.increment_login_attempts(3)
login.sign_in_attempt()

login.reset_login_attempts()
login.sign_in_attempt()

