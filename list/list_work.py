# LOOPING THROUGH AN ENTIRE LIST
"""
The concept of looping is important because it's one of the most common ways a
computer automates repetitive tasks.
For example in a lis statistical operation on every element. Or perhaps you'll
want to display each headline from a list
of articles on a website. When you want to do the same action with every item in
a list, you can use the python's 'for'
loop
"""
cities = ["Kyiv", "New York", "Sydney", "Lagos", "Shangai", "Hong Kong",
          "Tokyo"]
for city in cities:
    print(f"\nWelcome to {city}")
    print(f"Please enjoy your stay here!")

print("\nThank you")
"""
You can also write as many lines of code as you like in the 'for' loop.
Every indented line following the line 
for city in cities is considered inside the loop,and each indented line is 
executed once for each value in the list.
Therefore, you can do as much work as you like with each value in the list. You 
can use as many line as you like in
your 'for' loop. In practice you'll often find it useful to do a number of 
different operations with each item in a list when using a 'for' loop.
"""
# DOING SOMETHING AFTER THE FOR LOOP
"""
To summarize a block of code after using the for loop is as simple as 
un-indenting the next line after finishing writing 
all the code you require in the for loop. 
"""

# AVOIDING INDENTATION ERROR
"""
Python uses indentation to determine how a line, or group of lines, is related to the rest of the program. It uses white
-space to force you to write neatly formatted code with a clear visual structure.As one begins to write code that relies
on proper indentation, you'll need to watch out for a few common indentation errors. For example:
1. Forgetting to indent: Always indent the line after the for, if, else or elseif statement. If you forget python will 
remind you.
2. Forgetting to indent additional lines: Sometimes your loop will run without any errors but won't produce the results
you expected. This can happen when you're trying to do several tasks in a for loop and you forget to indent some of the
lines. This is a logical error. The syntax is valid Python code, but the code does not produce the desired result bcos
a problem occurs in its logic.
3. Indenting Unnecessarily: If you accidentally indent a line that doesn't need to be indented, Python informs you about 
the unexpected indentation. For example:
message = "Good morning! And welcome to the Steve Jobs theatre"
    print(message); Python gives you this error warning; IndentationError: unexpected indent
4. Indenting Unnecessarily after the loop: If you accidentally indent code that should run after a loop has finished,
that code will be repeated once for each item in the list. Sometimes this prompts Python to report an error, but often 
this will result in logical error.
5. Forgetting the colon: The colon at the end of a for loop statement tells python to interpret the next line as the 
start of a loop. If you forget the colon python will print a syntax error warning.  
"""
# MAKING A NUMERICAL LIST
"""
Many reasons exist to store a set of numbers. For example, you'll need to keep track of the positions of each character
in a game and you might want to keep track of a player's high score. In data visualization, you'll need almost always 
work with sets of numbers, such as temperatures, distances, population sizes, or latitude and longitude values, among 
other types of numerical sets.
"""

# Using The range() Function
# Python's range() function makes it easy to generate a series of numbers. For example:
for age in range(5, 21):
    print(age)
"""
NOTE: Although the code should looks like it should print the values from 5 to 21 it doesn't print out 21. This is due 
to the off-by-one behaviour you'll see in most programming languages. The range() function causes python to start count
-ing at the first value you give it, and it stops when it reaches the second value you provide. Hence, the output never
contains the end value, which would have been 21.
To print the 5 to 21, you would have to use the range(5, 22) 
"""

# Using range() to Make a List of Numbers
"""
If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() 
function. When you wrap list() around a call to range() function, the output will be a list of numbers. 
"""
audience = list(range(5, 21))
print(audience)  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

"""
We can also use the range() function to tell python to skip numbers in a given range. If you pass a third argument to 
range(), Python uses that value as a step size when generating numbers. For example:
"""
street_numbers = list(range(1, 22, 5))
print(street_numbers)  # [1, 6, 11, 16, 21]
"""
In this example, the range() function starts with the value 1 with the value at the middle 22 being the end of the range
and there is the value 5 at the end of the argument, the third argument is the value that helps python recognize the 
step size it should when generating the number. So it adds 5 repeatedly until it reaches or passes the end value, 22 to
produce the result [1, 6, 11, 16, 21].
"""
# You can also create almost any set of numbers you want with the range()
# function. For example
squares = []
for value in range(3, 30, 3):
    square = value ** 2
    squares.append(square)
print(squares)
"""
We start with an empty list called squares at line 89. At line 90 we tell python to loop through each value from 3 to 30
using the range() function. Inside the loop the current value is repeatedly added by 3 and is raised to the second power
and assigned to the variable square at line 91. At line 92, each new value of square is appended to the list squares. 
Finally, when the loop has finished running, the list of squares is printed at line 93.  
[9, 36, 81, 144, 225, 324, 441, 576, 729]
"""
# To write this code more precisely, omit the temporary variable square and
# append each new value directly to the list:
squares = []
for value in range(3, 30, 3):
    squares.append(value ** 2)

