"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up
the code form exercise 6-3 by replacing your series of print() calls with a loop
that runs through the dictionary's keys and values. When you're sure that your
loop works, add five more python terms to your glossary. When you run your
program again, these new words and meanings should automatically be included in
the output.
"""
glossary = {
    'bytecode': 'Compiled programming code that targets a virtual machine'
                ' rather than a specific computer architecture',
    'arrays': 'A collection of elements, each identified by an index',
    'backlog': 'A list of features or technical tasks which the development '
               'team maintains & which are known to be necessary & sufficient '
               'to complete a project or a release',
    'algorithm': 'A step by step procedure to achieve a specific goal',
    'argument': 'A value passed into a function when it is called.',
    'bug': 'An error, flaw, or fault in a computer program',
    'constant': 'A variable that never changes its value',
    'compiler': 'A program that converts code into an executable',
    'loop': 'Piece of code that runs itself repeatedly',
    'method': 'A function that is attached to an object',
    'function': 'A piece of code that does a specific thing',
}
for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(f"\t{meaning}.")

"""
6-5. Rivers: Make a dictionary containing three major rivers and the country 
each river runs through. One key-value might be 'nile': 'egypt'.
1. Use a loop to print a sentence about each river.
2. Use a loop to print each river in the dictionary.
3. Use a loop to print the name of each country included in the dictionary.
"""
rivers = {
    'Nigeria': 'Niger and Benue',
    'Egypt': 'Nile',
    'Brazil': 'Amazon'
}
for country, river in rivers.items():
    print(f"{country}'s major river is the {river} river.")

for river in rivers.values():
    print(f"\n{river}")

for country in rivers.keys():
    print(f"\n{country}")

"""
6-6. Polling: Use the code in favorite_flavor.py
1. Make a list of people who should take the poll. Include some names of people 
already in the dictionary and some that are not.
2. Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding. If they 
have not taken the poll, print a message inviting them to do so.
"""
favorite_flavors = {
    'johnny': 'vanilla',
    'jane': 'salty caramel',
    'igor': 'chocolate',
    'jude': 'vanilla',
    'olga': 'mango',
}
people = ['johnny', 'jane', 'igor', 'jude', 'olga', 'phil', 'anna', 'lyubov']

for person in favorite_flavors.keys():
    if person in people:
        print(f"Hi {person.title()},thank for taking our flavor poll your "
              f"feedback helps us improve the quality of our products.")
for name in set(people) - favorite_flavors.keys():
    print(f"\nHi {name},\nWe are conducting a survey on customers preferred ice-"
          f"cream flavor, we'd love that you help us by answering the survey,"
          f"as your feedback helps us improve the quality of our product.\n"
          f"Stay sweet.")
