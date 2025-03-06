class GPA:
    def __init__(self):
        self.total_credits = 0
        self.total_credit_points = 0
        self.course_data = []

    def add_course(self, course_name, credits, grade):
        credit_points = self.calculate_credit_points(credits, grade)
        self.total_credit_points += credit_points
        self.total_credits += credits
        self.course_data.append((course_name, credits, credit_points))

    def calculate_credit_points(self, credits, grade):
        if grade == "O":
            return credits * 10
        elif grade == "A+":
            return credits * 9
        elif grade == "A":
            return credits * 8
        elif grade == "B+":
            return credits * 7
        elif grade == "B":
            return credits * 6
        elif grade == "C":
            return credits * 5
        elif grade == "RA":
            return credits * 0
        elif grade == "SA":
            return credits * 0
        elif grade == "W":
            return credits * 0
        else:
            return 0

    def calculate_gpa(self):
        if self.total_credits == 0:
            return 0
        return self.total_credit_points / self.total_credits

# Creating an instance of the GPA class
student_gpa = GPA()

# Getting input from the user for courses and grades
num_courses = int(input("Enter the number of courses: "))
for _ in range(num_courses):
    course_name = input("Enter the name of the course: ")
    credits = int(input("Enter the credit hours of the course: "))
    grade = input("Enter the grade for the course (O, A+, A, B+, B, C, RA, SA, W): ").upper()
    student_gpa.add_course(course_name, credits, grade)

# Displaying subject names and calculated credits
print("\nSubject Name\tCredits\tCalculated Credit")
print("-----------------------------------------")
for course_name, credits, credit_points in student_gpa.course_data:
    print(f"{course_name}\t\t{credits}\t\t{credit_points}")

# Calculating and printing the GPA
gpa = student_gpa.calculate_gpa()
print(f"Student's GPA: {gpa:.2f}")
