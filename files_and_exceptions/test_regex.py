import re


def red_green_blue():
    """This function is to a regex list from the file rgb.txt"""
    filename = '/Users/johnphillip/Desktop/python_work/files_and_exceptions' \
               '/rgb.txt'
    with open(filename, 'r+') as file_object:
        reader = file_object.readlines()
        file_object.seek(0)
        for line in reader:
            if line != 'red       green         blue       colorname\n':
                file_object.write(line)
        file_object.truncate()
        n_reader = [re.sub(r'\s+', '\\t', line.strip()) for line in reader]
        file_object.write(line)
        file_object.truncate()
        print(n_reader)


if __name__ == "__main__":
    red_green_blue()
