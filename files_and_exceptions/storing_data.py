import json
import os

# Storing Data
"""
When writing programs that require the user to enter certain information, it is
almost typical to store that information in data structures such as list and
dictionaries. When the user closes a program, it is almost necessary to store
data they user may have entered. One way to do this is to use the json module.

    The json module allows the programmer to dump(upload) simple python data
structures into the file and load (download) the data from that file the next
time the program runs.
"""

# Using json.dump() and json.load()
"""
As discussed in the text above json.dump() allows the programmer to upload data
structures into a file for storage while, json.load() lets the program 
re-download the data from the file for further use when the program is again.
    For example, adding a dictionary of user profiles. The json.dump() function
takes two args: a piece of data to store and a file object it can store the data
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

filename = 'users.json'
with open(filename, 'w') as file_object:
    json.dump(users, file_object)

with open(filename, 'r') as file_item:
    user_profile = json.load(file_item)

print(user_profile)

# Saving and Reading User-Generated Data
"""
Saving data with json is useful when you're working with user-generated data, 
because if you don't store your user's information somehow you might lose it 
when the program stops running. Let's look at an example of storing data the 
user provides in dictionary then uploading it to a json file format and then 
remember the users details when the user logs back in:
"""


def collect_data():
    """Collect user input to build a dating profile and store it in a
    dictionary """
    date_profile = {
        'first_name': '',
        'surname': '',
        'gender': '',
        'age': '',
        'location': ''
    }

    validations = {
        'first_name': (None, None),
        'surname': (None, None),
        'gender': (validate_gender, 'Please select either "male" or "female".'),
        'age': (int, 'Age must be an integer.'),
        'location': (None, None)
    }

    for key in date_profile:
        value = query_user(key)
        if value is None:
            return
        validate, msg = validations.get(key)
        if validate:
            retry = True
            while retry:
                try:
                    validate(value)
                    retry = False
                except ValueError:
                    print(msg)
                    value = query_user(key)
                    if value is None:
                        return
        date_profile[key] = value
    return date_profile


def export_profile(file_path, date_profile):
    """Export the content of the dictionary to the json file"""
    # read in json, or create new list
    if os.path.exists(file_path):
        with open(file_path) as fp:
            j_data = json.load(fp)
    else:
        j_data = []
    j_data.append(date_profile)
    # write out
    with open(file_path, 'w') as fp:
        json.dump(j_data, fp)


def query_user(key):
    query = "Enter your {} (type 'quit' to exit): ".format(
        key.replace('_', ' '))
    value = input(query)
    if value.lower() == 'quit':
        print('Exiting.')
        return None
    return value


def validate_gender(g):
    """Validate the input of the gender given by the user"""
    try:
        assert g.lower() in ('male', 'female')
    except AssertionError:
        print("Please select either 'male' or 'female'. ")


if __name__ == '__main__':
    dp = collect_data()
    export_profile("dating_profile.json", dp)


def load_data():
    """Download the data in dating_profile.json"""
    file = "/Users/johnphillip/Desktop/python_work/dating_profile.json"
    try:
        with open(file) as profile_object:
            profile = json.load(profile_object)
            print("Welcome to Haay!")
            print(f"Here is the latest sign up:\n{profile}")
    except FileNotFoundError:
        pass


load_data()
