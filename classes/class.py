"""
Object Oriented Programming (OOP) is one of the most effective ways to writing
software. In OOP you write classes that represent real world things and
situations, and you create objects based on these classes.

Making an object from a class is known as instantiation, and you work with
instances of a class.
"""
# Creating and Using a Class
"""
Classes can be modelled after almost anything. For example,say we want to create
a class that describes a city, so we declare a class called Cities- not one city
in particular, but any city. We know all cities have a name, a residing country,
size and population. And a city has certain behaviours and characteristics like 
noise level, population density and size - large, small etc, pollution level and
crime rate etc. This class will tell Python how to make an object representing a 
city. After writing the class you can use it make individual instances, each of 
which representing one specific.  
Each instance created for City class will store the name, country and population
and I'll give each city certain behaviours.
"""


class Cities:
    """A simple attempt to model a city"""

    def __init__(self, name, country, population):
        """Initialize the name, country and population attributes"""
        self.name = name
        self.country = country
        self.population = population

    def noise(self):
        """Simulate the noise level of the city"""
        print(f"{self.name} is a very noisy city")

    def size(self):
        """Simulate the size of the city"""
        print(f"{self.name} is a big city in land area")


# To explain the process
"""
At line 24, I defined the class called City. By convention, capitalized names 
refers to classes in Python. There are no parentheses in the class definition 
because we are making the class from scratch. The class definition is then 
followed by a docstring describing what the class does.
"""

# The __init__() Method
"""
A function that's part of a class is a Method. The __init__() method at line 27,
is a special method that Python runs automatically whenever we create a new 
instance based on the defined class in our case City.

We define the __init__() method to have four parameters: self, name, country and 
population. The self parameter is required in the method definition, and it must
come first before any other parameters. It must be included in the definition 
because when Python calls the method later (to create instance of City), the 
method call will automatically pass the self argument. Every method call 
associated with an instance automatically passes  self, which is a reference to 
the instance itself; it gives the individual instance access to the attributes 
and methods in the class. We'll pass City() a name, country, and population as 
arguments; self is passed automatically, so we don't need to pass it. Whenever 
we make an instance from the City class, we'll provide values for only the last 
three parameters, name, country and population.

The three variables defined at lines 29, 30 and 31 each have the  prefix self.
Any variable prefixed with self is available to every method in the class and 
will also be accessible through any instance created from the class. The line 
self.name, self.country and self.population each take in the values associated 
with parameters name, country and population respectively. Variables that are 
accessible through instances are called Attributes.

The City class has two other methods defined: noise() and size() at lines 33 and 
37. Because these methods don't need additional information to run, we just 
define them to have one parameter, self. The instances we create later will have 
access to these methods. In other words we'll be able to simulate a noisy and 
large city area. For now noise() and size() don't do much, they simply print the
message saying the city is noisy and the city is large.
"""


# Making Instances from a Class


class City:
    """A simple attempt to model a city"""

    def __init__(self, name, country, population):
        """Initialize the name, country and population attributes"""
        self.name = name
        self.country = country
        self.population = population

    def noise(self):
        """Simulate the noise level of the city"""
        print(f"{self.name} is a very noisy city")

    def size(self):
        """Simulate the size of the city"""
        print(f"With a population of {self.population}, "
              f"this is a big city in land area")


my_city = City("kiev", country="", population=3000000)
print(f"My city is {my_city.name.title()} and has a population "
      f"of {my_city.population}")

"""
In line 105 we tell Python to create a city with the name 'kiev' and population 
of 3,000,000. When python reads this line, it calls the __init__() method in 
City with arguments 'kiev' and 3000000. The __init__() method creates instances
representing this particular city and sets the name, country & population attri-
butes using the value we provided. Python then returns an instance representing 
this city. We assign that instance to the variable my_city. The naming 
convention is here; we can usually refer that the capitalised name like City is 
the class, and the lowercase name like my_city refers to a single instance 
created from a class.
"""

# Accessing Attributes
"""
To access the attributes of an instance, you use dot notations. In line 106 we 
access the value of my_city's attributes name by writing:

            my_city.name
"""

# Calling Methods
"""
After we create an instance from the class City, we can use dot notation to call
any method defined in City. Let's make simulate our city's noise and size
"""


class City:
    """A simple attempt to model a city"""

    def __init__(self, name, country, population):
        """Initialize the name, country and population attributes"""
        self.name = name
        self.country = country
        self.population = population

    def noise(self):
        """Simulate the noise level of the city"""
        print(f"{self.name.title()} is a very noisy city")

    def size(self):
        """Simulate the size of the city"""
        print(f"With a population of {self.population}, "
              f"{self.name.title()} is a big city in land area")


my_city = City('lagos', 'nigeria', '16000000')
my_city.noise()
my_city.size()

"""
To call a method, give the name of the instance (in this case, my_city) and the 
method you want to call, separated by a dot. When python reads my_city.noise(), 
it looks for the method noise() in the class City and runs that code. Python
interprets the line my_city.size() the same way.
"""

