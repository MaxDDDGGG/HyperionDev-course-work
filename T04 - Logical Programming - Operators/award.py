# Inputs for times to complete swimming, cycling, and running
swimming_time = input("Swimming time (minutes): ")
cycling_time = input("Cycling time (minutes): ")
running_time = input("Running time (minutes): ")

while True:
    try:
        swimming_time = float(swimming_time)
        cycling_time = float(cycling_time)
        running_time = float(running_time)
        break
    except ValueError:
        print("\n---ERROR---\nTime needs to be entered in minutes (MM.SS)\n")
        swimming_time = input("Swimming time (minutes): ")
        cycling_time = input("Cycling time (minutes): ")
        running_time = input("Running time (minutes): ")


# Total time of swimming, cycling, and running
total_time = swimming_time + cycling_time + running_time
print(total_time)

# Award delegation
if total_time >= 111:
    print("Award: No Award")
elif total_time > 106:
    print("Award: Provincial Scroll")
elif total_time > 101:
    print("Award: Provincial Half Colours")
elif total_time <= 100:
    print("Award: Provincial Colours")

