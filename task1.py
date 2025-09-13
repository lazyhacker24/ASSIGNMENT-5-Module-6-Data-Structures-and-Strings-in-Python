# Task 1: Create a Dictionary of Student Marks

# Step 1: Create a dictionary with student names as keys and marks as values
# Pardeep
student_marks = {
    "Pardeep": 98,
    "Anjali": 92,
    "Rahul": 85,
    "Sneha": 90
}

# Step 2: Ask user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or display 'not found' message
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")
