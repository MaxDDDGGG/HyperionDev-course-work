# Input for password and confrimation.
password = input("Enter Password : ")
password_validation = input("Confirm the password : ")

# List for incorrect pasword_validation inputs.
incorrect_passwords = []

# Add incorrect passwords to the incorrect_passwords list.
while password_validation != password:
    print("Passwords do not match!")
    incorrect_passwords.append(password_validation)

# Repeated inputs for password_validation
    password_validation = input("Confirm the password : ")

# Matching passwords actions.
if password == password_validation:
    print (f"Correct password : {password}")
    print(f"Incorrect password inputs : {incorrect_passwords}")