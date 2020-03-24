"""
3-8. Seeing the world: Think of at least five places in the world you'd like to visit.
"""
# Store the locations in a list. Make sure they are not in alphabetical order.
locations = ["namibia", "japan", "switzerland", "italy", "greece", "zanzibar"]
print(locations)
# Use the sorted() function to print the list in alphabetical order without modifying the actual list.
print(sorted(locations))
# Show that your list is still in its original order by printing again
print("\nHere is the actual list:")
print(locations)
# Use the sorted() function to print the list in reverse alphabetical order without altering the original list
reversed_list = sorted(locations, reverse=True)
print("\nThis is the temporary reversed list:")
print(reversed_list)
# Show that your list is still in its original order by printing it again
print("\nHere is the actual list again:")
print(locations)
# Use reverse() method to change the order of the list, print it to show that the order has changed
locations.reverse()
print(locations)
# Use the reverse() method to change the order of your list again. Print the list to show its back to its original state
locations.reverse()
print(locations)
# Use the sort() method to change the list so it's stored in alphabetical order
locations.sort()
print(locations)
# Use the sort() method to change the list so it's stored in reverse alphabetical order
locations.sort(reverse=True)
print(locations)

"""
3-9. Working with one of the program from from exercise 3-4 (listex.py), use the len() function to print a message 
indicating the number of guest you are inviting to the dinner.
"""
guests = ['Bill Gates', 'Burna Boy', 'Lyubov', 'Elon Musk', 'Mark Joshua', 'Jeff Bezos', 'Mum', 'John Eagleton']
print(f"\nI've invited {len(guests)} to dinner.")




