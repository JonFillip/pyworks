# 10-1 Learning Python
big_text = "files_and_exceptions/learning_python.txt"

with open(big_text) as text:
    """first call is to read the entire file"""
    script = text.read()
print(script.rstrip())

with open(big_text) as info:
    """print each line in the file line by line"""
    for line in info:
        print(line)

with open(big_text) as file_object:
    lines = file_object.readlines()
"""Print the lines of the file in uppercase letters outside the with block"""
for line in lines:
    print(line.upper().rstrip())

# 10-2 Learning C
with open(big_text) as about_python:
    lines = about_python.readlines()
    """Replace the word python in the file with C"""
for line in lines:
    print(line.rstrip().replace("Python", "C"))
