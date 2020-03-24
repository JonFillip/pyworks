# Variables and methods #

message = "Hello world and welcome to the future!"
print(message.title())
print(message.upper())
print(message.lower())

first_name = "John"
last_name = "Phillip"
# formatted strings
full_name = f"{first_name} {last_name}"
print(full_name)
text = f"Hello, {full_name.title()}!"
print(text)

# Note: If you are using python 3,5 or lower you'll need to use the format()
# method rather than the f syntax
# For  example - full_name = "{} {}".format(first_name, last_name)

# Adding whitespace to strings with tabs or newlines
# Adding the character \t creates a whitespace

print("\tThis is the moment you've all been waiting for.")
# while to create a new line, we use the character '\n'
print("Car manufacturers:\nBugatti\nAston Martin\nPorsche")

""""
To ensure that there are no extra whitespace on the left or right side of a 
string we use the method'.strip()' to remove whitespace from the right side of 
a string is the method command '.rstrip()' and to remove whitespace from the 
left side of a string use '.lstrip()' 
"""
favorite_city = "Kiev "
print(favorite_city)
print(favorite_city.rstrip())   # for removing whitespace from the right side
# OR
favorite_movie = " Titanic"
print(favorite_movie)
print(favorite_movie.lstrip())  # for removing whitespace from the left side

# or from both sides at once using '.strip()'
animal = " Python "
print(animal)
print(animal.strip())
# Striping functions are used most often to clean up user input before it is
# stored in a program
# Avoiding syntax Errors with Strings
"""
One of the most common errors made when writing in a string is the dealing with 
syntax errors. These are commonly caused when using an apostrophe in a 
statement. 
"""
# When using an apostrophe in a string it is important to use double quotes
# ("") to wrap around your statement
description = "Mary's boyfriend is from England"
print(description)

# Do not use single quotes when using an apostrophe in your statement else it
# will result in syntax error
# For example text = 'Its Mary's bag' will produce a syntax error when run
