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
            while True:
                grade = int(input(f"Enter the grade {student} received in the {subject} subject: "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Please enter a valid grade between 0 and 100.")
                student_grades[name] = grade
print(student_grades)