# Creating Multiple Instances
"""
We can create as many instances from a class as you need. Let's create a second
city called your_city
"""


class City:
    """A simple attempt to model a city"""

    def __init__(self, name, country, population):
        """Initialize the name, country and population attributes"""
        self.name = name
        self.country = country
        self.population = population

    def noise(self):
        """Simulate the noise level of the city"""
        print(f"{self.name.title()} is a very noisy city")

    def size(self):
        """Simulate the size of the city"""
        print(f"With a population of {self.population}, "
              f"{self.name.title()} is a big city in land area")


my_city = City('tokyo', 'japan', 16000000)
your_city = City('moscow', 'russia', 12615000)

print(f"\n{my_city.name.title()} is a city in {my_city.country} and has a "
      f"population of {my_city.population}")
my_city.noise()

print(f"\n{your_city.name.title()} is a city {your_city.country} and has a "
      f"population of {your_city.population} living in it")
your_city.noise()

# Working with Classes and Instances
"""
Once you write a class, you'll spend most of the time working with instances 
created from that class. One of the first tasks you'll want to do is modify the
attributes associated with a particular instances. You can modify the attributes
of an instances directly or write methods that updates attributes in specific
ways. For example, consider a class that describes a robot:
"""


class Robot:
    """Model that describes a farm robot"""

    def __init__(self, name, model, purpose):
        """Initialize the attributes to describe the robot"""
        self.name = name
        self.model = model
        self.purpose = purpose

    def harvest(self):
        """Simulate the robot arm to harvest crop or signal when the crop
        is ready for harvest."""
        print(f"{self.name.title()} scanning plant 022646 in row 69, aisle 5.")

    def booting(self):
        """Simulate the booting of the robot"""
        full_name = f"{self.name} {self.model}"
        print(f"{full_name.title()}\n{self.purpose}.....loading")


robot_at_work = Robot("Ominis", "mars-1000", "crop growth monitoring")
print(f"\n{robot_at_work.name.title()} {robot_at_work.model.title()} is the "
      f"next generation in house crop growth monitoring system.")
robot_at_work.harvest()
robot_at_work.booting()

# Setting a Default Value for an Attribute
"""
When an instance is created, attributes can be defined without being passed in 
as parameters. These attributes can be defined in the __init__() method, where
they are assigned a default value.

For example,let's add an attribute called speedometer_reading that always starts
with a value of 0. We'll also add a method read_speedometer() that helps us read
each car's speedometer:
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
        full_name = f"{self.name} {self.model} {self.power}"
        return full_name.title()

    def read_speedometer(self):
        """Display a message that shows the vehicle's current speed"""
        print(
            f"{self.model.title()} is driving at a pace of "
            f"{self.speedometer_reading}km/hr")


automobile = Vehicle("bugatti", "chiron", "1500")
print(automobile.get_formatted_name())
automobile.read_speedometer()

# Modifying Attribute Values
"""
There are 3 major ways to change the value of an attribute: By changing the 
value directly, set the value through a method, or increment the value through a
method.

We'll use our Vehicle class as an example to demonstrate all the various methods
for modifying the attribute value.
"""

# Modifying the Attribute's Value directly
"""In this method we are going to alter the speedometer_reading's value from 
0 to 320 """


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
        full_name = f"\n{self.name} {self.model} {self.power}"
        return full_name.title()

    def read_speedometer(self):
        """Display a message that shows the vehicle's current speed"""
        print(
            f"The {self.model.title()} is driving at a pace of "
            f"{self.speedometer_reading}km/hr")


car = Vehicle("lotus", "evija", 2000)
print(car.get_formatted_name())
car.speedometer_reading = 320
car.read_speedometer()

# Modifying an Attribute's Value Through a Method
"""
It can be helpful to have the methods that update certain attributes for you. 
Instead of accessing the attribute directly, you pass the new value to a method
that handles the updating internally. For example adding a method called 
update_speedometer:
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
        full_name = f"\n{self.name} {self.model} {self.power}"
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
        if speed <= 200:
            self.speedometer_reading = speed
        else:
            print("Vehicle cannot go above 200km/hr on the highway")


automobile = Vehicle("mclaren", "gt", 720)
print(automobile.get_formatted_name())
automobile.update_speedometer(155)
automobile.read_speedometer()

# Incrementing an Attribute's Value Through a Method
"""
At times you might want to increment an attribute's value by a certain amount 
rather than set an entirely new value. For example, let's consider that the 
vehicle that is being used and has put on millage from the time we first bought
it till now. Here's a method that allows us to pass the incremental amount and 
that value to the odometer reading attribute:
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


race_car = Vehicle("mercedes", "gtr pro", 670)
print(race_car.get_formatted_name())

race_car.update_speedometer(210)
race_car.read_speedometer()

race_car.increment_speedometer(50)
race_car.read_speedometer()


