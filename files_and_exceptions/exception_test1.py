# 10-6. Addition & 10-7. Addition Calculator:
print("Please enter two values to be summed.")
print("Enter 'cancel' to exit program.")

while True:
    numb1 = input("Enter the first figure: ")
    if numb1 == "cancel":
        break
    numb2 = input("Enter a second figure: ")
    if numb2 == "cancel":
        break

    try:
        add = int(numb1) + int(numb2)
    except ValueError:
        print("Invalid value. Please enter an integer number.")
    else:
        print(f"The sum of {numb1} and {numb2} is {add}")


# 10-8. Cats and Dogs:
# with open("files_and_exceptions/cat.txt", 'a') as cat_file:
#    cat_file.write("This is a record of cat species:\n")
#    cat_file.write("1.Persian Cat\n2.Bengal Cat\n3.Siamese Cat")

# with open("files_and_exceptions/dog.txt", 'a') as dog_file:
#   dog_file.write("This is a record of dog breeds:\n ")
#   dog_file.write("1. German Shepperd\n2. Beagle\n3. Doberman")


def print_content(file):
    """Print the content of the files"""
    try:
        with open(file, encoding="utf-8") as file_object:
            file_item = file_object.read()

    except FileNotFoundError:
        pass

    else:
        print(file_item)


file_names = ["files_and_exceptions/cat.txt", "files_and_exceptions/dog.txt",
              "birds.txt"]

for doc in file_names:
    print_content(doc)


# 10-10. Common Words

def count_word(filename):
    """Count the number of occurrence of the given word"""
    try:
        with open(filename, 'r') as book_text:
            file_item = book_text.read()
        print(file_item)
    except FileNotFoundError:
        print(f"Sorry but the file {filename} does not exist. Please check the "
              f"file path or the spelling of the file for errors.")
    else:
        # count the number of times the word 'roman' appears
        word = "the"
        word_appearance = file_item.count(word)
        print(f"The word '{word}' appears in {filename}, {word_appearance} times")


book = "/Users/johnphillip/roma.txt"
count_word(book)
