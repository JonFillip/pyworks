# Writing to a File

# Writing to an Empty File
"""
To write to a file, you need to call the open() with a second argument telling
Python that you want to write to the file. To see how this works, I'll write a
simple tongue twister and store it in a file instead of printing to a screen:
"""

filename = "files_and_exceptions/tongue.txt"

with open(filename, "w") as twister:
    twister.write("Father francis fried five fresh fish for the five french "
                  "priest")

"""
The call to open() at line 12 has two arguments. The first argument is still the
name of the file I want to open. The second argument, 'w', tells python that I 
want to open the file in write mode. In Python you can open a file in read mode
('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read &
write to the file ('r+'). If you omit the mode argument, Python by default open 
the file only in read-only mode.

The open() function automatically creates the file you're writing to if it 
doesn't already. However, please be aware if you open a file in write mode 'w'
and that file already exists, Python will erase the contents of the existing 
file before returning the file object.

In line 13, we use the write() method on the file object to write a string to 
the file. The program has no terminal output, but if you open the the file
tongue.txt you will see the text has already been added in the file
"""
# NOTE:
"""
Python can only write strings to a text file. If you want to add in numerical 
data in a text file, you'll have to convert the data to string format first 
using the str() function.
"""

# Writing multiple line to a file
filename = "vertical_farm.txt"

with open(filename, "w") as file_object:
    file_object.write("Climate change is real and we the way we eat need to "
                      "change to save our planet.\n")
    file_object.write(str(7000000000))
    file_object.write("\nThat number is amount of people our planet needs to "
                      "feed and that number is growing everyday")
with open(filename, "r") as file_object:
    present = file_object.read()
print(present)

# Appending to a file
"""
When you want to add content to a file without writing over the existing content
you can open the file in append mode ('a'). When you open a file in append mode,
Python doesn't erase the contents of the file before returning the file object.
Any lines you write to the file will be added at the end of the file. If the 
file doesn't exist yet, Python will then create an empty file for you.

    I'll modify my vertical_farm.txt file in this example adding a few point to
explain vertical farming:
"""
with open(filename, 'a') as file_object:
    file_object.write("Vertical farming allows us to plant crops in already "
                      "existing building, stacking shelves of crops "
                      "vertically in the building.\n")
    file_object.write("The benefits of vertical farming are revolutionary. "
                      "Such as:\n")
    file_object.write("1. Less resources such as land, water, soil and "
                      "pesticides are used.\n")
    file_object.write("2. Crops are healthier and can grown all year round "
                      "due to the absence of being at the mercy of weather "
                      "and season changes. All the crops are grown in climate "
                      "controlled rooms all year round.\n")
with open(filename, 'r') as script:
    present = script.read()
print(present)
