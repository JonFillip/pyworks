"""
6-7. People: Start with the program you wrote in exercise 6-1. Make two new
dictionaries representing different people, and store all three dictionaries in
a list called people. Loop through your list of people. As you loop through the
list, print everything you know about each person
"""
people = {
    'luke_cage': {
        'first name': 'luke',
        'last name': 'peterson',
        'age': 21,
        'city': 'new york',
    },
    'johnnie': {
        'first name': 'john',
        'last name': 'webster',
        'age': 22,
        'city': 'kiev',
    },
    'sophie': {
        'first name': 'sophia',
        'last name': 'turner',
        'age': 18,
        'city': 'odessa',
    },
}
for person, person_info in people.items():
    print(f"\nPerson: {person.title()}.")
    full_name = f"{person_info['first name']} {person_info['last name']}"
    location = person_info['city']
    age = person_info['age']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location}")
    print(f"\tAge: {age}")
    print(f"\tLocation: {location}")

"""
6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
ent pet. In each dictionary, include the kind of animal and the owner's name.
Store these dictionaries in a list called pets. Next, loop through your lists &
as you do, print everything you know about each pet.
"""
pet_0 = {'pet': 'dog', 'owners name': 'sophie'}
pet_1 = {'pet': 'cat', 'owners name': 'john'}
pet_2 = {'pet': 'parrot', 'owners name': 'alina'}
pet_3 = {'pet': 'goldfish', 'owners name': 'tania'}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet}")

"""
6-9. Favorite places: Make a dictionary called favorite_places. Think of three 
names to use keys in the dictionary, and store one to three favorite places for 
each person. To make this exercise a bit more interesting, ask some friends to 
name a few of their favorite places. Loop through the dictionary, and print each
person's name and their favorite places.
"""
favorite_places = {
    'lubov': ['switzerland', 'bora bora', 'maldives'],
    'john': ['namibia', 'sweden', 'kiev'],
    'vlad': ['germany', 'england', 'ukraine'],
}
for name, places in favorite_places.items():
    print(f"\nMy name is {name.title()} & these are my favorite places in the "
          f"world: ")
    for place in places:
        print(f"\t{place.title()}")

"""
6-10. Favorite numbers: Modify your program from exercise 6-2 so each person can
have more than one favorite number. Then print each person's name along with 
their favorite numbers.
"""
favorite_number = {
    'tansi': [8, 0],
    'emmanuel': [100, 2, 5],
    'toby': [5],
    'vlad': [0, 10, 100],
    'mark': [6, 66, 36],
}
for name, numbers in favorite_number.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city &
include the country that the city is in, its appropriate population, and one 
fact about that city. The keys for each city's dictionary should be something
like country, population, and fact. Print the name of each city and all of the 
information you have stored about it.
"""
cities = {
    'lagos': {
        'country': 'nigeria',
        'population': 21_324_000,
        'fun fact': 'It is most populous city in africa',
    },
    'tokyo': {
        'country': 'japan',
        'population': 13_943_000,
        'fun fact': 'It has the most top-rated restaurants in the world. It is'
                    ' home to over 14 three-star Michelin restaurants',
    },
    'kiev': {
        'country': 'ukraine',
        'population': 3_000_000,
        'fun fact': 'It has the 2nd deepest subway in the world known as '
                    'arsenalna metro station',
    },
}
for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fun fact']
    print(f"\n{city.title()} is the largest city in {country.title()} and has a"
          f"population of {population}. One fun fact about {city.title()};"
          f" {fact}")

