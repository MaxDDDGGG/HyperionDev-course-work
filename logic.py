print ("---Cephalopod Tracker---")

# Ecology of area of ocean, list of cephalapods of interest
octopus_counter = int(input("Number of octopuses counted : "))
squid_counter = int(input("Number of squid counted : "))
cuttlefish_counter = int(input("Number of cuttlefish counted : "))
#total cephalapod count
cephalopod_counter = octopus_counter + squid_counter + cuttlefish_counter
#shark counter (will always be 0) because there is no input for different sharks
shark_counter = 0

#Octopus % will cause an error because I used the shark counter in the calculation so will be divided by 0
octopus_percent = octopus_counter/shark_counter * 100
# Correct calculations
squid_percent = squid_counter / cephalopod_counter * 100
cuttlefish_percent = cuttlefish_counter / cephalopod_counter * 100

# Outputs for numbers and percentages of different cephalopods
print (f"number of octopus: {octopus_counter}")
print (f"percentage of octopus: {octopus_percent}%")
print (f"number of squid : {squid_counter}")
print (f"percentage of squid: {squid_percent}%")
print (f" number of cuttlefish: {cuttlefish_counter}")
print (f"percentage of cuttlefish: {cuttlefish_percent}%")