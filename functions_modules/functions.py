"""
A function is a block of code that are designed to a specific job. For example:
"""


def add_amount(total_cost):
    # Display message
    print(f"Your total is ${total_cost} + $2 VAT")


add_amount(30 + 2)
"""
In this example, the line at line 6 uses the keyword 'def' to inform Python that
you're defining a function. This is the function definition, which tells Python
the name of the function and, if the function applicable, what kind of data 
needs to do its job, in this case we passed the information 'total_cost' as the 
parameter/argument. Finally, the definition ends in a colon.

Any indented lines like on line 7, that follows def and function definition,
def add_amount(): make up the body of the function is called a docstring, which 
describes what the function should perform. Docstrings are enclosed in triple
quotes, which Python looks for when it generates documentation for the functions
in your programs

The line 8, print(f"Your total is ${total_cost} + $2 VAT") is the only line of
code in the body of this function, so add_amount(total_cost) has one task: print
(f"Your total is ${total_cost} + $2 VAT"). When we want to use a function, you 
call it. A function call tells Python tom execute the code in the function. To
call a function, you write the name of the function, follow by the necessary 
information in parentheses, as shown in line 11.
"""

# Passing Argument
"""
Function definitions can have multiple parameters, a function call may need 
multiple arguments. You can pass argument to your functions in a number of ways.
To do so you can use positional arguments, which need to be in the same order 
the parameters were written; keyword arguments, where each argument consists of 
a variable name and a value; and lists and dictionaries of values.
"""
# Positional Argument
"""
When you call a function, Python must match each argument in the function call 
with a parameter in the function definition. The simplest way to do this is 
based on the order of the arguments provided. Values matched up this way are 
called positional arguments. For example:
"""


def total_amount(cost, vat):
    """Display and calculate the total cost of item"""
    print(f"\nThe total cost before VAT: ${cost}")
    print(f"Total amount after VAT: ${cost + vat}")


total_amount(150, 23)  # You can also call a function multiple times as shown
total_amount(230, 40)

# Keyword Arguments
"""
A keyword argument is name-value pair that is passed to a function. One can 
directly associate the name and the value within the argument, so when you pass
the argument to the function, there's no confusion. Keyword arguments free one 
from having to worry about correctly ordering ones arguments in the function 
call, and they clarify the role of each value in the function call. For example:
"""


def population_density(population, area):
    """Calculates and displays the population density in Kiev"""
    print(f"The population density of Kiev is {population / area} people per "
          f"square meter")


population_density(population=3_000_000, area=20000)

# Default Values
"""
When writing a function, you can define a default value for each parameter. If 
an argument for a parameter is provided in the function call, Python uses the 
argument value. If not, it uses the parameter's default value. For example:
"""


def user_profile(name, location="United Kingdom"):
    """Display the user's name and location"""
    print(f"Username: {name.title()}")
    print(f"Location: {location.title()}")


user_profile(name=input("Enter your name: "))
user_profile(name="henry", location="scotland")  # Because an explicit parameter
# for location is provided, Python will ignore the parameter's default value

# Return Values
"""
A function doesn't always have to display its output directly. Instead, it can
process some data and then return a value or sets of values. The value the 
function returns is called the 'return value'. The return statement takes a 
value from inside a function and sends it back to the line that called the 
function. Return values allow you to move much of the program's grunt work into
functions, which simplify the body of your program.
"""


# Returning a Simple Value


def student_record(first_name, middle_name, last_name):
    """Return the full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


student = student_record("john", "phillip", "george")
print(student)
"""
The definition of student_record() takes as parameters a first, middle and last
name at line 107. The function combines these 3 names, add a space between them,
& assigns the results to the full_name variable line 109. The value full_name 
is converted into a title() case, and then returned to the calling line at 110.

