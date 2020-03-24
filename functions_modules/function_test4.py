"""
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""


def show_messages(messages):
    """Print a the messages in the list"""
    for message in messages:
        print("\nYou have a new message in the mail;")
        read = f"{message}"
        print(read)


texts = [
    "Hey dear, please can you pick up my dress at the airport",
    "Hey John! Are you coming to university today?",
    "Hey Phillip,\nPlease be in the office by 15:00"
]
show_messages(texts)

"""
8-10. Sending Messages: Start with a copy of your program from exercise 8-9. 
Write a function called send_messages() that prints each text messages and moves
each message to a new list called sent_messages as it's printed. After calling 
the function, print both of your lists to make sure the messages were moved 
correctly.

8-11. Archived Messages: Start with your work from exercise 8-10. Call the 
function send_messages() with a copy of the list of messages. After calling the 
function, print both of your lists to show that the original list has retained
its messages.
"""


def show_messages(unsent_messages, sent_messages):
    """
    Send a copy of each message and move each sent message to sent_message after
    printing.
    """
    while unsent_messages:
        sending_message = unsent_messages.pop()
        print(f"Sending message:\n{sending_message}")
        sent_messages.append(sending_message)


def show_sent_messages(sent_messages):
    """Show all sent messages."""
    print(f"\nThe following message has been sent to recipient:")
    for message in sent_messages:
        print(f"\n{message}")


unsent_messages = [
    "Hey dear, please can you pick up my dress at the airport",
    "Hey John! Are you coming to university today?",
    "Hey Phillip, Please be in the office by 15:00"
]
sent_messages = []

show_messages(unsent_messages[:], sent_messages)
show_sent_messages(sent_messages)
