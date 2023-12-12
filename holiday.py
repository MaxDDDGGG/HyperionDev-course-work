def cities():
    print("Available return flights:")
    print("Paris--- £25.00")
    print("Madrid--- £30.00")
    print("Budapest--- £35.00")
    print("Hel--- £66.60")
    print("Secret offer--- £10.00")

cities()
city_flight = input("Select a city from the list to fly to: ").capitalize()

valid_cities = ["Paris", "Madrid", "Budapest", "Hel"]

if city_flight not in valid_cities:
    print("Well done! You are entered into the random flight generator for just £10.00!")

num_nights = input("Enter the number of nights you wish to stay: ")
rental_days = input("Enter the number of days you need to rent a car: ")

try:
    num_nights = int(num_nights)
except ValueError:
    while True:
        try:
            num_nights = int(input("Please enter a valid number for the number of nights you wish to stay: "))
            break  
        except ValueError:
            print("Please enter a valid number.")

try:
    rental_days = int(rental_days)
except ValueError:
    while True:
        try:
            rental_days = int(input("Please enter a valid number for the number of days you need to rent a car: "))
            break  
        except ValueError:
            print("Please enter a valid number.")

def hotel_cost(num_nights):
    return num_nights * 50

def plane_cost(city_flight):
    if city_flight == "Paris":
        return 25.00
    elif city_flight == "Madrid":
        return 30.00
    elif city_flight == "Budapest":
        return 35.00
    elif city_flight == "Hel":
        return 66.60
    else:
        return 10.00

def car_rental(rental_days):
    return rental_days * 15
    

holiday_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
print(holiday_cost)

print("\n---Summary of holiday---")
print(f"\n    -Flights-\nPrice for flight to {city_flight}: \n£{plane_cost(city_flight):.2f}")
print(f"\n     -Hotel-\nPrice for {num_nights} nights: \n£{hotel_cost(num_nights):.2f}")
print(f"\n   -Car Rental- \nPrice for {rental_days} days: \n£{car_rental(rental_days):.2f}")
print(f"\n-Total Holiday Cost- \n£{holiday_cost:.2f}")
