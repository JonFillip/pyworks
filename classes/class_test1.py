"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for the
class should store two attributes: a restaurant_name and cuisine_type. Make a
method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the
restaurant is open.
    Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.

9-2. Three Restaurants: Create three different instances from the class, and
call describe_restaurant for each instance
"""


class Restaurant:
    """Model of a restaurant and its description"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine_type attributes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Displays a description of the restaurant"""
        print(f"{self.name.title()} is a {self.cuisine} restaurant")

    def open_restaurant(self):
        """Displays a message indicating the restaurant is open"""
        print(f"{self.name.title()} opens at 9.a.m")


my_restaurant = Restaurant("sushiya", "asian")
your_restaurant = Restaurant("grille de brazil", "steakhouse")
the_restaurant = Restaurant("Beef et Vino", "steakhouse")

print(f"\n{my_restaurant.name.title()} is a restaurant that specializes "
      f"in {my_restaurant.cuisine} cuisines")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"\n{your_restaurant.name.title()} is a uptown {your_restaurant.cuisine}"
      f"that specializes in meat dishes and fine wines.")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

print(f"\n{the_restaurant.name.title()} is a 4 star {the_restaurant.cuisine} "
      f"restaurant that serves exquisite meat dishes and fine wines")
the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()

"""
9-3. Users: Make a class called User. Create two attributes called first_name &
last_name, and then create several other attributes that are typically stored in 
a user profile. Make a method called describe_user() that prints a summary of 
the user's information. Make another method called greet_user() that prints a 
personalized greeting to the user.
    Create several instances representing different users, and call both methods
for each user
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

    def describe_user(self):
        """Display the summary of the user's information"""
        print(f"\nUser name: {self.first_name.title()} {self.surname.title()}")
        print(f"Age: {self.age}\nLocation: {self.location.title()}"
              f"\nOccupation: {self.occupation.title()}")

    def greet_user(self):
        """Display a greeting to the user"""
        print(f"Hi {self.first_name.title()}! Welcome to the Apple theatre.")


user_profile = User("john", "phillip", 22, "kiev", "software engineer")
user_profile1 = User("lyubov", "steblina", 23, "kiev", "UX designer")

full_name = f"{user_profile.first_name} {user_profile.surname}"
full_name1 = f"{user_profile1.first_name} {user_profile1.surname}"

print(f"\n{full_name.title()} is a {user_profile.age} year old "
      f"{user_profile.occupation} living in {user_profile.location.title()}")
user_profile.describe_user()
user_profile.greet_user()

print(f"\n{full_name1.title()} is a {user_profile1.age} year old "
      f"{user_profile1.occupation} living in {user_profile1.location.title()}")
user_profile1.describe_user()
user_profile1.greet_user()
