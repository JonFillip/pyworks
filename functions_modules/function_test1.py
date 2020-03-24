"""
8-1. Message: Write a function called display_message() that prints one sentence
telling  everyone what you are language you are learning right now. Call the
function, and make sure the message displays correctly.
"""


def displayed_message(message):
    """Take a poll on which programming language a user is learning"""
    print(f"User is currently learning {message.title()}.")


displayed_message(input("What programming language are you"
                        " currently learning? "))
"""
8-2. Favorite book: Write a function called favorite_book() that accepts one 
parameter, title. The function should print a message. Call the function, make 
sure the a book title as an argument in the function call.
"""


def favorite_book(title):
    """Ask the user for their favorite book title and print it"""
    print(f"My favorite book is {title.title()}")


favorite_book(input("What is the name of your favorite book? "))
