"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of green, yellow or red.
1. Write an if statement to whether the alien's color is green. If it is, print
a message that the player just earned 5XPs
2. Write one version that passes the test and one that fails. The one that fails
(The one that fails should have no output
"""
alien_color = "green"
if alien_color == "green":
    print("You've earned 5XP.")
if alien_color != "green":
    print("")
"""
5-4. Alien Colors #2: Choose a color for an alien as you did in ex.5-3 & write
an if-else chain.
1. If the alien color is green, print the statement that the player just earned
5XP for shooting the green alien.
2. If the alien's color isn't green, print the statement that player just earned
10XP
"""
alien_color = "blue"
if alien_color == "green":
    print("You've earned 5XP")
else:
    print("You earned 10XP")
"""
5-5 Alien Color #3: Turn your if-else chain into a if-elif-else chain.
1. If the alien is green, print the player earned 5XP
2. If the alien is yellow, print the player earned 10XP
3. Id the alien is red, print the player earned 15XP
"""
alien_color = "red"

if alien_color == "green":
    print("You earned 5XP!!!")
elif alien_color == "yellow":
    print("You earned 10XP!!!!!")
elif alien_color == "red":
    print("You earned 15XP!!!!!")
else:
    print("")
"""
5-6 Stages of life: Write an if-elif-else chain that determines a person's stage
of life. Set a value for the variable age, and then:
1. If then person is less than 2yrs old, print the message that the person is
an infant
2. If the person is at least 2yrs old but less than 4yrs old, print the message 
that the person is a toddler.
3. If the person is at least 4yrs old but less than 13yrs old, print the message
that the person is an adolescent.
4. If the person is at least 13yrs old but less than 20yrs old, print a message
that the person is a teenager.
5. If the person is at least 20yrs old but less than 65, print a message the the 
person is an adult
6. If the person is 65 or older, print a message that the person is an elder
"""
age = 2

if age < 2:
    print("\nYou are an infant.")
elif 2 <= age < 4:
    print("\nYou are a toddler.")
elif 4 <= age < 13:
    print("\nYou are an adolescent.")
elif 13 <= age < 20:
    print("\nYou are a teenager.")
elif 20 <= age < 65:
    print("\nYou are an adult.")
elif age >= 65:
    print("\nYou are an elder")

"""age = 2

if age < 2:
    person = "infant"
elif 2 <= age < 4:
    person = "toddler"
elif 4 <= age < 13:
    person = "adolescent"
elif 13 <= age < 20:
    person = "teenager"
elif 20 <= age < 65:
    person = "adult"
elif age >= 65:
    person = "elder"

print(f"\nYou are a {person.title()}")"""

"""
5-7 Favorite fruit: Make a list of your favorite fruits, and then write a series
of independent if statements that check for certain fruits in your lists
1. Make a list of three favorite fruits and call it favorite_fruits.
2. Write five if statements. Each check whether a certain kind of fruit is in 
the list. If the fruit is in your list, the if block should print a statement.
"""
favorite_fruits = ["apple", "pear", "strawberry"]
if "apple" in favorite_fruits:
    print("Yes! You've got apples")
if "pear" in favorite_fruits:
    print("Yes! You've got pears")
if "avocados" in favorite_fruits:
    print("Yes! You've got some avocados.")
if "bananas" in favorite_fruits:
    print("Yes! There are bananas.")
if "strawberry" in favorite_fruits:
    print("Yes! You've got strawberries")
