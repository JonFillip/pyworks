import json

"""
10-11. Favorite number: Write a program that prompts the user for their favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, "I know your favorite
number! It's ___".

10-12. Favorite number remembered: Combine the program in 10-11 into one file.
If the number is already stored, report the favorite number to the user. If not,
prompt for the user's favorite number and store it in a file. Run the program
twice to see that it works.
"""


def add_favorite_number():
    """Prompt the user for their favorite number and export to the json file"""
    file = "files_and_exceptions/favorite_number.json"
    poll = input("What is your favorite number: ")
    polled = int(poll)
    try:
        with open(file, 'a') as file_object:
            json.dump(polled, file_object)

    except FileNotFoundError:
        print(f"Sorry but {file} not found. Please examine the file path or "
              f"file spelling is correct.")


def remember_number():
    """Load the favorite number, if it has been stored previously. Otherwise
  prompt the user to enter their favorite number and store it"""
    filename = "files_and_exceptions/favorite_number.json"
    try:
        with open(filename) as read_object:
            result = json.load(read_object)
    except FileNotFoundError:
        poll = input("Enter your favorite number: ")
        polled = int(poll)
        with open(filename, 'w') as f:
            json.dump(polled, f)
            print(f"I will remember your favorite number to be {polled}")
    else:
        print(f"Hi there, I remember your favorite is {result}")


add_favorite_number()
remember_number()

"""
10-13. Verify user: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the 
first time. We should modify it in case the current user is not the person who 
last used the program
    Before printing a welcome back message in greet_user(), ask the user if this
is the correct username. If it's not, call get_new_username() to get the correct
username.
"""


def get_user():
    """Ask the user for their username and store it in a json file"""
    filename = "username.json"
    username = input("Please enter your username: ")
    try:
        with open(filename, 'a') as user_file:
            json.dump(username, user_file)

    except FileNotFoundError:
        print(f"Sorry {filename} does not found. Please check the file path "
              f"and file spelling for errors.")

    else:
        print(f"Hello {username}, we will remember you next time you log in.")


def get_stored_username():
    """Get the stored user name and return it"""
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)

    except FileNotFoundError:
        return None

    else:
        ask_user = input(f"Is {username} your username? Yes/No ")
        if ask_user == "yes" or "Yes":
            print(f"Welcome back {username}!")

        elif ask_user == "no" or "No":
            username = get_new_username()
            return username


def get_new_username():
    """Get new username if the current user is a new user"""
    username = input("Please enter a username: ")
    filename = "username.json"
    with open(filename, 'a') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")

    else:
        username = get_new_username()
        print(f"We will remember you when you come back, {username.title()}!")


get_user()
greet_user()
