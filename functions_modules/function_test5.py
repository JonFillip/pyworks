"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the
sandwich that's being ordered. Call the function three times, using a different
number of arguments each time.
"""


def make_sandwich(*fillings):
    """Print the filling of the sandwich the user requests"""
    print("\nThis is the ingredients in the sandwich:")
    for item in fillings:
        print(f"- {item.title()}")


make_sandwich("lettuce", "tomatoes", "bacon", "cheddar cheese")
make_sandwich("beef", "lettuce", "mayo", "eggs")
make_sandwich("sausages", "scrambled eggs", "bbq sauce", "lettuce")

"""
8-13. User Profile: Start with a copy of user_profile from the previous exercise
. Build a profile of yourself by calling build_profile(), using your first and 
last names and three other key-value pairs that describes you.
"""


def user_database(name, surname, **user_info):
    """Build a dictionary containing everything we know about yourself"""
    user_info['first_name'] = name
    user_info['last_name'] = surname
    return user_info


user_profile = user_database("john", "phillip", age=22, height=183,
                             location="ukraine")
for key, value in user_profile.items():
    print(f"{key.title()}: {value}")

"""
8-14. Cars: Write a function that stores information about the car in a diction
-ary. The function should always receive a manufacturer and a model name. It 
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs.
"""


def build_car(brand, model, **car_info):
    """Build a dictionary of the details of a car and display it"""
    car_info['manufacturer'] = brand
    car_info['model'] = model
    return car_info


automobile = build_car('bugatti', 'chiron', power=1500, acceleration_60=2.5)
for key, value in automobile.items():
    print(f"{key.title()}: {value}")
