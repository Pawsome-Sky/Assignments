print("Student Grade Tracker")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value != 0:
                return value
            else:
                print("The number cannot be zero. Please enter a number that is not zero.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_float(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid. Please enter a valid number.")


student_grades = {

}

# Number of students and names
num_students = get_int("Enter the number of students: ")
for _ in range(num_students):
    name = input("Enter student name: ")
    student_grades[name] = {}
    # Number of subjects and names
    num_subjects = get_int(f"Enter the number of subjects {name} has: ")
    for _ in range(num_subjects):
        subject_name = input("Enter the name of the subject: ")
        student_grades[name][subject_name] = {}
        # Grades for each student for the subjects
        while True:
            grade = get_float(f"Please enter the grade {name} received for {subject_name}: ")
            if 0 <= grade <= 100:
                student_grades[name][subject_name] = int(grade)
                break
            else:
                print("Please enter a valid grade between 0 and 100.")
            # print(student_grades)
# Calculate average student grade
for name in student_grades:
    grades = list(student_grades[name].values())
    total_grades = sum(grades)
    num_grades = len(grades)
    average_grade = total_grades / num_grades if num_grades > 0 else 0
    print(f"Average grade for {name}: {average_grade:.2f}")
