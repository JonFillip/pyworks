"""This the model of an ice cream restaurant"""


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


class IceCreamStand(Restaurant):
    """Build a subclass of Restaurant that models an Ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes of the parent class. Then initialize the
        attributes specific to IceCreamStand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chunky monkey", "chocolate", "caramel"]

    def ice_cream_flavors(self):
        """Display the flavors of ice cream available"""
        print(f"Welcome to {self.name.title()}. These are the available "
              f"ice cream flavors:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")
