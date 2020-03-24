"""
Most programs are written to solve an end user's problem. To do so, you need to
get some information from the user. To do that you'll need to use the input()
function to allow the user enter information into the program. You'll also use
python's while loop to keep the programs running as long as certain conditions
remain True.
"""

# How the input() Function Works
"""
The input() function pauses your program and waits for the user to enter some 
text. The input() function takes one argument: the prompt, or instruction that 
display to the user so they know what to do. Once python receives the user's 
input, it assigns that input to a variable to make it convenient for you to 
work with. Each time you use the input() function, you should include a clear,
easy-to-follow prompt that tells the user exactly what kind of information is 
needed from the user. For example:  
"""
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# To print a prompt over one line, use the operator += , This takes the string
# that was assigned to prompt and adds the new string onto the end. For example:
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"Hello, have you met {name}, he's new to tik-tok.")

# Using int() to Accept Numerical Input
"""
When you use the input() function, Python interprets everything the user enters
as a string. But when trying accept numerical values you can use the int() or 
float() functions. The int() and float() functions converts a string representa-
tion of a number to a numerical representation.
"""
population = input("What is the population of Nigeria? ")
population = float(population)
if population >= 180_000_000:
    print(True)
else:
    print(False)

# The Modulo Operator
"""
A useful tool for working with numerical information is the modulo operator (%)
, which divides one number by another number and returns the remainder.
"""
print(4 % 3)
print(7 % 3)
"""
The modulo operator does not specify how many times one number fits into 
another number; it only tells us the remainder.

When one number is divisible by another number, the remainder is 0, so the 
modulo operator always returns 0. You can use this fact to determine if a number
is even or odd:
"""
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd")
