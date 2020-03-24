"""
3-1 Names: Store the name of a few names of a few of your friends in a list called names. Print each person's name by
accessing each element in the list, one at a time.
"""

names = ["Alex", "Igor", "Sasha", "Tansi", "Toby", "Lyubov", "Joshua"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])

"""
3-2 Greetings: Start with the list you used in exercise 3-1, but instead of just printing each person's name, print a
message to them. The next of each message should be the same, but each message should be personalized with the person's 
name.
"""
greeting = f"Hi {names[-7].title()}, hope you're going great. Would you be coming to this year's reunion?"
print(greeting)

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that 
stores several examples. Use your list to print a series of statements about these items.
"""
cars = ["Bugatti", "Aston Martin", "Porsche", "Mercedes Benz", "Tesla"]

bugatti = f"The fastest car in the world is the {cars[0]} chiron super sport."
print(bugatti)

aston = f"I fell in love with {cars[1]} after seeing the DB10 in a James Bond movie"
print(aston)

porsche = f"The {cars[2]} Taycan Turbo S is probably my favorite car in the world right now."
print(porsche)

mercedes = f"The {cars[3]} F1 team is my favorite formula one team period."
print(mercedes)

tesla = f"{cars[-1]} roadster 2 is the holy grail of hyper cars"
print(tesla)












