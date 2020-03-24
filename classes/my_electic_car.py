# Importing class from Multiple classes stored in a Module
"""from classes.car import ElectricVehicle"""
# Importing Multiple Classes from a Module
from classes.car import Vehicle, ElectricVehicle

zero_carbon = ElectricVehicle("porsche", "taycan turbo s", 800)
print(zero_carbon.get_formatted_name())
zero_carbon.describe_battery()

gas_car = Vehicle("porsche", "panamera", 650)
print(gas_car.get_formatted_name())
gas_car.read_speedometer()
