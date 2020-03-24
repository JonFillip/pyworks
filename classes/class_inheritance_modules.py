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


race_car = Vehicle("mercedes", "gtr pro", 670)
print(race_car.get_formatted_name())

race_car.update_speedometer(210)
race_car.read_speedometer()

race_car.increment_speedometer(50)
race_car.read_speedometer()

# Inheritance
"""
You don't always to write a class from scratch. If the class you're writing is a
specialized version of another class you wrote, you can use inheritance. When 
one class inherits from another, it takes on the attributes and methods of the 
first class. The original class is called the parent class, and the new class is
the child class. The child class can inherit any or all the attributes and 
methods of its parent class, and is also free to define new attributes and 
methods of its own. 
"""

# The __init__() Method for a child class
"""
When writing a new class based on an existing class, it is often necessary to 
call the __init__() method of the parent class. This will initialize the any 
attributes that were defined in the parent __init__() method to make them 
available in the child class.
    For example, let's consider the Vehicle class, supposing we want to model an
ElectricVehicle class from the our Vehicle class (the parent class which is 
written above): 
"""


class ElectricVehicle(Vehicle):
    """Represent the aspects of the vehicle, specific to an EV."""

    def __init__(self, brand, model, horsepower):
        """Initialize the attributes of the parent class."""
        super().__init__(brand, model, horsepower)


my_ev = ElectricVehicle("rivian", "r1s", 780)
print(my_ev.get_formatted_name())

"""
N.B: 
    1. When creating a subclass make sure the parent class is in the same file
as the subclass and must appear before the subclass in the file.
    2. The super() function at line 435 is a special function that allows you to
call a method from the parent class. The line tells Python to call the 
__init__() method from the parent class (in this case Vehicle) which gives an 
ElectricVehicle (subclass) instance all the attributes defined in that method.
The name super comes from a convention of calling the parent class a superclass
and the child class subclass
"""

# Defining Attributes and Methods for the Child Class
"""
When a child class has inherited the attributes and methods of its parent class,
you can add any new attributes and methods necessary to differentiate the child
class from the parent class. 
    For example, let's add a new attribute that's specific to electric vehicles
(battery capacity) and a method that reports on this attributes. We'll store the
battery size and write a method that prints a description of the battery:
"""


class ElectricVehicle(Vehicle):
    """Represent the aspects of the vehicle, specific to an EV."""

    def __init__(self, brand, model, horsepower):
        """Initialize the attributes of the parent class.
        Then add the new attribute specific to EVs
        """
        super().__init__(brand, model, horsepower)
        self.battery_capacity = 80

    def describe_battery(self):
        """Print a statement describing the battery capacity."""
        print(f"This car has a {self.battery_capacity}-KWh battery")


my_porsche = ElectricVehicle("porsche", "taycan turbo s", 750)
print(my_porsche.get_formatted_name())
my_porsche.describe_battery()

# Overriding Methods from the Parent Class
"""
To override any method from the parent class that doesn't fit what you're trying
to model with the child class, you first define a method in the child class with 
the same name as the method you want to override in the parent class. Python
will disregard the parent class method and only pay attention to the method you
define in the child class 
"""

# Instances as Attributes
"""
When modelling something from the real world in code, you may find that you're 
adding more and more detail to a class. You'll find that you have a growing list 
of attributes and methods and that your files are becoming lengthy. In these 
situations, you might recognize that part of one class can be written in a 
separate class. And then break down your large class into smaller classes that
work together.
    For example, if we continue adding detail to the AfricanCity class, we might
notice that we are adding many attributes and methods specific to the city's 
population. When we see this happening, we can stop and move those attributes & 
methods to a separate class called People. Then use a People instance as an 
attribute in the AfricanCity class:
"""


class Cities:
    """A simple attempt to model a city"""

    def __init__(self, name, country, land_mass):
        """Initialize the name, country and population attributes"""
        self.name = name
        self.country = country
        self.size = land_mass

    def get_formatted_description(self):
        """Return a neatly formatted description of the city"""
        about_city = f"{self.name}, {self.country}\nLand mass: {self.size} km2."
        return about_city.title()

    def noise(self):
        """Simulate the noise level of the city"""
        print(f"{self.name} is a very noisy city")

    def area(self):
        """Simulate the size of the city"""
        print(f"{self.name} is a big city in land area")


class People:
    """ Write code that defines attributes and methods for the population."""

    def __init__(self, population, size):
        """Initiate the population attribute"""
        self.population = population
        self.land_area = size

    def describe_population(self):
        """Print a statement describing the population size"""
        print(f"The city has a population of {self.population} people.")

    def population_density(self):
        """Calculate and print the population density"""
        density = self.population / self.land_area
        print(f"The population density is {density} people per km2")


class AfricanCity(Cities):
    """Build a subclass of Cities and represent aspect of a city that are
    specific to population """

    def __init__(self, name, country, land_mass):
        """Initialize the attributes of the parent class
         Then initialize attributes specific to AfricanCity"""
        super().__init__(name, country, land_mass)
        self.people = People(18000000, 1172)


ecowas = AfricanCity("lagos", "nigeria", 1172)
print(ecowas.get_formatted_description())
ecowas.people.describe_population()
ecowas.people.population_density()
