"""
Python's if statements allows us to examine a set of conditions in a program
and decide which action to take based on those conditions. For example, setting
the thermostat in a room relative to outside temperatures.
"""
temperatures = (9, 10, 11, 12, 13, 14)  # outside temperature
for temperature in temperatures:
    if temperature == 9:
        print(f"The temperature outside is {temperature} degrees celsius,"
              f" setting room temp to 26 degrees celsius.")
    else:
        print(f"The temperature outside is {temperature} degrees celsius"
              f",the room temperature is set to 23 degrees celsius.")
"""
The loop in this example first checks if the current value of the temperature 
is 9. If it is, the thermostat sets the room temperature to 26 degrees. If the 
outside temperature is anything other than 9, it sets the room temps to 23 
degrees
"""

# CONDITIONAL TEST
"""
At the heart of every if statement is an expression that can be evaluated as 
True or False and is called a 'conditional test'. Python uses the values True 
or False to decide whether the code in an if statement should be executed.
"""
# Checking for equality
"""
Most conditional tests compare the current value of a variable to a specific
value of interest. The simplest conditional test checks whether the value of a 
variable is equal to the value of interest: 
"""
password = "New_password668"
print(password == "New_password668")  # True
# When the password is anything other than 'New_password668', the test will run
# False:
print(password == "Hello1998")  # False
"""
IGNORING CASE WHEN CHECKING FOR EQUALITY
Testing for equality is case sensitive in python. For example, two value with 
different capitalization are not considered equal:
"""
print(password == "new_password668")  # The result is False
"""
If case matter, this behaviour is advantageous. But is case doesn't matter and 
instead test the value of a variable, you can convert the variable's value to
lowercase before doing the comparision.
"""
print(password.lower() == "new_password668")  # True

# Checking for Inequality
"""
When you want to determine whether two values are not equal, you can combine an
exclamation point and an equal sign (!=). The exclamation point represent 'not'
as it does in many programming languages. For example:
"""
order = "Chicken wings"
if order != "Chicken burger":
    print("Wrong order!")

# Checking Multiple Conditions
"""
To check multiple conditions at the same time two keywords are and & or can be 
used in these situations. 
"""
# Using 'and' to check Multiple Conditions
"""
To check whether two or more conditions are both True simultaneously, use the 
keyword 'and' to combine the two conditional tests. If each test passes, the 
overall expression evaluates to True. If either of the test fails or if both 
tests fails, the expression evaluates to False.
"""
legal_age = 18
region = "ukraine"
if legal_age >= 18 and region == "ukraine":
    print("Welcome CodeHub!")  # Welcome CodeHub!

# Using 'or' to check Multiple Conditions
"""
The keyword 'or' allows you to check multiple conditions as well, but it passes
when either or both of the individual test pass. An 'or' expression fails only
when both individual tests fail.
"""
age_limit = 18
regions = ["ukraine", "russia", "canada", "china", "south korea", "japan"]
if age_limit >= 18 or region[0:]:
    print("Welcome to Anonymous!")

# Checking whether a value is in a list
"""
To find out whether a particular item is already in a list,use the keyword 'in'
.This comes in when you want to check whether a username already exists in a 
of current usernames before completing someone's registration on a website. In
a mapping project, you might want to check whether a submitted location already
exists in a list of known locations. 
"""
usernames = ["maryjane", "jonnnyboi", "alina_love", "lovlyluu", "phillip"]
username = "Peter"

if username in usernames:
    print(f"Username already taken! Choose another username.")
else:
    print("You may continue your registration")
# The result will be False, because the username peter does not exist in the
# username list

# Checking Whether a Value Is Not in a List
"""
Other times, it's important to know if a value does not appear in a list. You 
can use the keyword 'not'. For example, consider a list of items that are 
banned from entering a country:
"""
banned_items = ["mango", "dragon fruit", "cocaine", "tomatoes", "alcohol"]
item = "cookies"

if item not in banned_items:
    print(f"{item.title()} not prohibited, traveller can bring in item")
else:
    print(f"{item.title()} is prohibited to travel with.")

# Boolean Expressions
"""
A Boolean expression is just another value for a conditional test. A Boolean
value is either True or False, just like the value of a conditional expression
after it has been evaluated.
Boolean values are often used to keep track of certain conditions, such as 
whether a game is running or whether a user can edit certain content on a 
website or whether a device is on:
"""
camera_active = True
can_edit = False
user_active = True

# Boolean values provide an efficient way to track the state of a program or a
# particular condition that is important in your program
