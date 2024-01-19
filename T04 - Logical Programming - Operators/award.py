# Inputs for times to complete swimming, cycling and running
swimming_time = int(input("Swimming time (minutes) : "))
cycling_time = int(input ("cycling time (minutes) : "))
running_time = int(input("running time (minutes) : "))

# Total time of swimming, cycling and running
total_time = swimming_time + cycling_time + running_time
print(total_time)

# Award delegation
if total_time >= 111:
    print("Award: No Award")
elif total_time > 110:
    print("Award: Provincial Scroll")
elif total_time > 105:
    print("Award: Provincial Half Colours")
elif total_time < 100:
    print("Award: Provincial Colours")
