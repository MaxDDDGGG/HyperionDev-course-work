# Function for the selection of cities available
def cities():
    print("Available return flights:")
    print("Paris--- £25.00")
    print("Madrid--- £30.00")
    print("Budapest--- £35.00")
    print("Hel--- £66.60")
    print("Secret offer--- £10.00")

# Call Cities function
cities() 

# Input a city name and reformat, capital first letter only
city_flight = input("Select a city from the list to fly to: ").capitalize()

# Check for correct city names, or secret offer
city_check = ["Paris", "Madrid", "Budapest", "Hel"]
if city_flight not in city_check:
    print("Well done! You are entered into the random flight generator for just £10.00!")

# function to ensure the number of nights entered is a number
def number_check(x):
    while True:
        try:
            value = int(input(x))
            return value
        except ValueError:
            print("Please enter a valid number.")

#inputs and check using number check functions for the number of nights for hotel and number of days for car hire
num_nights = number_check("Please enter the number of nights you wish to stay: ")
rental_days = number_check("Please enter the number of days you need to rent a car: ")

# function for hotel cost calculation
def hotel_cost(num_nights):
    return num_nights * 50

# function for plane cost calculation
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

# function for car rental cost calculation
def car_rental(rental_days):
    return rental_days * 15
    
# total holiday cost using other costing functions
holiday_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
print(holiday_cost)

#Print out all info in easy to read format
print("\n---Summary of holiday---")
print(f"\n    -Flights-\nPrice for flight to {city_flight}: \n£{plane_cost(city_flight):.2f}")
print(f"\n     -Hotel-\nPrice for {num_nights} nights: \n£{hotel_cost(num_nights):.2f}")
print(f"\n   -Car Rental- \nPrice for {rental_days} days: \n£{car_rental(rental_days):.2f}")
print(f"\n-Total Holiday Cost- \n£{holiday_cost:.2f}")
