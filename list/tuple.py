"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a
tuple.
1. Use a for loop to print each food the restaurant offers.
2. Try to modify one of the items, and make sure that Python rejects the change.
3. The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple,
and then use a for loop to print each of the items in the revised menu.
"""
buffet = ("Burger", "Soup", "Pie", "Pizza", "BBQ")
print("This is the list of foods offered in the buffet:")
for food in buffet:
    print(food)
print("\nBon appetite!")


# 3
buffet = ("Burger", "Shrimps", "Pie", "Sushi", "BBQ")
print("\nThis is the updated buffet menu:")
for food in buffet:
    print(food)
print("Enjoy your meal!")

