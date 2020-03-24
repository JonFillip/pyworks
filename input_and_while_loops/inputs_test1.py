"""
7-1. Rental car: Write a program that asks the user what kind of rental car they
would like to have. Print the message about the car.
"""
cars = ["chevy Volt", "tesla model 3", "toyota camry", "bmw m3", "mazda 6"]
wanted_car = input("What car would you like to rent? ")

if wanted_car not in cars:
    print(f"Sorry but {wanted_car.title()} is not available in our rental "
          f"service.")
else:
    print(f"\n{wanted_car.title()} is available to rent.")

"""
7-2. Restaurant. Write a program that asks the user how many people are in a 
dinner group. If the answer is more than eight, print a message saying they'll 
have to wait for a table. Otherwise, report that their table is ready.
"""
restaurant = input("How many people are in your dinner group? ")
restaurant = int(restaurant)
time = input("What time would be booking the table for? ")

if restaurant <= 8:
    print(f"You're booking a dinner table for {restaurant}. We'll have the"
          f" table ready by {time}.")
elif restaurant > 8:
    print(f"We apologise but we currently do not have a table available "
          f"for {restaurant}.")

"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
number is a multiple of 10 or not
"""
number = input("Tell me a number and I'll tell you if is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is indeed a multiple of 10")
else:
    print(f"The number {number} is not a multiple of 10")
