'''input for the number of students and error checker'''
number_of_students = input("Please enter the number of students you are registering: ")
while True:
    try:
        number_of_students = int(number_of_students)
        break
    except ValueError:
        print("\n---ERROR---\nIncorrect input: Number of children must be a whole number!")
        number_of_students = input("Please enter the number of students you are registering: ")
    
'''Create a blank dictionary 
Add the student IDs'''
added_ids = []
while number_of_students > 0:
    student_ID = input("Enter student ID: ")

    '''The dictionary is them appended to reg_form.txt
    Unless it is already present in reg_form.txt, then an error message is printed
    If it is added correctly a success message is printed, containing the student ID
    For each student number successfully added the number_of_students is counted down until number_of_students = 0
    When all students are added, there is a prompt to say "All Students addded!"'''
    with open("reg_form.txt", "a+") as f:
        if student_ID in added_ids:
            print("Error! Student already added to register")
        else:
            f.write(student_ID + "............................\n\n")
            print(f"Student ID: {student_ID} added successfully!")
            added_ids.append(student_ID)
            number_of_students -= 1
print(f"\nAll students added!")