When you call a function that returns a value, you need to provide a variable 
that the return value can be assigned to. In the case, the returned value is 
assigned to the variable student at line 113. The output then shows a neatly 
formatted name made up of parts of the student's name
"""

# Making an Argument Optional
"""
Sometimes it makes sense to make an argument/parameter optional so that a user 
using the function can choose to provide extra information only if they want to.
You can use the default values to make an argument optional. For example, say we
to make user_profile() to handle location parameter as an option:
"""


def user_profile(name, age, location=''):
    """Return the user profile data, neatly formatted."""
    if location:
        user = f"\nName: {name.title()}\nAge: {age}" \
               f"\nLocation: {location.title()}"
    else:
        user = f"\nName: {name.title()}\nAge: {age} years old."
    return user.title()


register = user_profile("john", 22, 'Bahamas')
print(register)

register = user_profile("jane", 18)
print(register)
"""Note: When making an argument optional, it is important that the parameter 
you wish to make optional is passed last so python will match the positional 
argument correctly """

# Returning a Dictionary
"""
A function can return any kind of value you need it to, including more 
complicated data structures like list and dictionaries. For example, writing a 
function that takes in a users name, age, sex and location and returns a 
dictionary representing a person:

You can also extend the dictionary to including other pieces of data you want to
store about the user. For example I added occupation at the end of the function
parameter with None as the placeholder, then at line 172 added an if statement 
to see if the placeholder None evaluates as False. If the function call includes
the value for occupation, that value is stored in the dictionary.
"""


def build_person(name, age, sex, location, occupation=None):
    """Return a dictionary of info on a person."""
    person = {'full_name': name, 'age': age, 'gender': sex,
              'location': location}
    if occupation:
        person['occupation'] = occupation
    return person


citizen = build_person("john phillip", 22, "male", "ukraine")
print(citizen)
citizen = build_person("steblina lubov", 23, "female", "ukraine", "logistics")
print(citizen)

# Using a Function with a While Loop
"""Functions can also be used with while loops. For example, lets use the 
build_person function"""


def build_person(name, age, sex, location, occupation=None):
    """Return a dictionary of info on a person."""
    persons = {'full_name': name, 'age': age, 'gender': sex,
               'location': location, 'occupation': occupation}
    return persons


people = []

while True:
    print("\nPlease fill in the information required:")
    print("(enter 'quit' at any time to cancel your registration")

    f_name = input("Enter your full name: ")
    if f_name == "quit":
        break

    f_age = input("Enter your age: ")
    if f_age == "quit":
        break

    f_gender = input("Enter your sex: ")
    if f_gender == "quit":
        break

    f_location = input("Enter your location: ")
    if f_location == "quit":
        break

    f_occupation = input("Enter your occupation: ")
    if f_occupation == "quit":
        break

    individual = build_person(f_name, f_age, f_gender, f_location, f_occupation)
    people.append(individual)

for person in people:
    print(f"{person}")

# Passing a List
"""
Often it is useful to pass a list to a function, whether it's a list of names,
numbers, or more complex objects like dictionaries. When passing a list to a 
function, the function gets direct access to the contents of the list. For 
example: 
Say we have a list of users and want to print a message to each user.
"""


def greet_user(names):
    """Print a simple greeting to the users in the list"""
    for name in names:
        greeting = f"\nHello {name.title()}, welcome to Omnis."
        print(greeting)


username = ["james", "toby", "alexi", "phillip"]
greet_user(username)

# Modifying a List in a Function
"""
When a list is passed into a function, the function can modify the list. Any 
changes made to the list inside the function's body are permanent, allowing you
work efficiently even when you're dealing with large amounts of data.

Consider a company that creates 3D printed models of designs that users submit.
Designs that need to be printed are stored in a list, and after being pulled 
they are moved into a separate list:
"""


def print_models(unprinted_model, completed_model):
    """
    Simulate printing each design, until none are left. Move each design
    to completed_model after printing.
    """
    while unprinted_model:
        current_model = unprinted_model.pop()
        print(f"Printing model: {current_model.title()}")
        completed_model.append(current_model)


def show_completed_models(x):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in x:
        print(model)


unprinted_models = ["Robot hands", "hand gun", "pendant", "car spoiler"]
completed_models = []

print_models(unprinted_models[:], completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
"""
Sometimes you'll want to prevent a function from modifying a list. In this case
, we can address this issue by passing the function a copy of the list, not the
original. Any changes the function makes to the list will affect only the copy
of the list, leaving the original intact.
        You can send a copy of a list to a function like this:
