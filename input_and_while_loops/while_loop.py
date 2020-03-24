"""
The for loop takes a collection of items and executes a block of code once for
each item in the collection. In contrast, the while loop runs as long as, or
while, a certain condition is true. For example:
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Breaking the while loop
"""
It is often necessary to allow the user to quit your program while inside the 
while loop. This can be done by defining a quit value, a keyword or condition 
that when met breaks or end the loop. For example:
"""
favorite_color = "space gray"
question = "\nWhat's my favorite color? "
question += "\nEnter 'quit' if you give up guessing. "
message = ""

while message != "quit":
    message = input(question)
    if message != favorite_color:
        print(message)
    elif message == "quit":
        break
    elif message == favorite_color:
        break

# Using a Flag
"""
For a program that should run only as long as many conditions are true, you can
define one variable that determines whether or not the entire program should 
run or is active. This variable is called a flag, acts as a signal to the 
program. You can set your program to run while the flag is set to True and stop
it from running when it is False and vice versa.
"""
voice_mail = "Hi! This John's voice mail please leave a message and I'll back" \
             " to you as soon as possible. Thank you and have a great day. "
active = True
while active:
    message = input(voice_mail)

    if message == 'drop':
        active = False
    else:
        print("Message saved.")
        break
# N.B: To exit a while or for loop immediately without running any remaining
# code in the loop, regardless of the results of any conditional test, use the
# 'break' statement

"""
Using Continue in a Loop

Rather than breaking out of the loop entirely without executing the rest of the
code, you can use the continue statement to return to the beginning of the loop
based on the result of a conditional test. For example, consider a while loop
that counts from 1 to 10 but print only the odd numbers in that range:
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding Infinite Loops
"""
Every while loop needs a way to stop running so it won't continue to run forever
. For example, this guessing game:
"""
guesses = 0
secret_word = "iron-man"
guess = None
while guess != secret_word and guesses < 5:
    guess = input("Who is my favorite super-hero of all time? ")
    guesses += 1
    if guess == secret_word and guesses < 5:
        print("Awesome! You won.")
        break
else:
    print(f"Game over! My favorite superhero of all time is {secret_word}.")

# Using a while loop with Lists and Dictionaries
"""
Keeping track of a large amount of data in lists or dictionaries is more 
efficient using a while loop. A for loop is effective for looping through a list
or dictionary, but it makes modifying information in the list or dictionary
cumbersome for python to keep track of the items in the list. To modify a list
or dictionary as you work through it, use a while loop. Using a while loop with 
lists or dictionaries allows you to collect, store, and organise lots of input
to examine and report on later.
"""
# Moving Items from One List to Another
"""
Consider a list of newly registered but unverified users of a website. After we 
verify these users, how can we move them to a separate list of confirmed users?
One way would be to use a while loop to pull users from the list of unconfirmed
users as we verify them and then add them to a separate list of confirmed users.
Here's what that code might look like: 
"""
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ["alice", "brain", "candace"]
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each of the unconfirmed users into a list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users
print("\nThe following users have been verified:")
for user in confirmed_users:
    print(user.title())

# Removing All instances of specific values from a list
"""
To remove a value from a list we use the remove() function. I previously used it
but to remove one specific that appeared only once. But the remove() function 
can also be used to remove a value that appears multiple times in a list by 
using it with a while loop. For example:
"""
# In the list the name 'new york' appears multiple times in the list
cities = ["lagos", "madrid", "accra", "new york", "hung kong", "new york", "LA"]
for city in cities:
    print(city)
while "new york" in cities:
    cities.remove("new york")
print(cities)

# Filling a Dictionary with User Input
"""
You can prompt for as much input as you need in each pass through a while loop.
In real world scenarios when programming, we need to collect dictionaries or
list of data from the user. To do so we'll want to store the data we gather in a 
dictionary, because we want to connect each data to a specific person or file:
"""
user_profile = {}
# Set a flag to indicate that the user is active
user_active = True

while user_active:
    # Prompt the user for his/her gender, name, age and location
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    gender = input("Please enter your gender: ")
    age = input("Enter your age: ")
    age = int(age)
    location = input("Enter your location: ")

    # Store the user's data in the dictionary
    user_profile[first_name] = first_name
    user_profile[last_name] = last_name
    user_profile[gender] = gender
    user_profile[age] = age
    user_profile[location] = location

    # Ask if anyone will like to have their location status made public
    status = input("Would you like to turn on location status? (yes/ no) ")
    if status == "no":
        del(user_profile[location])
        break

# Now display all the user's data
for key, value in user_profile.items():
    full_name = f"{user_profile[first_name]} {user_profile[last_name]}"
    print(f"\nUsername: {full_name.title()}")
    print(f"\t Sex: {user_profile[gender].title()}")
    print(f"\tAge: {user_profile[age]}")
    print(f"\tLocation: {user_profile[location]}")

