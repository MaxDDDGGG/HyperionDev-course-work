print ("---Cephalopod Tracker---")

# Ecology of area of ocean, list of cephalapods of interest
octopus_counter = int(input("Number of octopuses counted : "))
squid_counter = int(input("Number of squid counted : "))
cuttlefish_counter = int(input("Number of cuttlefish counted : "))
#total cephalapod count
cephalopod_counter = octopus_counter + squid_counter + cuttlefish_counter

#Octopus % will cause a a logical error because I used the squid counter instead of total cephalopods
octopus_percent = round(octopus_counter/squid_counter * 100)

# Correct calculations
squid_percent = round(squid_counter / cephalopod_counter * 100)
cuttlefish_percent = round(cuttlefish_counter / cephalopod_counter * 100)

# Outputs for numbers and percentages of different cephalopods
print("---------------------------------------")
print (f"number of octopus: {octopus_counter}")
print (f"percentage of octopus: {octopus_percent}%")
print("---------------------------------------")
print (f"number of squid : {squid_counter}")
print (f"percentage of squid: {squid_percent}%")
print("---------------------------------------")
print (f"number of cuttlefish: {cuttlefish_counter}")
print (f"percentage of cuttlefish: {cuttlefish_percent}%")
print("---------------------------------------")