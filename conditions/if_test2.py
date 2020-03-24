"""
5-8. Hello Admin: Make a list of five or more usernames, including then name
'admin'. Imagine you are writing code that will print a greeting to each user:
1. If the username is 'admin', print a message, such as Hello admin, would you
like to see a status report?
2. Otherwise, print a generic greeting, such as Hello Jaden, thank you for
jogging in again.

5-9. No Users: Add an if test to check if the list is not empty.
3. If the list is empty, print the message stating no users available
4. Remove all users from the list to ensure the message is printed
"""
usernames = ["editor", "manger", "admin", "QA", "owner"]
for name in usernames:
    if name == "admin":
        print(f"Hello Admin, would you like to view status report?")
    else:
        print(f"Hello {name.title()}, you have new messages in your mail.")


if usernames:
    for name in usernames:
        print(f"Verifying {name.title()} account")
    print("\nAccounts verified")
else:
    print("No users available, please register user accounts")

"""
5-10. Checking usernames: Do the following to create a program that simulates 
how a website ensure that everyone has a unique username.
1. make a list of five or more usernames called current_users.
2. Make another list of five usernames called new_users. Make sure one or two of
the new usernames are also in the current users list.
3. Loop through the new_users list to see if each new username has already been
used. If it has, print a message telling the user that the name has been taken 
and should try something else. If not, print a message telling the username is 
available.
4. Make sure your comparision is case sensitive. if John has been used JOHN 
should not be accepted. 
"""
current_users = ["Amelia", "John", "Mary", "Henry", "Phillip", "Anna", "Trump"]
current_users_lower = [user.lower() for user in current_users]

new_users = ["Draco", "Drake", "mary", "john", "diana"]
for username in new_users:
    if username.lower() in current_users_lower:
        print("Username unavailable! Please enter another username: ")
    else:
        print("Username available! Continue your registration.")

"""
5-11. Ordinal numbers: Ordinal numbers indicate their position in a list, such
as 1st and 2nd. Most ordinal numbers end in th, except 1, 2 and 3.
1. Store the numbers 1 to 9 in a list
2. Loop through the list
3. Use an if-elif-else chain in the loop to print the proper ordinal ending for
each number. Your output should read "1st, 2nd, 3rd .... 9th" and each output 
should be on a separate line.  
"""
numbers = []
for number in range(1, 10):
    numbers.append(number)
    print(number)
for position in numbers:
    if position == 1:
        print("1st")
    elif position == 2:
        print("2nd")
    elif position == 3:
        print("3rd")
    else:
        print(f"{position}th")
