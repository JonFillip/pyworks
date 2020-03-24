"""A class that can be used to represent a car"""


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
