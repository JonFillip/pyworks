"""
A dictionary in python is a collection of key-value pairs. Each key is connected
to a value, and can be used to access a value associated with that key. A key's
value can be number, a string, a list, or even another dictionary. In fact you
can use any object that you can create in python as a value in a dictionary.

In python, a dictionary is wrapped in braces, {}, with a series of key value
pairs inside the braces. For example:
"""
bit_vader = {"color": "green", "health": 200}

"""
A key-value pair is a set of values associated with each other. When you provide
a key, python returns the value associated with that key. Every key is connected
to its value by a colon & individual key-value pairs are separated by a commas.
You can store as many key-value pairs as you want in a dictionary. The example
above, the dictionary variable stores two pieces of information about bit_vader,
namely the vader's color and its health. The strings 'color' and 'health' are 
the keys in the dictionary, and its associated value are 'green' and 200.
"""
# Accessing Values in a Dictionary
"""
To get access to a value in a dictionary, give the name of the dictionary and 
then place the key value inside a set of square brackets []:
"""
user = {"name": "John", "age": 22, "ethnicity": "African"}
print(user["age"])  # This returns the value associated with the key "age" - 22
# To  use the value in a message to output a request to a user
race = user["ethnicity"]
print(f"Candidate is of {race} descent.")

# Adding New Key Value Pairs
"""
Dictionaries are dynamic structures, and are mutable, meaning one can add and 
remove key-value pairs to a dictionary at any time. To add a new key 
value pair, you would give the name of the dictionary followed by the new key in
square brackets [] along with the new value.

For example, adding three new data points to the user dictionary:country,surname
, email.
"""
user["country"] = "Ukraine"
user["surname"] = "Phillip"
user["email"] = "jonathan@gmail.com"
print(user)

# Starting with an Empty Dictionary
"""
It's sometimes beneficial to start an empty dictionary and then add each new 
item to it. To start filling an empty dictionary, first define the name of the 
dictionary then, open an empty braces/ curly bracket{}, and then add each key-
value pair on its own line. 

Typically, you'll use the empty dictionaries when storing user-supplied data in 
a dictionary or when you write code that auto generates a large number of key 
value pairs automatically. For example, making a student database. 
"""
student = {}
student["first name"] = "Mary"
student["last name"] = "Joanne"
student["grade"] = 7
student["date of birth"] = "May 9th 1995"
student["performance"] = "Very good"
print(student)

# Modifying Value in a Dictionary
"""
To modify a value in a dictionary, give the name of the dictionary with the key
in a square bracket[] and then the new value you want associated with that key.

For example, changing the students performance from 'very good' to 'excellent':
"""
print(student)
print(f"{student['first name'].title()} is a {student['performance'].lower()} "
      f"student")

student["performance"] = "Excellent"
print(f"{student['first name'].title()} is now an "
      f"{student['performance'].lower()} student")
"""
Another example, tracking the position of an aircraft that can move at different 
speeds. We'll store a value representing the aircraft's current speed and then
use it to determine how far to the right the aircraft should move:
"""
blackbird = {'x_position': 0, 'y_position': 25, 'speed': "transonic"}
print(f"Original position is latitude {blackbird['x_position']} and longitude "
      f"{blackbird['y_position']} and moving at {blackbird['speed']}.")

# Move the aircraft east (right).
# Determine how far to move the aircraft based on its current speed
if blackbird['speed'] == 'subsonic':
    x_increment = 10
    y_increment = 5
elif blackbird['speed'] == 'transonic':
    x_increment = 20
    y_increment = 10
elif blackbird['speed'] == 'supersonic':
    x_increment = 30
    y_increment = 15
# Algorithm for the new position
blackbird['x_position'] = blackbird['x_position'] + x_increment
blackbird['y_position'] = blackbird['y_position'] + y_increment

print(f"At {blackbird['speed']} speed, the new position of the aircraft is at "
      f"latitude {blackbird['x_position']}, longitude {blackbird['y_position']}")

# Removing key-value Pairs
"""
When a piece of information is no longer needed  that's stored in a dictionary,
you can use 'del' statement to completely remove a key-value pair. To remove a 
key-value pair use the del statement in front of the dictionary name with the 
value you wish to remove in the square bracket[]. For example:
"""
ceo = {'name': 'John Phillip', 'age': 22, 'location': 'Nigeria'}
del ceo['location']
print(ceo)

# A dictionary of similar objects
"""
You can also use a dictionary to store one kind of information about many 
objects. For example, recording the scores for a class on a particular subject:
"""
math_score = {
    'jen': 58,
    'mark': 68,
    'john': 80,
    'toby': 46,
}
# To use the dictionary value
score = math_score['toby']
print(f"Toby scored a {score}/100 in his maths exam")

