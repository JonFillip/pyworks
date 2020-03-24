from testing_code.city_function import city_location

print("Enter 'q' to quit program.")
while True:
    city = input("Enter the name of your city: ")
    if city == 'q':
        break

    country = input("Enter the name of your country: ")
    if country == 'q':
        break

    inhabitants = input("Enter the population of your city: ")
    if inhabitants == 'q':
        break
    else:
        population = int(inhabitants)

    city_info = city_location(city, country, population)
    print(f"\n{city_info}")