function_name(list_name[:])
    The slice notation [:] make a copy of the list to send to the function. If 
we didn't want to empty the list of unprinted designs in printing_models.py, we
could call the print_models() like this: 

print_models(unprinted_model[:], completed_model)
"""

# Passing an Arbitrary NUmber of Arguments
"""
Sometimes you won't know ahead of time how many arguments a function needs to 
accept. Fortunately, python allows a function to collect an arbitrary number of 
arguments from the calling statement. 

For example, consider a function that builds a car. It need to accept a number 
of options the buyer wants, but you can't know ahead of time how many options
the buyer will want. The function in the following example has one parameter,
*options, but this parameter collects as many arguments as the calling line 
provides:  
"""


def make_car(car_name, *options):
    """Print the list of options that have been requested by the car buyer"""
    print(f"Car model: {car_name.title()}")
    for option in options:
        print(f"- {option}")


make_car("Porsche Taycan", "sport aero", "glass roof", "vegan interior",
         "exposed carbon black body")

# N.B: In the example above we mixed positional and arbitrary arguments

# Using Keyword Arguments
"""
Sometimes you'll want to accept an arbitrary number of arguments, but you won't 
know ahead of time what kind of information will be passed to the function. In 
the case, you can write functions that accept as many key-value pairs as the 
calling statement provides. To do this we use the parameter known as a **Kwargs,
this parameter name is used to collect non-specific keyword arguments.

One example involves building user profiles: you know you'll get information
about a user, but you're not sure what kind of information you'll receive. The 
function build_profile() in the following example always takes in a first and 
last name, but it accepts an arbitrary number of keyword arguments as well;
"""


def build_profiles(name, surname, **user_info):
    """Build a dictionary containing everything we know about the user."""
    user_info['first_name'] = name
    user_info['last_name'] = surname
    return user_info


user_profile = build_profiles('john', 'phillip', age=22, sex='male',
                              ethnicity='nubian')
print(user_profile)

# Storing Your Functions in Modules
"""
One of the advantages of functions is the way they separate blocks of code from
your main program. By using descriptive names for your functions, your main 
program will be much easier to follow.

Storing functions in separate files allows us to hide the details of our 
program's code and focus on its higher-level logic. It also allows for the reuse
of functions in many different programs. When you store a function in a separate
file that file is called a Module and then importing that module into your main
program. An import statement tells Python to make the code in a module available
in the currently running program file. Knowing how to import functions also 
allows one to use libraries of functions that other programmers have written.

    There are also several ways to import a module:
"""
# Importing the Entire Module
"""
To start importing functions, we have to first create a module. A file ending in
.py that contains the code of the function you want to import for example:
builder.py which contain the functions make_car(). Then we will have to create a
separate file in our case module1.py.

The first approach to importing, in which you simply write import followed by 
the name of the module, makes every function from the module available in your 
program. If you use this kind of import statement to import an entire module, 
each function in the module is available through the following syntax:
    import module_name
    
    module_name.function name()
"""

# Importing Specific Functions
"""
To import specific functions from a module use this general syntax:

from module_name import function_name

    You can import as many functions as possible from a module by separating 
each function's name with a comma:

from module_name import function_0, function_1, function_2
"""

# Using as to Give a Function an Alias
"""
If the name of a function you're importing might conflict with an existing name 
in your program or if the function name is long, you can use a short unique 
alias-- an alternative name similar to a nickname for the function. 

The general syntax for providing an alias is:

from module_name import function_name as ph

To call the function use:
alias()
"""

# Using as to Give a Module an Alias
"""
You can also provide an alias for a module name. Giving a module an alias, like
t for time, allows the programmer to call the module's name more quickly. The 
general syntax for this approach is:

import module_name as mn

To call a function in this approach use:
alias.function_name()
"""

# Importing All Functions in a Module
"""
You can tell Python to import every function in a module by using the asterisks
(*) operator. The general syntax for this procedure is:

from module_name import*
"""
