number_of_students = int(input("Please enter the number of students you are registering: "))
added_ids = []
while number_of_students > 0:
    student_ID = input("Enter student ID: ")

    with open("reg_form.txt", "a+") as f:
        if student_ID in added_ids:
            print("Error! Student already added to register")
        else:
            f.write(student_ID + "............................\n\n")
            print(f"Student ID: {student_ID} added successfully!")
            added_ids.append(student_ID)
            number_of_students -= 1
print(f"\nAll students added!")