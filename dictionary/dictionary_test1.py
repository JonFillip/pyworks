"""
6-1. Person: Use a dictionary to store information about the person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age and city. Print each piece
of information stored in your dictionary.
"""
person = {'first name': 'Lyubov', 'last name': 'Steblina', 'age': 23,
          'city': 'Kiev'}
print(person)

"""
6-2. Favorite numbers: Use a dictionary to store people's favorite numbers. 
Think of five names, and use them as keys in your dictionary.Think of a favorite
favorite number for each person in the dictionary. Print each person's name and 
their favorite number.
"""
favorite_number = {
    'tansi': 8,
    'emmanuel': 19,
    'toby': 5,
    'vlad': 0,
    'mark': 6,
}
numb1 = favorite_number['tansi']
print(f"Tansi's favorite number is {numb1}")

numb2 = favorite_number['emmanuel']
print(f"\nEmmanuel's favorite number is {numb2}")

numb3 = favorite_number['toby']
print(f"\nToby's favorite number is {numb3}")

numb4 = favorite_number['vlad']
print(f"\nVlad's favorite number is {numb4}")

numb5 = favorite_number['mark']
print(f"\nMarks's favorite number is {numb5}")
print(favorite_number)

"""
6-3. Glossary: A python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let's call it a glossary.
1. Think of five programming words you know. Use these words as the keys in your
glossary, and store their meanings as values.
2. Print each word and it's meaning as neatly formatted output. 
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
print(f"Bytecode:\n{glossary['bytecode']}")
print(f"Array:\n{glossary['arrays']}")
print(f"Backlog:\n{glossary['backlog']}")
print(f"Algorithm:\n{glossary['algorithm']}")
print(f"Function:\n{glossary['function']}")
