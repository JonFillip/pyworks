"""
In Python, when handling errors a special object call 'exceptions' are used that
manage errors that might arise during a program's execution. Whenever an error
occurs that might make Python unsure on how to handle the error, it creates an
exception object. If you write code that handles the exception, the program will
continue running. If you don't handle the exception, the program will halt and
show a traceback, which includes a report of the exception that was raised.

    Exceptions are handled with try-except blocks. A try-except block asks
Python to do something, but it also tells Python what to do if an exception is
raised. When you use the try-except block, your programs will keep running even
when things begin to go wrong. Instead of traceback, which can be somethings
confusing for users to read, users will see friendly error messages left by the
programmer.
"""

# Handling the ZeroDivisionError Exception
"""
In Python, you cannot divide a number by zero (0) because it is impossible to 
divide a number by nothing. If you write a piece of code that divides a number 
by zero, it raises an error.

    To mange this type of error from crashing your program, you can create a 
try-except block to handle the exception that might occur. By telling Python to 
run some code, and telling what to do if the code results in a particular kind 
of exception.
    For example, I'll create a simple program that calculates the body mass 
index of the user, asking them for two values; their mass in kg and their height
in m**2
"""

print("Please enter your mass in kg and your height in cm, and you'll get your"
      " BMI")
print("Enter 'quit' to exist program.")

while True:
    height = input("Please enter your height in cm: ")
    if height == "quit":
        break

    mass = input("Please enter your mass in kg: ")
    if mass == "quit":
        break

    try:
        height_meters = float(height) / 100
        BMI = float(mass) / float(height_meters ** 2)
    except ZeroDivisionError:
        print("Sorry you cannot divide by 0!")
    else:
        print(f"Your Body Mass Index is {BMI}kg/m2")

# Handling  the FileNotFoundError Exception
"""
When working with files, one common is the handling of missing files. This error
might be as a result of having the wrong file path, misspelling the name of the
file or calling a file that simply doesn't exists. To handle such exceptions we
can create a try-except block of code.
    For example, I'll try to read a file called vertical_farm.txt but I'm going 
purposely misspell the file name. I'll also write a try-except block that will
handle any exceptions if any arises:
"""
filename = "vertical_farm.txt"

try:
    with open(filename, encoding="utf-8") as file_object:
        content = file_object.read()
    print(content)
except FileNotFoundError:
    print(f"Sorry but {filename} doesnt exist. Please check the spelling of the"
          f"file address or go over the file path again.")

# Analysing Text
"""
You can analyze a file to know more about that file. For example, wanting to 
know how many words or characters are in a file. To do this we can use the 
string split() method, which can build a list of words from a string.
"""

data = "files_and_exceptions/ai_bigdata.txt"

try:
    with open(data, encoding="utf-8") as file_object:
        text = file_object.read()
    print(text)
except FileNotFoundError:
    print(f"Sorry but {data} doesnt exist. Please check the spelling of the"
          f"file address or go over the file path again.")
else:
    # Count the approximate number of words in the data file
    words = text.split()
    num_words = len(words)
    print(f"The file {data} consists of {num_words} words.")

# Working with Multiple Files
"""
Sometimes one might find themselves working with multiple files at once. To do 
so comfortably and efficiently start off by creating a function that contains
the programs try-except block and what you want your code to perform.

For example, replacing the word 'number' to 'quantity' in the files I'll be 
working with:
"""


def replace_word(document):
    """Replace the word 'number' to 'quantity' in a file"""
    try:
        with open(document) as doc_object:
            files = doc_object.readlines()

    except FileNotFoundError:
        print(f"Sorry but {document} doesnt exist. Please check the spelling "
              f"of the file address or go over the file path again.")
    else:
        # Replace the given word in the files
        for line in files:
            print(line.replace("number", "quantity").rstrip())


doc_names = ["vertical_farm.txt", "files_and_exceptions/ai_bigdata.txt",
             "dec.txt"]
for doc_name in doc_names:
    replace_word(doc_name)

# N.B
"""
In some cases when you don't need to report an error. When can allow the program 
to fail silently when an exception occurs and continue as if nothing happened.
To make a program fail silently, you write a try-except block, but inside the 
except block tell Python to do nothing by using the simple syntax called 'pass'.

For example:
"""


def count_word(doc):
    """Count the number of terms in the file."""
    try:
        with open(doc, encoding="utf-8") as file_item:
            text_file = file_item.read()

    except FileNotFoundError:
        pass

    else:
        # Count the approximate number of terms in the data file
        terms = text_file.split()
        word_count = len(terms)
        print(f"The file {doc} consists of {word_count} terms.")


documents = ["vertical_farm.txt",
             "/Users/johnphillip/Desktop/python_work"
             "/files_and_exceptions/ai_bigdata.txt",
             "green_project.pdf"]
for document in documents:
    count_word(document)
