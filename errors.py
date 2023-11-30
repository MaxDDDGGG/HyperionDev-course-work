# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Added ()
print ("\n") # Removed indentation and added ()

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" # Removed indentation and changed == to =
age_extraction = ''.join(filter(str.isdigit, age_Str)) # Added a number extraction step
age = int(age_extraction) # Removed indentation and used the extracted number
print(f"I'm {age} years old.") # Removed indentation

# Variables declaring additional years and printing the total years of age
years_from_now = 3 # Removed indentation and ""
total_years = age + years_from_now # Removed indentation

print (f"The total number of years: {total_years}") # Added (f{}) and changed "answer_years" to total_years

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Changed total to total_years
print (f"In 3 years and 6 months, I'll be {total_months + 6} months old") # Added (formatted string) and added the + 6 months


#HINT, 330 months is the correct answer