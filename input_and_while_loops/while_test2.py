"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of
various sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such as
I made your tuna sandwich. As each sandwich is made, move it to a list of
finished sandwiches. After all the sandwiches are made, print a message listing
each sandwich that was made.
"""
sandwich_orders = ["Tuna", "BBQ", "Hawaii", "vegan"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"Your {sandwich.title()} sandwich is ready!")
while sandwich_orders:
    finished_sandwiches = sandwich_orders[:]
    print(finished_sandwiches)
    break

"""
7-9. No Pastrami: Using the list of sandwich_orders from 7-8, make sure the 
sandwich 'pastrami' appears in the list at least three times. Add code near the 
beginning of your program to print a message saying the deli has run out of 
pastrami, and use the while loop to remove all occurrences of pastrami form the 
sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""
sandwich_orders = ["pastrami", "Tuna", "BBQ", "pastrami", "Hawaii", "vegan",
                   "pastrami"]
finished_sandwiches = []
print("\nSorry but deli has run out of Pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    finished_sandwiches = sandwich_orders[:]
print("\nThese sandwiches are available on the menu:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")

"""
7-10. Dream Vacation: Write a program that polls users about their dreams 
vacation. Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll.
"""

places = []
while True:
    question = input("If you could visit one place in the world, "
                     "where would you go? If you want to opt out type 'quit' ")
    if question == "quit":
        break
    places.append(question)

print("These are the most desirable vacation destinations")
for place in places:
    print(f"\t{place.title()}")
