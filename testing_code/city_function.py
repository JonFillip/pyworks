# 11-1. City, Country


def city_location(city, country, population=None):
    """Function accepts two parameters for the city and country names and
    returns a neatly formatted string of the city location"""
    if population:
        location = f"{city}, {country} - population {population}."

    else:
        location = f"{city}, {country}."

    return location.title()
