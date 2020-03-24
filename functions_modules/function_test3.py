"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like
this: 'Santiago, Chile'. Call the function with a least 3 city-country pairs,
and print the values that are returned.
"""


def city_country(city, country):
    """Return the city and country of a user, neatly formatted."""
    place = f"{city}, {country}"
    return place.title()


location = city_country("kiev", "Ukraine")
print(f"\nThis is {location}")
location = city_country("Rio", "brazil")
print(f"\nThis is {location}")
location = city_country("lagos", "nigeria")
print(f"\nThis is {location}")

"""
8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make 3 dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.

Use the None value to add an optional parameter to make_album() that allows you 
to store the number of songs on an album. If the calling line includes a value
for the number of songs, add that value to the albums's dictionary. Make at 
least one new function call that includes the number of songs on an album.
"""


def make_album(artist, album_title, number_songs=None):
    """Return the album description, neatly formatted in a dictionary."""
    music_album = {'artist': artist, 'title': album_title}
    if number_songs:
        music_album['songs'] = number_songs
    return music_album


album = make_album("eminem", "kamakazi", 12)
print(album)

"""
8-8. User Album: Start your program from ex.8-7. Write a while loop that allows
users to enter an album's artist and title. Once you have that information, call
make_album() with the user's input and print the dictionary that's created. Be
sure to include a quit value in the while loop.
"""


def make_album(artist, title):
    """Allow user to enter the name of the artist and album title &
    add it to the dictionary"""
    music_album = {'artist': artist, 'album_title': title}
    return music_album


while True:
    print("Please enter the name of the artist and album:")
    print("(enter 'done' to quit.)")

    artist_name = input("Enter the artist name: ")
    if artist_name == "done":
        break

    album_title = input("Enter the album title: ")
    if album_title == "done":
        break

    music_box = make_album(artist_name, album_title)
    print(f"I want to listen to:\n{music_box}")
