# Introduction to Lists
"""
A list is a collection of items in a particular order. A list can be made of letters of the alphabet, numbers, names and
attributes. The items of a list don't have to be related in any particular way. Because a list usually contains more
than one element, it's a good idea to make the name of your list plural, such as letters, digits, or names.
In python, square brackets ([]) indicate a list, and individual elements in the lists are separated by commas. For exam-
ple:
"""

space_companies = ["SpaceX", "NASA", "Blue Origin", "Virgin Galactic", "EASA", "Boeing"]
print(space_companies)

"""
When python prints a list notice that it prints the list together with the bracket which is okay but when outputting
the content of a list to a user you should make it outputs without the square brackets. This can be done by accessing 
the elements in the lists
"""

# Accessing Elements in a list
"""
Lists are ordered collection, so one can access any element in a list by telling Python the position, or index, of the 
desired item. To access an element in a list, write the name of the list followed by the index of the item. Also note
that in Python and all programming languages index position always starts at 0, not 1. 
"""
# For example, printing the first item on the space_companies list
print(space_companies[0])  # Prints SpaceX the first item in the list

"""
Python has a special syntax for accessing the last element in a list. By asking for the item index -1, Python always 
returns the last item in the list. For example:
"""
print(space_companies[-1])  # Returns the last item in the list
print(space_companies[-2])  # Returns the second item from the end of the list
print(space_companies[-3])  # Returns the third item at the end of the list, and so forth

# Methods can also be used when dealing with list
print(space_companies[3].upper())

# Using individual values from a list
"""
You can use individual values from a list just as you would any other variable. For example, you can use f-strings to 
create a message based on a value from a list
"""
message = f"My favorite space company is {space_companies[0].lower()}."
print(message)

# Changing, Adding, and Removing Elements
"""
Modifying Elements in a List

Most lists you create will be dynamic, meaning you'll build a list and then add and remove elements from it as your
program runs it course.

The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element,
use the name of the list followed by the index of the element you want to change, and then provide the list new value
you want that item to have. For example we want to modify the first element in the space_companies list:
"""
space_companies[0] = "Star Trek"
print(space_companies)  # This prints out ['Star Trek', 'NASA', 'Blue Origin', 'Virgin Galactic', 'EASA', 'Boeing']

# This can be done with any item in the list as you know its index

# Adding Elements to a list
"""
You might want to add a new element to a list for many reasons. For example, you might to want to make new aliens appear
in a game, add new data to a visualization, or add new registered users to a website you've built. Python provides ways
to add new data to existing lists.
"""
# Appending Elements to the End to a List
"""
The simplest way to append a new element to a list is to use the append() method with new element in the parentheses at 
the end of the list.
"""
space_companies.append("Lockheed Martin")
print(space_companies)  # Prints ['Star Trek', 'NASA', 'Blue Origin', 'Virgin Galactic', 'EASA', 'Boeing',
# 'Lockheed Martin']
"""
The append() method makes it easy to build lists dynamically. It can also be used to be build a list from scratch. For 
example:
"""
planets = []

planets.append("Mars")
planets.append("Mora")
planets.append("Vormir")
planets.append("Nebula")
print(planets)

# Inserting Elements into a list
"""
You can add a new element at any position in your list by using the insert() method. By specifying the index of the new
and the value of the new item. 
"""
space_companies.insert(3, "Cosmos")
print(space_companies)
# ['Star Trek', 'NASA', 'Blue Origin', 'Cosmos', 'Virgin Galactic', 'EASA', 'Boeing', 'Lockheed Martin']
# Removing Elements from a List
"""
Often, you'll want to remove an item or a set of items from a list. For example, when a player shoots down an alien the 
game, you'll want remove it from the list of active aliens. Or when a user decides to cancel their account on a web 
application, or when a user unsubscribe from a mailing list, you'll want to remove that user from the list of active 
users or subscribers. You can remove an item according to its position in the list or according to its value. If you
know the position of the item you want to remove from the list , you can use the 'del' statement in front the list name.
"""
del space_companies[0]  # Note after doing this you will no longer access to this value
print(space_companies)
# ['NASA', 'Blue Origin', 'Cosmos', 'Virgin Galactic', 'EASA', 'Boeing', 'Lockheed Martin']

