class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self):
        for course in self.enrolled_courses:
            course_name = course.name
            grade = self.grades.get(course, "N/A")
            print(f"Student: {self.name}, Course: {course_name}, Grade: {grade}")

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    def list_courses(self):
        return self.courses


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        self.lessons = []
        teacher.courses.append(self)  # Add this course to the teacher's course list

    def __repr__(self):
        return self.name

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = []

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student].append((date, status))

    def generate_report(self):
        for student in self.students:
            attendance_status = self.attendance.get(student, [])
            print(f"Student: {student.name}, Attendance: {attendance_status}")

    def add_lesson(self, lesson):
        if isinstance(lesson, Lesson):
            self.lessons.append(lesson)
        else:
            print("Invalid lesson type. Please provide a Lesson object.")

    def get_lessons(self):
        return self.lessons


class Lesson:
    def __init__(self, lesson, date, material):
        self.lesson_topic = lesson
        self.date = date
        self.material = material


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report()
# Student: Alice, Attendance: ['2024-01-21: Present']
# Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()  # Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']

lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])

math_course.add_lesson(lesson1)
math_course.add_lesson(lesson2)
math_course.get_lessons()

lessons = math_course.get_lessons()
for lesson in lessons:
    print(f"Lesson Topic: {lesson.lesson_topic}, Date: {lesson.date}, Material: {lesson.material}")