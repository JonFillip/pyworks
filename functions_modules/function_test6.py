def display_list(content, leftwidth, rightwidth):
    """Takes a dictionary input and displays the content in neatly formatted table"""
    print("CONTENT LIST".center(leftwidth + rightwidth, '#'))
    for key, value in content.items():
        print(key.ljust(leftwidth, '.') + str(value).rjust(rightwidth))

itinerary = {'tuition': 15000, 'accommodation': 7500, 'salary': 55000, 'bills': 2000}
display_list(itinerary, 15, 14)
