# Testing a Function
# To begin testing a function I'll begin writing a simple function that returns
# a neatly formatted full name of the user


def get_fullname(first_name, last_name, middle_name=''):
    """Return a neatly formatted fullname of the user by adding the first and
    last name"""
    if middle_name:
        fullname = f"{first_name} {middle_name} {last_name}"
    else:
        fullname = f"{first_name} {last_name}"

    return fullname.title()
