def make_car(car_name, *options):
    """Print the list of options that have been requested by the car buyer"""
    print(f"Car model: {car_name.title()}")
    for option in options:
        print(f"- {option}")
