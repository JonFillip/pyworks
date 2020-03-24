"""
3-4. If you could invite anymore, living or deceased, to dinner, who would you invite? Make a list that includes at
least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them
to dinner.
"""

guests = ["Bill Gates", "Burna Boy", "Lyubov", "Jeff Bezos", "Sir Sunny", "Mum"]
for guest in guests:
    print(f"Dear {guest},\nIt will be of great honor if you could join me for dinner this Friday by 19:00 at the alps")

# 3-5.
declined_guest = guests.pop(-2)
print(declined_guest)
guests.insert(-2, "Mark Joshua")
print(guests)
for re_guest in guests:
    print(f"\nDear {re_guest},\nIt will be of great honor if you could join me for dinner this Friday by 19:00 at the "
          f"alps")

# 3-6.
print(guests)
for guest in guests:
    print(f"\nHey {guest}, I found a larger dinner table so might be having more guests.")

guests.insert(0, "Mary Joanne")
guests.insert(-3, "Elon Musk")
guests.append("John Eagleton")
print(guests)
for guest in guests:
    print(f"\nHey {guest}, It's me again just wanted to inform that dinner will be in hall 2 at the tissot alps.")


# 3-7.
print(guests)
print(f"\nHey guys, I'm sorry but I just found out our table got canceled and they've only got a table for three")
uninvited_guests1 = guests.pop(0)
print(f"\nDear {uninvited_guests1},\nI'm sad to inform that dinner has been cancelled due to lack of guest places.")

print(guests)  # ['Bill Gates', 'Burna Boy', 'Lyubov', 'Elon Musk', 'Mark Joshua', 'Jeff Bezos', 'Mum', 'John Eagleton']

uninvited_guests2 = guests.pop(0)
print(f"\nDear {uninvited_guests2},\nI'm sad to inform that dinner has been cancelled due to lack of guest places.")

uninvited_guests3 = guests.pop(0)
print(f"\nDear {uninvited_guests3},\nI'm sad to inform that dinner has been cancelled due to lack of guest places.")

uninvited_guests4 = guests.pop(1)
print(f"\nDear {uninvited_guests4},\nI'm sad to inform that dinner has been cancelled due to lack of guest places.")

print(guests)  # ['Lyubov', 'Mark Joshua', 'Jeff Bezos', 'Mum', 'John Eagleton']

uninvited_guests5 = guests.pop(1)
print(f"\nDear {uninvited_guests5},\nI'm sad to inform that dinner has been cancelled due to lack of guest places.")

uninvited_guests6 = guests.pop(2)
print(f"\nDear {uninvited_guests6},\nI'm sad to inform that dinner has been cancelled due to lack of guest places.")

uninvited_guests7 = guests.pop(-1)
print(f"\nDear {uninvited_guests7},\nI'm sad to inform that dinner has been cancelled due to lack of guest places.")

print(guests)  # ['Lyubov', 'Jeff Bezos']
for guest in guests:
    print(f"\nDear {guest},\nIt's me again, just writing to let us you guys know that we will still be having dinner at "
          f"the alps but it will be at the Rolex resort. Thanks for accepting my invite, can't wait to see you on Friday")

del guests[0]
print(guests)

del guests[0]
print(guests)








