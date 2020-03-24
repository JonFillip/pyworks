from testing_code.testing_function import get_fullname

print("Enter 'q' to quit program.")
while True:
    first_name = input("Enter your first name: ")
    if first_name == 'q':
        break
    last_name = input("Enter your last name: ")
    if last_name == 'q':
        break

    formatted_name = get_fullname(first_name, last_name)
    print(f"\tFullname is {formatted_name}")
