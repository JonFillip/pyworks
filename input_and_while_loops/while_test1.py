"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you'll add that topping to their pizza.
"""
toppings = None
pizza_topping = []
while True:
    toppings = input("Please enter the topping you wish to add: ")
    pizza_topping.append(toppings)
    if toppings == "done":
        break
    else:
        print(f"{toppings.title()} has been added to your pizza.")
# for topping in pizza_topping:
#   print("Here is the list of topping you requested:")
#   print(f"\n{topping}")

"""
7-5. Movie Tickets: A movie theater charges different tickets prices depending
on a  person's age. If a person is under the age of 3, the ticket is free; if 
they are between 3 and 12, the ticket is $10, and if they are over age 12, the 
ticket is $15. Write a loop in which you ask users their age, and then tell them
the cost of their movie ticket
"""
age = None
while True:
    age = input("Please enter your age: ")
    age = int(age)
    if age < 3:
        print("Your movie ticket is Free!")
        break
    elif 3 >= age <= 12:
        print("Your movie ticket costs $10.")
        break
    elif age > 12:
        print("Your movie ticket will cost $15.")
        break

"""
7-7. Write a loop that never ends, and run it.
"""
population = 180000000
while population < 1000000000:
    population += 1
    print(population)
