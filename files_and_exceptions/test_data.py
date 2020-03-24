import json


def collect_data():
    """Collect user input to build a dating profile and store it in a
    dictionary """
    date_profile = {}
    dating_file = "dating_profile.json"
    while True:
        # Prompt the user for his/her name, age, gender, date of birth and
        # location
        name = "name"
        first_name = input("Enter your first name: ")
        if first_name == 'quit':
            break
        surname = "surname"
        last_name = input("Enter your last name: ")
        if last_name == 'quit':
            break
        sex = "sex"
        gender = input("What is your gender? Male or Female: ")
        if gender == 'quit':
            break
        lifespan = "age"
        age = input("Enter your age: ")
        try:
            age = int(age)
        except ValueError:
            print(input("Invalid value! Please enter your age"))
        locality = "location"
        location = input("Please enter your location: ")
        if location == 'pass':
            pass
        elif location == 'quit':
            break
        # Store the user's data in a dictionary
        date_profile[name] = first_name
        date_profile[surname] = last_name
        date_profile[sex] = gender
        date_profile[lifespan] = age
        date_profile[locality] = location
        with open(dating_file, 'a') as f:
            json.dump(date_profile, f)


def retrieve_data():
    """Re-downloads the data stored in dating_file.json"""
    with open("dating_profile.json") as f_object:
        download_profile = json.load(f_object)
        print(download_profile)


collect_data()
retrieve_data()
