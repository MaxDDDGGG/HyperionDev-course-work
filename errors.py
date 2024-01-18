# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error - added ()
print ("\n") # Indentaiton error - removed indentation and Syntax error - added ()

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" # Indentaiton error - removed indentation and logic error changed == to =
age_extraction = ''.join(filter(str.isdigit, age_Str)) # potential logic error - added a number extraction step
age = int(age_extraction) # Indentaiton error - removed indentation and potential logic error - used the extracted number
print(f"I'm {age} years old.") # Indentaiton error - removed indentation

# Variables declaring additional years and printing the total years of age
years_from_now = 3 # Indentaiton error - removed indentation and logic error""
total_years = age + years_from_now # Indentaiton error - removed indentation

print (f"The total number of years: {total_years}") #  syntax error Added (f{}) and name error changed "answer_years" to total_years

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # logic error - Changed total to total_years
print (f"In 3 years and 6 months, I'll be {total_months + 6} months old") # syntax error - added (formatted string) and logic error added the + 6 months


#HINT, 330 months is the correct answer