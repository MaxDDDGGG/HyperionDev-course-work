total = 0
count = 0
number = int(input("Please enter a number: "))

while number != -1:
    total += number
    count += 1

    number = int(input("Please enter a number: "))
    if number == -1:
        print(f"The average of entered numbers : {int(total/count)}")
        break
