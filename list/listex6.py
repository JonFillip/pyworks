"""
4-10. Using one of the programs you wrote in this chapter, add several line to the end of the program that do the follow
-ing:
1. Print the message 'The first three items in the list are:'. Then use a slice to print the first three items from that
program's list.
2. Print the message 'Three items in the middle of the list are:'. Use a slice to print three items from the middle of
the list.
3. Print the message 'The last three items in the list are:' Use the slice print the last three items in the list
"""
gamers = ["Thor", "Ninja", "Keem", "Toby_One", "Kimberly", "Cara"]
print("The first three items in the list are:")
for item in gamers[0:3]:
    print(item)

# 2
print("\nThree items in the middle of the list are:")
for item in gamers[2:5]:
    print(item)

# 3
print("\nThe last three items in the list are:")
for item in gamers[-3:]:
    print(item)

"""
4-11. My Pizzas, Your Pizzas: Start with your program from listex4.py. Make a copy of the list of pizzas, and call it 
friend_pizzas. Then, do the following:
1. Add a new pizza to the original list
2. Add a different pizza to the list friend_pizzas.
3. Prove that you have two separate lists. Print the message 'My favorite pizzas are:', and then use a for loop to print
the first list. Print the message 'My friend's pizzas are:', and then use a for loop to print the second list.
"""
# 1
my_pizzas = ["BBQ", "Hawaii", "Texas", "Italian", "Philadelphia"]
friend_pizzas = my_pizzas[:]
print(my_pizzas)
print(friend_pizzas)

# 2
my_pizzas.append("Salmon")
friend_pizzas.append("Vegan")

# 3
# My_pizzas
print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nAnd now you know my favorite pizzas.")

# Friend_pizzas
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
print("\nAnd now you know my friend's favorite pizzas")