print(squares)  # [9, 36, 81, 144, 225, 324, 441, 576, 729]

# Simple Statistics with a List of Numbers
"""
A few Python functions are helpful when working with lists of numbers. For example, you can easily find the minimum, 
maximum, and sum of a list of numbers:
"""
digits = [3, 5, 7, 89, 1, 86, 2, 100]
print(min(digits))  # Prints the minimum value in the list
print(max(digits))  # Prints the maximum value in the list
print(sum(digits))  # Prints the sum of the value in the list

# LIST COMPREHENSION
"""
The approach described earlier for generating the list squares consisted of using three to four line of code. A 'list 
comprehension' allows you to generate that same list in just one line. A list comprehension combines the for loop and 
the creation of new elements into one line of code, and automatically appends each new element. For example
"""
squares = [value ** 2 for value in range(3, 30, 3)]
print(squares)  # [9, 36, 81, 144, 225, 324, 441, 576, 729]

"""
To use this syntax begin with a descriptive name for the list. Next, open a square bracket[] and define the expression 
for the value you wish to store in the list. In the example the expression is value ** 2, which raises the value to the 
second power. Then, write a for loop to generate the numbers you want to feed into the expression and close the bracket.
The loop in the example above is for value in range(3, 30, 3), which feeds the value in multiples of 3 until it reaches 
30 into the expression value ** 2. Notice that there is no colon at the end of the for statement.
"""

# WORKING WITH PART OF A LIST
"""
Slicing a List
To make a slice, you specify the index of the first and last elements you want to work with. As it is with range()
function, Python stops one item before the second index you specify. For example:
"""
# To output the first three elements in a list of players
players = ["Thor", "Ninja", "Keem", "Toby_One", "Kimberly", "Cara"]
print(players[0:3])  # ['Thor', 'Ninja', 'Keem']
# You can also generate any subset of a list. For example:
print(players[2:6])  # ['Keem', 'Toby_One', 'Kimberly', 'Cara']
# If you omit an index in a slice, Python automatically starts your slice at the beginning of the list:
print(players[:4])  # ['Thor', 'Ninja', 'Keem', 'Toby_One']; Without a starting index Python starts at the beginning of
# the list.
# If you also end without an ending index, Python will continue displaying all the items in the list till the end:
print(players[1:])  # ['Ninja', 'Keem', 'Toby_One', 'Kimberly', 'Cara']
# If you want to print the last 3 players names in the roster, we can use the slice players[-3]:
print(players[-3:])  # ['Toby_One', 'Kimberly', 'Cara']

# LOOPING THROUGH A SLICE
"""
You can use a slice in a for loop if you want to loop through a subset of the elements in a list. In the next example we 
loop through the first four players and print their names as part of a simple roster:
"""
print("Here are the players moving on to the Fornite quarter final championship:")
for player in players[:4]:
    print(player)
print("\nITS GAME ON!")

# COPYING A LIST
"""
To copy a list, you can make a slice that includes the entire original list by omitting the first and last index ([:]).
This tells python to make a slice that starts and ends with the first and ends with first and last item, producing the 
entire list. For example copying a persons travel destination that you have common destinations with:
"""
person_trips = ["Dubai", "India", "New York", "Kiev", "London", "Bahamas"]
my_trips = person_trips[:]

print("You and Person have been to the following travel locations:")
print(my_trips)

print("\nHere are the person's travel destinations:")
for destination in person_trips:
    print(destination)
"""
You and Person have been to the following travel locations:
['Dubai', 'India', 'New York', 'Kiev', 'London', 'Bahamas']

Here are the person's travel destinations:
Dubai
India
New York
Kiev
London
Bahamas
"""
# To prove we actually have two separate list we could append an item unique
# to each list
my_trips.append("Ghana")
person_trips.append("Canada")
# My trips
print("\nHere is a list of all my trips:")
for trip in my_trips:
    print(trip)
print("\nBon voyage!")
# Person's trips
print("\nHere are all the trips person made:")
for destination in person_trips:
    print(destination)
print("\nBon Voyage!")

# TUPLES
"""
In Python, a value that not be changed is referred to as immutable, and an immutable list is referred to as a 'Tuple'. 
A tuple looks just like a list except it wrapped in a parentheses() rather than square brackets[]. Once you define a 
tuple, you can access individual item's index, just as you would with a regular list.
For example the longitude and latitude on someone's last location, should always be certain, so one can ensure a search 
location for a missing person
"""
location = (350, 40)
print(location[0])
print(location[1])
"""
Note: Tuples are technically defined by the presence of a comma; the parentheses made is just to make them look neater
and more readable. If you want to define a tuple with one element, you need to include a trailing comma:
"""
my_t = (4,)
# Looping through all the value in a tuple
# Looping through a tuple is the same as looping through a list. For example:
print("\nThese are the original coordinates:")
for dimension in location:
    print(dimension)
# We can also write over a tuple. Since tuples can't be modified you can
# however assign new value to its original variable. For example:
location = (70, 30)
print("\nThis are the new coordinates:")
for coordinate in location:
    print(coordinate)


