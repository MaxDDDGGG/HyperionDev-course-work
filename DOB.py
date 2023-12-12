
# Print Name as a title with space above and below
print("\n---Name---\n")
# Open DOB.txt in a reading format
with open('DOB.txt', "r") as file:
# take the first 2 words from each line loop and print
    for line in file:
        name = line.split()[:2]
        name = ' '.join(name)
        print(name)
# Print DOB as a title with space above and below
print("\n---DOB---\n")
# Open DOB.txt in a reading format again 
with open('DOB.txt', 'r') as file:
# take all but the first 2 words from each line loop and print    
    for line in file:
        dob = line.split()[2:]
        dob = ' '.join(dob)
        print(dob)