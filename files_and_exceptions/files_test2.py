"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write a name to a file called guest.txt.
"""
filename = "/Users/johnphillip/Desktop/python_work/files_and_exceptions/guest" \
           ".txt "
guest = input("Please enter your full name: ")
with open(filename, 'w') as guest_list:
    guest_list.write(f"{guest}\n")

with open(filename, 'r') as file_object:
    guests = file_object.read()
print(guests)

"""
10-4. Guest book: Write a while loop that prompts users for their names. When 
the user enters their name, print a greeting to the screen and add a line record
-ing their visit in a file called guest_book.txt. Make sure each entry appears 
on a new line in the file.
"""
visitor_list = "files_and_exceptions/guest_book.txt"

print("Enter 'Done' to quit program.")
while True:
    guest_name = input("Please enter your full name: ")
    if guest_name == "done":
        break
    else:
        with open(visitor_list, 'a') as guest_list:
            guest_list.write(f"{guest_name}\n")
        print(f"Welcome {guest_name}, you've been added to the guest list. "
              f"Enjoy your stay.")

with open(visitor_list) as book:
    lines = book.readlines()

for line in lines:
    print(line)

"""
10-5. Programming Poll: Write a while loop that asks people why they love 
programming. Each time someone enters a reason, add their reason to a file that
stores all the responses.
"""
language_poll = "files_and_exceptions/programming_poll.txt"

print("Enter 'quit' to exit poll.")
while True:
    poll = input("Why do you like programming? ")
    if poll == "quit":
        break
    else:
        with open(language_poll, 'a') as survey:
            survey.write(f"{poll}\n")
        print("Thank you for taking part in our survey!")
