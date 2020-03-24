"""
8-3. T-shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the t-shirt and the message printed on it.
    Call the function once using positional arguments to make a shirt. Call the
    function a second time using keyword arguments.
"""


def make_shirt(size, message):
    """Ask the user for their size & the text they want printed on the shirt"""
    print(f"\nT-shirt size: {size.upper()}")
    print(f"T-shirt text: {message.title()}")


make_shirt(input("What t-shirt size do you wear? "), input("Enter a message: "))
make_shirt(size="m", message="just do it")

"""
8-4. Large shirts: Modify the make_shirt() function so that shirts are large by 
default with a message that reads I love Python. Make a large shirt and a medium
shirt with the default message and a shirt of any size and a different message.
"""


def make_shirt(size="Large", message="I love Python"):
    """Ask the user for their size & the text they want printed on the shirt"""
    print(f"\nT-shirt size: {size.upper()}")
    print(f"T-shirt text: {message.title()}")


make_shirt(size="medium")
make_shirt()

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a
city and its country. The function should print a simple sentence. Give the 
parameter for the country a default value. Call your function for 3 different
cities, at one of which is not in the default country.
"""


def describe_city(city, country="United States"):
    """"Ask the user to enter the city & country they live in and display it"""
    print(f"\n{city.title()} is in {country.title()}.")


describe_city(city=input("Enter the city you currently live in: "),
              country=input("Enter the country you live in: "))
describe_city("Houston")
describe_city("Los Angeles")
