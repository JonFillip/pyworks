from random import randint
from random import choice

"""
9-13.Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number between
1 and the number of sides the die has. Make a 6 sided die and roll it 10 times.
"""


class Die:
    """Model a of 6 sided dice and rollin simulation"""

    def __init__(self, sides=6):
        """Initiate the attribute"""
        self.sides = sides

    def roll_die(self):
        """Simulate the rolling of the die and print a random number"""
        return randint(1, self.sides)


my_6dice = Die()
# Roll a 6 sided die 10 times
results = []
for roll_num in range(10):
    result = my_6dice.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

my_10dice = Die(sides=10)

# Roll a 10-sided die 10 times
results = []
for roll_num in range(10):
    result = my_10dice.roll_die()
    results.append(result)
print("10 rolls of a 10-sided die:")
print(results)

my_20dice = Die(sides=20)
# Roll a 20 sided die 10 times
results = []
for roll_num in range(10):
    result = my_20dice.roll_die()
    results.append(result)
print("10 rolls of a 20-sided die:")
print(results)

"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five
letters. Randomly select four numbers or letters from the list and print a 
message saying that any ticket matching these four numbers or letters wins a 
prize
"""

lotto_win_code = (4, 100, 156, 288, 1009, 3838, 2127, 8384, 4343, 2909, "u",
                  "g", "x", "n", "q")
winning_ticket = []
print("The winning ticket for tonight is:")

# To avoid repeating the same values on the ticket, I used a while loop
while len(winning_ticket) < 4:
    code = choice(lotto_win_code)
    """Add the code only if it has not been chosen before"""
    if code not in winning_ticket:
        print(f"Winning code for tonight is {code}")
        winning_ticket.append(code)

print(f"The final winning ticket combination is {winning_ticket}")

"""
9-15: Lottery Analysis: You can use the loop to see how hard it might be 
to win the kind of lottery you just modeled. Make a list or tuple called 
my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 
Print the message reporting how many times the loop had run to give you a 
winning ticket.
"""


def get_winning_ticket(lotto_code):
    """Return the winning combination code"""
    winning_ticket = []

    # To avoid repeating the same values on the ticket, I used a while loop
    while len(winning_ticket) < 4:
        codes = choice(lotto_code)
        """Add the code only if it has not been chosen before"""
        if code not in winning_ticket:
            print(f"Winning code for tonight is {codes}")
            winning_ticket.append(codes)
    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    """Check all the value in the played ticket. If they are not in the
    winning_ticket, return False """
    for value in played_ticket:
        if value not in winning_ticket:
            return False
    # If the ticket is the winning_ticket return True
    return True


def make_random_ticket():
    """Return a random ticket from the list of lotto codes."""
    ticket = []
    # To avoid repeating the same values on the ticket, I used a while loop
    while len(ticket) < 4:
        codes = choice(lotto_code)
        """Add the code only if it has not been chosen before"""
        if codes not in ticket:
            print(f"Winning code for tonight is {codes}")
            ticket.append(codes)
    return ticket


lotto_code = (4, 100, 156, 288, 1009, 3838, 2127, 8384, 4343, 2909, "u",
              "g", "x", "n", "q")
winning_ticket = get_winning_ticket(lotto_code)

plays = 0
won = False

# Set the maximum about of tries possible to get a winning ticket
max_tries = 100_000


while not won:
    new_ticket = make_random_ticket()
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")