# Removing an item Using the pop() Method
"""
Sometimes you'll want to use the value of an item you removed from the list. For example, you might want to get the
x and y position of an alien that was shot down, so you can draw an explosion at that position. 
In a web application, you might to want remove the a user from a list of active members and the add that user to a list 
of inactive members. 

The pop() method removes the last item in a list, but it lets you work with that item after removing it. The term pop 
comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the 
top of a stack corresponds to the end of a list.
"""
popped_companies = space_companies.pop()
print(space_companies)  # ['NASA', 'Blue Origin', 'Cosmos', 'Virgin Galactic', 'EASA', 'Boeing']
print(popped_companies)  # Lockheed Martin

"""
We start by defining and printing the list of space companies at line 106. At line 120 we pop a value from the list and 
store that value in the variable popped_companies. We print that list at line 121 to show the value has been removed 
from the list. Then at line 122 we print the popped value to prove that we still have access to the value that was re-
moved

The output at line 121 shows that the value 'lockheed Martin' was removed from the end of the list and is now assigned 
to the variable popped_companies.  
"""
"""
How might this pop() method be useful? Imagine that the space_companies in the list are stored in chronological order 
according to when they were applied to a government contract and only the first six companies that are applied are 
considered and you want to show that the last company that registered was no longer considered. If this is the case, we 
could use the pop() method to print a statement about the company that wasn't considered for the contract.  
"""
print(f"After much debate in the pentagon, it was decided that {popped_companies} would not be amongst the candidates "
      f"considered for the contract ")
# After much debate in the pentagon, it was decided that Lockheed Martin would not be amongst the candidates considered
# for the contract

# Popping Items from any position in a list
"""
You can use the pop() method to remove an item from any position in a list by including the index of the item you want 
to remove in parentheses
"""
print(planets)  # ['Mars', 'Mora', 'Vormir', 'Nebula']
popped_planets = planets.pop(-2)
print(f"The soul stone is kept in {popped_planets}.")  # The soul stone is kept in Vormir.

"""
If you're unsure whether to use the del statement or the pop() method, here's a simple way to decide: when you want to
delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you 
remove it, use the pop() method.
"""
space_companies.remove("NASA")
print(space_companies)  # ['Blue Origin', 'Cosmos', 'Virgin Galactic', 'EASA', 'Boeing']

"""
You can also use the remove() method to work with a value that's being removed from a list.
"""
print(space_companies)
largest_company = "Boeing"
space_companies.remove(largest_company)
print(space_companies)  # ['Blue Origin', 'Cosmos', 'Virgin Galactic', 'EASA']
print(f"\n{largest_company} is one of the largest aerospace companies in the world")

"""
After defining the list at line 164, we assign the value 'Boeing' to a variable called largest_company at line 165. We 
then use the variable to tell Python which value to remove from the list at line 166. At line 168 the value 'Boeing' has
removed from the list but is still accessible through the variable largest_company, allowing us to print a statement
about why we removed 'Boeing' from the list of space_companies

['Blue Origin', 'Cosmos', 'Virgin Galactic', 'EASA', 'Boeing']
['Blue Origin', 'Cosmos', 'Virgin Galactic', 'EASA']

Boeing is one of the largest aerospace companies in the world
"""
# The remove() method deletes only the first occurrence of the value you specify. If there is a possibility the value
# appears more than once in the list,you'll need to use a loop to make sure that all occurrence of the value are removed

