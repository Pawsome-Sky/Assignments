print("Student Grade Tracker")
students = []
student_grades = {}
subjects = ["first", "second", "third"]
num_students = int(input("Enter the number of students: "))
i = 0
while i < num_students:
    name = input("Enter student name: ")
    students.append(name)
    i += 1
    for student in students:
        for subject in subjects:
            grade = int(input(f"Enter the {subject} subject's grade of {student}: "))