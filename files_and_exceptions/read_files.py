# Reading from a File

"""Data presents itself in many formats and extensions (for example csv, txt,
json, xml). A large amount of data is available in text files. Text files can
contain data, traffic data, socioeconomic data, literary works, and more.
Reading from a file is particularly useful in data analysis applications,
but it's also applicable to any situation in which you want to analyze or
modify information stored in a file. For example, you can write a program  that
reads in the contents of a text file and rewrites the file with formatting that
allows a browser to display it.
    When you want to work with the information in a text file, the first step is
to read the file into memory. You can read the entire contents of a file, or you
work through the file one line at a time"""

# Reading an Entire File
"""
To begin working with a file, we have to first open it to access it and the 
open() function is the first piece of code need to do that. The open() function
needs one argument: The name of the file you want to open. For example, reading 
the file ai_bigdata.txt. The keyword 'with' closes the file once access to it is
longer needed.
    Notice the file has open() call but not a close(). You could open and close 
the file by calling the open() and close() function, but if a bug  in your 
program prevents the close() method from being executed, the file may never 
close.
"""

with open("/Users/johnphillip/Desktop/python_work/files_and_exceptions"
          "/ai_bigdata.txt") as file_object:
    script = file_object.read()
print(script.rstrip())

# File paths
"""When passing a filename like ai_bigdata.txt to the open() function, 
Python looks in the directory where the file that's currently being executed 
is stored. Sometimes, depending on how one might organize ones work, the file 
you want to open won't be in the same directory as your program file. For 
example, one might store a store a program file in a folder/directory called 
python_work; inside python_work, I have smaller directories/folders and in 
one of the folders called files_and_exceptions to distinguish your program 
files from the text files they're manipulating. Even though 
files_and_exceptions is in python_work, just passing open() the name of the 
file in files_and_exceptions won't work, because Python will only look in the 
python_work and stop there; it won't go on and look in files_and_exceptions. 
To get python to open files from a directory other than the one where your 
program file is stored, you need to create a 'file path' which tells Python to
look in a specific location on your system.

Because files_and_exceptions is inside python_work, you could use a relative 
file path to open a file from files_and_exceptions. A 'relative file path' tells
Python to look for a given location relative to the directory where the current
running program file is stored. For example:

with open(files_and_exceptions/ai_bigdata.txt) as file_object: 

You can also use absolute file paths to tell Python exactly where the file is 
on your computer regardless of where the program that's being executed is stored
. Absolute file paths have longer addresses and are better stored in a variable.
For example: 

file_path = '/Users/johnphillip/Desktop/python_work/files_and_exceptions'
          '/ai_bigdata.txt' 
with open(file_path) as script:
"""
# Reading Line by Line
# To read through a file's content line by line. Use the following syntax:

filename = "/Users/johnphillip/Desktop/python_work/files_and_exceptions" \
           "/ai_bigdata.txt"
with open(filename) as text:
    for line in text:
        print(line)

# Making a List of lines from a File
"""
When you use 'with', the file object returned by open() is only available inside
the 'with' block of code. If you want to work with the file's content outside 
the 'with' block, you can store the file's lines in a list inside the the block
and then work with that list. You can process parts of the file immediately or 
postpone some processing for later in the program.
    For example, storing the lines of ai_bigdata.txt in a list inside the 'with'
block and then print the lines outside the with block.
"""
paper = "/Users/johnphillip/Desktop/python_work/files_and_exceptions" \
           "/ai_bigdata.txt"

with open(paper) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace("data", "information"))

