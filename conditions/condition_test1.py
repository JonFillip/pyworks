"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test.
"""
location = "London"
print("Is location == 'London'? I predict True.")
print(location == "London")

print("If location == 'Manchester', I predict False")
print(location == "Manchester")

user_online = "Active"
print("If user_online == 'Active', I predict True")
print(user_online == "Active")

print("If user_online == 'Away', I predict False")
print(user_online == "Away")

username = "Taken"
print("If username == 'Taken', I predict True")
print(username == "Taken")

print("If username == 'Not taken', I predict False")
print(username == "Not taken")

"""
5-2. More conditional tests: You don't have to limit the number of tests you 
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_test.py. Have at least one True and one False result for 
each of the following:
a. Test for equality and inequality with strings
b. Tests using the lower() method
c. Numerical tests involving equality and inequality, greater than and less 
than, greater than or equal to, and less than or equal to.
d. Test using the and keyword and the or keyword
e. Test whether an item is in a list
f. Test whether an item is not in a list
"""
# Equality Test
literature = "A+"
if literature == "A+":
    print("Excellent!")
# Inequality Test
new_student = "Mark"
if new_student != "Sara":
    print("Not new student")
# Test using the lower() method
crush = "Me"
print(crush.lower() == "me")
# Numerical test
incline = 30
decline = 60
if incline <= 30 and decline >= 60:
    print("Road is drivable.")
else:
    print("Road conditions not drivable")
# Numerical conditional test
numb1 = 2 ** 2
numb2 = 2 + 2
print(numb2 == numb1)
print(numb1 != numb2)

# And & Or test
price = 50
item = "Arduino"
available = False
if price <= 50 and item == "Arduino" and available is True:
    print(f"{item.title()} has been added to my shopping cart")
else:
    print("This item is not available at the moment")
# Or Keyword
region = "United States"
age_permit = 18
if region != "United States" or age_permit < 18:
    print("404 Error!")
else:
    print("Welcome to USA Today!")
# in or not in a list
subjects = ["Physics", "Maths", "Chemistry", "Machine learning", "Algorithms"]
subject = "Statistics"
if subject in subjects:
    print(f"{subject} is available this semester.")
elif subject not in subjects:
    print(f"{subject} not available this semester.")