# ORGANIZING A LIST
# Sorting a list Permanently with the sort() Method
"""
Python's sort() method makes it relatively easy to sort a list. Imagine we have a list of cars and want to change the 
order of the store them alphabetically. To keep the task simple, let's assume that all the values are in the list are in
lowercase.
"""
countries = ["sweden", "netherlands", "ukraine", "nigeria"]
countries.sort()
print(countries)  # ['netherlands', 'nigeria', 'sweden', 'ukraine']
# The sort() method, shown in line 192, changes the order of the list permanently. The countries list are now displayed
# In alphabetical order, and can never be reverted to its original order
"""
You can also sort a list in a reverse alphabetical order by passing the argument 'reverse=True' to the sort() method. 
For example: 
"""
countries.sort(reverse=True)
print(countries)  # ['ukraine', 'sweden', 'nigeria', 'netherlands'] again the order of the list has been permanently
# changed

# Sorting a list temporarily with the sorted() Function
"""
To maintain the original order of a list but present it in a sorted order, the sorted() function can be used. 
The sorted() function lets you display your list in a particular order but doesn't affect the actual order of the list.
For example:
"""
dogs = ["corgie", "greyhound", "doberman", "german shepperd"]

print("This is the original list:")
print(dogs)
# This is the original list:
# ['corgie', 'greyhound', 'doberman', 'german shepperd']

print("\nThis is the sorted list:")
print(sorted(dogs))
# This is the sorted list:
# ['corgie', 'doberman', 'german shepperd', 'greyhound']

print("\nHere is the original list again:")
print(dogs)
# Here is the original list again:
# ['corgie', 'greyhound', 'doberman', 'german shepperd']
# The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical
# order. For example
print(sorted(dogs, reverse=True))
"""
NOTE:Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several
ways to interpret capital letters when determining a sort order, and specifying the exact order can be complex. 
"""

# Printing a List in Reverse Order
"""
To reverse the original order of a list, one can use the reverse() method. If we originally stored the list of dogs in 
chronological order according to when we owned them, we could easily rearrange the list into reverse chronological order
"""
dogs.reverse()
print(dogs)  # ['german shepperd', 'doberman', 'greyhound', 'corgie']
# Notice that the reverse() method doesn't sort backwards alphabetically; but reverses the order of the list
"""
The reverse() method changes the list permanently, but you can revert to the original order anytime by applying reverse()
to the same list a second time.
"""
# FINDING THE LENGTH OF A LIST
# To find the length of a list, simply use the len() function. For example:
print(len(countries))
# 4
print(len(space_companies))
# 4
print(len(dogs))
# 4

"""
The len() function is useful when you need to quantify the number of characters that are in a game, determine the amount
of data you have to manage in a visualization, or figure out the number of registered users on a website and so on.

NOTE: Python counts the items in a list starting with one, so you shouldn't run into any off-by-one errors when determi-
ing the length of a list.
"""

# AVOIDING INDEX ERRORS WHEN WORKING WITH LISTS

"""
One type of common error when working with list for the first time is the index error. For instance, lets say you have a 
list with four items in it, and you ask for a fifth item: 
"""
# print(dogs[4])
"""
We get this error message in run console:
Traceback (most recent call last):
  File "/Users/johnphillip/PycharmProjects/python_work/lists.py", line 269, in <module>
    print(dogs[4])
IndexError: list index out of range

Python will attempt to give us the item at index 4. But when it searches the list, no item in dogs has the index 4. 
Because of the off-by-one nature of indexing in lists, this error is typical. People think the forth item is item number
4, because they start counting at 1, but in  python like most programming languages items in a list or dictionary starts
indexing from 0.

An index error means python can't find an item at the index you requested. If an index error occurs in your program, try
adjusting the index you're requesting by one and run the program again to see if the results are correct. Or if an index
error occurs and you can't figure out how to resolve it, try printing your list or just printing the length of the list.
Your list might look much different than you thought it did, especially if it has been managed dynamically by your pro
-gram. Seeing the actual list, or the exact number of items in your list, can help you sort out such logical errors.
"""












