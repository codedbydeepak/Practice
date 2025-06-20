student_marks = {"Deepak": 85, "Anjali": 90, "Rahul": 78, "Priya": 88}

user_input = input("Enter a student's name to get their marks: ")

if user_input in student_marks:
    marks = student_marks[user_input]
    print(f"{user_input}'s marks: {marks}")
else:
    print("Student not found.")
