"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 or 9-4. Either version of the class will work; just pick the one
you better. Add an attribute called flavors that stores a list of ice cream
flavors. Write a method that displays these flavors. Create an instance of
IceCreamStand, and call this method.
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


my_desert = IceCreamStand("Mr Pops", "desert")
my_desert.describe_restaurant()
my_desert.ice_cream_flavors()

"""
9-7. Admin: An administrator is a special kind of user. Write a class 
called Admin that inherits from the User class in Exercise 9-3 or 9-5. Add an 
attribute , privileges, that stores a list of strings like 'can delete post', 
'can add post', 'can ban user', and so on. Write a method called 
show_privilege() that lists the admins set of privileges. Create an instance of
Admin, call your method.

9-8. Privileges: Write a separate Privilege class. The class should have one 
attribute, privileges, that stores a list of strings as described in Exercise 
9-7. Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
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


class Privileges:
    """Write code that defines attributes amd methods for admin privileges."""

    def __init__(self, privileges):
        """Initialize the attribute for Privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the Admin user"""
        print(f"Admin features:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    """Build a child class from User and represent aspects of the User that
    are specific to the Administrator."""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize the attributes of the parent class. Then add the new
        attributes specific to Admin"""
        super().__init__(first_name, last_name, age, location, occupation)
        self.privilege = Privileges(privileges=[
            "add post",
            "delete post",
            "ban user",
            "edit account settings",
        ])


admin = Admin("john", "phillip", 22, "kiev", "product owner")
admin.privilege.show_privileges()

"""
9-9. Battery upgrade: Use the final version of ElectricVehicle. Create a class
called Battery and add a method called upgrade_battery(). This method should
check the battery size and set the capacity to 100 if it isn't already. Make an 
electric car with a default battery capacity, call get_range() once, and then
call get_range() a second time after upgrading the battery. You should see an
increase
"""


class Vehicle:
    """Build a description of a vehicle's name, model, horsepower,
    current_speed """

    def __init__(self, brand, model, horsepower):
        """Initialize the attributes and add a default attribute"""
        self.name = brand
        self.model = model
        self.power = horsepower
        self.speedometer_reading = 0

    def get_formatted_name(self):
        """Return neatly formatted full descriptive name of the vehicle"""
        full_name = f"\n{self.name} {self.model} {self.power}hp"
        return full_name.title()

    def read_speedometer(self):
        """Display a message that shows the vehicle's current speed"""
        print(
            f"{self.model.title()} is driving at a pace of "
            f"{self.speedometer_reading}km/hr")

    def update_speedometer(self, speed):
        """
        Set the speedometer to read any given value.
        Set a speed limiter of 200km/hr
        """
        if speed <= 300:
            self.speedometer_reading = speed
        else:
            print("Vehicle cannot go above 200km/hr on the highway")

    def increment_speedometer(self, velocity):
        """Add the given amount to the odometer reading."""
        self.speedometer_reading += velocity


class Battery:
    """Model a battery for an electric car and create new methods."""

    def __init__(self, battery_capacity=100):
        """Initialize the battery's attributes"""
        self.battery_capacity = battery_capacity
        self.drive_range = 0

    def describe_battery(self):
        """Print a statement describing the battery capacity."""
        print(f"This car has a {self.battery_capacity}-KWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_capacity == 100:
            self.drive_range = 270
        elif self.battery_capacity > 100:
            self.drive_range = 310

        print(f"The drive range for this car is about {self.drive_range}.")

    def upgrade_battery(self, battery_improvement):
        """Upgrade the battery capacity of the EV"""
        self.battery_capacity += battery_improvement


class ElectricVehicle(Vehicle):
    """Represent the aspects of the vehicle, specific to an EV."""

    def __init__(self, brand, model, horsepower):
        """Initialize the attributes of the parent class.
        Then add the new attribute specific to EVs
        """
        super().__init__(brand, model, horsepower)
        self.battery = Battery()


my_ev = ElectricVehicle("rimac", "concept 2", 1900)
print(my_ev.get_formatted_name())

my_ev.battery.get_range()
my_ev.battery.describe_battery()
my_ev.battery.upgrade_battery(15)
my_ev.battery.get_range()
my_ev.battery.describe_battery()
