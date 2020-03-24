"""A class that can be used to represent a mechanized in-house farm."""


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
