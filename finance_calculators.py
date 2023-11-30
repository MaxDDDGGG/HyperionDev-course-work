import math

# Content descriptions for each calculator option
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Input for choosing the finance calculator
finance_calculator = input("Enter either 'investment' or 'bond' from the above menu to proceed: ").lower()

# investment calculator
if finance_calculator == "investment":

    #confirmatory statement
    print(f"You have selected the {finance_calculator} calculator")
    print()

    # Input of required data for calculations
    depositing_funds = float(input("Enter the amount of money being deposited : "))
    interest_rate = float(input("Enter the interest rate : "))
    investment_period = int(input("Enter the number of years you intend to invest for : "))
    interest = input("Do you want 'simple' or 'compound' interest : ").lower()

    # Calculations and output for 'simple' interest investments
    if interest == "simple":
        print(f"You have selected the {interest} interest option")
        print(f"The total amount once interest has been applied will be: £{round(float(depositing_funds * (1 + (interest_rate / 100)) * investment_period),2)}")
    # Calculations and output for 'compound' interest investments
    elif interest == "compound":
        print(f"You have selected the {interest} interest option")
        print(f"The total amount after interest has been applied will be: £{round(float(depositing_funds * math.pow(1 + (interest_rate / 100), investment_period)),2)}")
    
    # Output if the interest option was not valid, eg a mistake
    else:
        print(f"{interest} is not a valid interest option")

# bond calculator
elif finance_calculator == "bond":

    #confirmatory statement
    print(f"You have selected the {finance_calculator} calculator")
    print()
    # Input of required data for calculations
    house_value = int(input("Enter present value of house : "))
    interest_rate =  float(input("Enter the interest rate : "))
    months = int(input("Enter the number of months you plan to take to repay the bond : "))

    #Calculations and output for the bond
    print(f"The amount you will have to repay each month is : £{round(float((interest_rate / 100) * house_value) / (1 - (1 + interest_rate / 100) ** (-months)), 2)}")

# Output if finance calculator option is not valid
else:
    print(f"{finance_calculator} is not a valid calculator option!")