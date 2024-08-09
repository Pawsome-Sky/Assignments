print("Student Grade Tracker")
student_grades = {

}
subjects = ["first", "second", "third"]
num_students = int(input("Enter the number of students: "))
i = 0
while i < num_students:
    name = input("Enter student name: ")
    student_grades[name] = {}
    i += 1
    for subject in subjects:
        while True:
            grade = int(input(f"Enter the grade {name} received in the {subject} subject: "))
            if 0 <= grade <= 100:
                student_grades[name][subject] = int(grade)
                break
            else:
                print("Please enter a valid grade between 0 and 100.")
    numbers = list(student_grades[name].values())
    total_grades = sum(numbers)
    average_grade = total_grades / 3
    print(f"Average grade for {name}: {average_grade}")