# Using get() to Access Values
"""
Using keys in square brackets to retrieve the value you're interested in from a 
dictionary might cause one potential problem: If the key you ask for doesn't 
exist, you'll get a KeyError. To avoid this error, it is sensible to use the 
get() method to set a default value that will be returned if the requested key 
doesn't exist. For example:
"""
car = {'brand': 'Tesla', 'model': 'Roadster 2', 'power': 1900}
car_color = car.get('color', )
print(car_color)

# Looping through a Dictionary
"""
Dictionaries can be used to store information in a variety of ways; therefore, 
several different ways exist to loop through them. You can loop through all of a
dictionary's key-value pairs, through its keys, or through its values.
"""
# Looping Through All Key-Value Pairs
"""
Lets use a dictionary that stores the types of game consoles in a store. And we 
will loop through its key-value pairs.
"""
consoles = {
    'sony': 'PS4',
    'microsoft': 'Xbox one',
    'nintendo': 'switch',
    'oculus': 'rift wireless',
}
for key, value in consoles.items():
    print(f"\nCompany: {key}")
    print(f"Console: {value}")
"""
To write a for loop for a dictionary, you create two variable names that will 
hold the key and value in each key-value pair as shown in line 162, then you 
mention the name of the dictionary together with the items() method, which 
returns a list of key value pairs. The for loop then assigns each of the pairs
to the two variables provided at line 163 & 164. 

We could also use the value pairs to loop in a sentence. For example:
"""
math_score = {
    'jen': 58,
    'mark': 68,
    'john': 80,
    'toby': 46,
}
for name, score in math_score.items():
    print(f"{name.title()}'s maths score is {score}/100")

# Looping through All the Keys in a Dictionary
"""
The keys() method is useful when you don't need to work with all the value in a 
dictionary. To loop through a dictionary's keys, we first need to declare a for
loop, after the for loop keyword we then call a variable that will hold the 
key in the dictionary, then mention the name of the dictionary together with the
key() method. For example:
"""
capital = {
    'USA': 'Washington DC',
    'United kingdom': 'London',
    'Nigeria': 'Abuja'
}
for country in capital.keys():
    print(f"The country is {country}.")
# if statement in a Dictionary
tropics = {
    'Indonesia': 'Bali',
    'Nigeria': 'Lagos',
    'Ghana': 'Accra',
    'Brazil': 'Rio',
}
beaches = ['Ghana', 'Brazil']
for country in tropics.keys():
    print(f"{country.title()} is a tropical country.")
    if country in beaches:
        place = tropics[country].title()
        print(f"\t{country.title()} has beautiful beaches in {place}.")

