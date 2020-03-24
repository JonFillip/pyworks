"""
An if-else block is similar to a simple if statement, bout the else statement
allows you to define an action or set of actions that are executed when the
conditional test fails
"""
player = "Active"
if player == "Active":
    print("Player is online")
else:
    print("Player offline")

# If-elif-else chain
"""
Often, you'll need to test more than two possible situations, and to evaluate 
these you can use python's if-elif-else syntax. Python executes only one block 
in an if-elif-else chain. It runs each conditional test in order until one 
passes. When a test passes, the code following that test is executed and Python
skips the rest of the tests.

For example,consider a metro station that charges different rates for different
age groups:
1. Rides for minors under age 5 is free
2. Rides for minors age 5 to 18 is $2.
3. Rides for minors age 5 to 18 with a student card is free.
4. Rides for adults age 18 to 50 is $2.
5. Rides for pensioners age 50 above is free. 
"""
minor_age = 6

adult_age = 19

pensioner_age = 50

has_student_card = True

disabled = True
pensioner = True

if minor_age < 5:
    print("The ride fare is free for minors under the age of 5")
elif minor_age <= 18:
    print("The ride fare is $2")
elif minor_age <= 18 and has_student_card is True:
    print("The ride fare is free!")
elif minor_age <= 18 and has_student_card is not True:
    print("The ride fare is $2")
elif adult_age <= 49 and disabled is False:
    print("The ride fare is $2")
elif pensioner_age >= 50 and pensioner is True:
    print("Your ride is free!")
elif pensioner_age >= 50 or pensioner is True:
    print("Your ride is free")
else:
    print("STOP!")

# Testing multiple conditions
"""
The if-elif-else chain is appropriate when trying to test for one possible 
condition at time to pass. As soon as  python find one test passed it skips the
rest of the tests. Though this behaviour is beneficial, because its efficient 
and allows you to test for one specific condition.

However, sometimes it's important to check all the conditions of interest in a
list of conditions as to one specific condition. In this case one could use a 
series of if statements with no elif or else blocks. This techniques makes 
sense when more than one condition could be True, and want to act on every 
condition that is True. Let's take for example the previous code for the metro
station ride:
"""
minor_age = 6

adult_age = 19

pensioner_age = 50

has_student_card = True

disabled = True
pensioner = True

if minor_age < 5:
    print("\nThe ride fare is free for minors under the age of 5")
if minor_age <= 18:
    print("\nThe ride fare is $2")
if minor_age <= 18 and has_student_card is True:
    print("\nThe ride fare is free!")
if minor_age <= 18 and has_student_card is not True:
    print("\nThe ride fare is $2")
if adult_age <= 49 and disabled is False:
    print("\nThe ride fare is $2")
if pensioner_age >= 50 and pensioner is True:
    print("\nYour ride is free!")
if pensioner_age >= 50 or pensioner is True:
    print("\nYour ride is free")

# USING IF STATEMENTS WITH LISTS
# Checking for special items
"""
We can do interesting work when we combine list and if statements to watch for 
special values that need to be treated differently than other values in the list
It helps manage changing conditions efficiently, such as the availability of an
item in a shopping cart.
"""
shopping_cart = ["iPhone", "iPhone case", "apple watch", "macbook pro"]

for item in shopping_cart:
    if item == "macbook pro":
        print("Macbook pro to be shipping in 3 weeks.")
    else:
        print(f"{item.title()} to be delivered tomorrow.")

print("\nYou will be notified via email when your items head out for shipping")

# Checking That a List Is Not Empty
"""
In most real world scenarios we will be able to assume the content of a list,
because we will need to work with user input, making more reasonable to check
if the list is empty before running a for loop.

For example checking whether a list of food order is empty before building the 
order cart. If the list is empty, we'll prompt the user to make input what they
want to eat and add it to the order cart
"""
food_cart = []

if food_cart:
    for food in food_cart:
        print(f"Adding {food}.")
    print(f"Your order is: {food_cart}")
else:
    print("Your cart is empty, continue to menu.")

# Using Multiple Lists
"""
Sometime in real world scenarios we might need to compare two or lists to check 
for specific elements that are common in both list. For example, a shop or 
restaurant will have a menu and when a customer request an item or meal you'll
want to make that what the customer ordered is in the list of items provided by 
the restaurant or store. For example
"""
available_skateboards = ["long-board", "electric board", "diamond board",
                         "short-board", "wooden board", "saint laurent board",
                         "supreme board"]
requested_skateboards = ["long-board", "saint laurent board", "supreme board"]

for skateboard in requested_skateboards:
    if skateboard in available_skateboards:
        print(f"{skateboard} added to shopping cart.")
    else:
        print(f"Sorry, but {skateboard} not found in search.")
print("\nReady to check out.")

# compare two list case insensitive
"""
To compare two lists in Python is easy with build in functions or list 
comprehensions. The more difficult problems is to compare two lists case 
insensitive. The first example is finding the missing elements between two list 
without taking into account the case of the words:
"""
countries1 = ['Brazil', 'Italy', 'Egypt', 'Canada', 'China', 'Panama', 'Mexico']
countries2 = ['Cuba', 'Brazil', 'ItalY', 'Egypt', 'canada', 'China', 'Australia']

missing = []
countries1_lower = [x.lower() for x in countries1]
for country in countries2:
    if country.lower() not in countries1_lower:
        missing.append(country)
print(missing)

# The second example shows how to find the intersection of the two lists case
# insensitive:
countries1 = ['Brazil', 'Italy', 'Egypt', 'Canada', 'China', 'Panama', 'Mexico']
countries2 = ['Cuba', 'Brazil', 'ItalY', 'Egypt', 'canada', 'China', 'Australia']

missing = []
d = [x.lower() for x in countries1]
for m in countries2:
    if m.lower() in d:
        missing.append(m)
print(missing)

"""
The last example do the same: case-insensitive comparison of two lists but this 
time using dictionaries in order to show the matches between the two lists as a 
couples:
"""
countries1 = ['Brazil', 'Italy', 'Egypt', 'Canada', 'China', 'Panama', 'Mexico']
countries2 = ['Cuba', 'Brazil', 'ItalY', 'Egypt', 'canada', 'China', 'Australia']

d1 = {v.lower(): v for v in countries1}
d2 = {v.lower(): v for v in countries2}

k1 = set(d1.keys())
k2 = set(d2.keys())
common_keys = set(k1).intersection(set(k2))

for key in common_keys:
    if d1[key] != d2[key] :
        print(key + ":" + str(d2[key]) + " match " + str(d1[key]))