# Looping through a Dictionary's Keys in a Particular Order
"""
Usually in Python, looping through a dictionary returns the items in the order 
they were inserted, but sometimes we might want to loop through a dictionary in
a different order. One way to do so is to sort the keys as they are returned in 
the loop. Using the sorted() function to get a copy of the keys in order:
"""
favorite_flavors = {
    'johnny': 'vanilla',
    'jane': 'salty caramel',
    'igor': 'chocolate',
    'jude': 'vanilla',
    'olga': 'mango',
}
for name in sorted(favorite_flavors.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through All Values in a Dictionary
"""
If you're primarily interested in the values that a dictionary contains, you can 
use the values() method to return a list of values without any keys. For example
, taking a poll of customers favorite ice-cream flavors and wanting to create a 
list of all flavors chosen the pollsters without revealing the name of the 
person who chose each flavor:
"""
favorite_flavors = {
    'johnny': 'vanilla',
    'jane': 'salty caramel',
    'igor': 'chocolate',
    'jude': 'vanilla',
    'olga': 'mango',
}
print("The following flavors have been chosen by the public: ")
for flavor in favorite_flavors.values():
    print(flavor.title())
"""
In this result, we notice it also pulls values without checking for repetitive
values in the list. This might work fine with small amounts of data but in large
data of respondents, this would result in a very repetitive list. To see each
flavor chosen without repetition, we can use the set() function. A set is 
collection in which each item must be unique:  
"""
favorite_flavors = {
    'johnny': 'vanilla',
    'jane': 'salty caramel',
    'igor': 'chocolate',
    'jude': 'vanilla',
    'olga': 'mango',
}
print("\nThese are the most popular flavors with consumers:")
for flavor in set(favorite_flavors.values()):
    print(flavor.title())

# Nesting Dictionary
"""
Sometimes you'll want to store multiple dictionaries in a list, or a list of 
items as a value in a dictionary. This practice is called Nesting, You can nest 
a dictionary inside a list, a list of items inside a dictionary, or even a 
dictionary inside another dictionary.
"""

# A List of Dictionaries
"""
We'll start by creating a few separate dictionaries called agent_0, 1, 2, these 
variables have similarities in a database but we don't want our screen full of
separate data, so make them into a list called agents in which each agent is a 
dictionary of information about that agent:
"""
agent_0 = {'race': 'caucasian', 'height_cm': 185, 'mass_kg': 75}
agent_1 = {'race': 'nubian', 'height_cm': 190, 'mass_kg': 90}
agent_2 = {'race': 'asian', 'height_cm': 175, 'mass_kg': 75}

agents = [agent_0, agent_1, agent_2]
for agent in agents:
    print(agent)

"""
In game development, a more realistic example would involve more than three 
characters with code that automatically generates each alien. In the following
example we use the range() function to create an army of 20 agents: 
"""
# Make an empty list for storing the agents
agents = []

# Make 5 nubian agents, 5 caucasian agents and 10 asian agents
for agent_number in range(5):
    nubian_agent = {'race': 'nubian', 'height_cm': 190, 'mass_kg': 90,
                    'health': 1000, 'iq': 250, 'strength': 'mighty'}
    agents.append(nubian_agent)

for agent_number in range(5):
    caucasian_agent = {'race': 'caucasian', 'height_cm': 185, 'mass_kg': 80,
                       'health': 1100, 'iq': 288, 'strength': 'fast'}
    agents.append(caucasian_agent)

for agent_number in range(10):
    asian_agent = {'race': 'asian', 'height_cm': 178, 'mass_kg': 70,
                   'health': 1500, 'iq': 300, 'strength': 'fast'}
    agents.append(asian_agent)

for agent in agents[:11]:
    print(agent)
print("\nSTART MISSION\n")

# Show how many agents have been created.
print(f"Total numbers of agents in the city is {len(agents)}.")

# To modify characters in the list
for agent in agents[10:16]:
    if agent['race'] == 'asian':
        agent['race'] = 'arabian'
        agent['height_cm'] = 188
        agent['strength'] = 'weapons'
for agent in agents[10:]:
    print(agent)

# A List in a Dictionary
"""
Rather than putting a dictionary in a list, it's sometimes useful to put a list 
in a dictionary. For example, consider how you might want to describe the specs
of a computer a customer is buying. If you were to use only a list, all you 
could store is a list of the computer specs. With a dictionary, a list of specs
can just be one aspect of the computer you are describing.
"""
# Store information about the a computer being ordered.
computer = {
    'brand': 'Apple',
    'model': 'Macbook Pro',
    'specs': ['intel core i9', 'vega 20 gpu', '15\" super retina display',
              '1TB SSD']
}
# Summarize the order
print(f"You ordered a {computer['model']}, with the following specification: ")

for spec in computer['specs']:
    print(f"\t{spec.title()}")

# Another example, polling people on their favorite flavors of ice-cream
favorite_flavors = {
    'johnny': ['vanilla', 'dark chocolate', 'coconut'],
    'jane': ['strawberry', 'truffle', 'banana'],
    'igor': ['chocolate', 'oreo'],
    'jude': ['bubblegum', 'avocado'],
    'olga': ['mango', 'dragon-fruit', 'passion'],
}
for name, flavors in favorite_flavors.items():
    print(f"\n{name.title()}'s favorite ice-cream flavors are:")
    for flavor in flavors:
        print(f"\t{flavor.title()}")

# A Dictionary in a Dictionary
"""
You can nest a dictionary in another dictionary, but your code can get complex
quickly when you do. For example, if you users for a website, each with a unique
username, you can use the username as the keys in a dictionary. You can then 
store information about each user by using a dictionary as the associated with
their username. 

In the following listing, we store four pieces of information about each user:
their first name, last name, location and age. We'll access this information 
by looping through the usernames and the dictionary of the information 
associated with each username:   
"""
users = {
    'jakey': {
        'first name': 'jake',
        'last name': 'Kayle',
        'location': 'united states',
        'age': 18,
    },
    'tee-jay': {
        'first name': 'toby',
        'last name': 'john',
        'location': 'ukraine',
        'age': 22,
    },
    'luvly': {
        'first name': 'lubov',
        'last name': 'steblina',
        'location': 'ukraine',
        'age': 23,
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first name']} {user_info['last name']}"
    location = user_info['location']
    age = user_info['age']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location}")
    print(f"\tAge: {age}")
    
# The following code simulates a picnic and counts the number of distinct food items 
# brought by the picnic goers

picnic_guests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'John': {'beef steaks': 12, 'beer': 8},
    'Ivan': {'chicken': 20, 'beer': 8},
    'Dasha': {'Juice': 4, 'Doritos': 2}
}

def total_items(guests, item):
    """Counts the number of unique items brought by the guests ands accumulates them"""
    sum_items = 0
    for guest, itinerary in guests.items():
        sum_items += itinerary.get(item, 0)
    return sum_items

print("These are the sum of distinct food items brought to the picnic:")
print(f"\t- Apples: {total_items(picnic_guests, 'apples')}")
print(f"\t- Pretzels: {total_items(picnic_guests, 'pretzels')}")
print(f"\t- Beef steaks: {total_items(picnic_guests, 'beef steaks')}")
print(f"\t- Beer: {total_items(picnic_guests, 'beer')}")
print(f"\t- Juice: {total_items(picnic_guests, 'Juice')}")
print(f"\t- Chips: {total_items(picnic_guests, 'Doritos')}")