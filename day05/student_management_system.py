class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display_details(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)

    def calculate_grade(self):
        if self.marks >= 75:
            return "A"
        elif self.marks >= 65:
            return "B"
        elif self.marks >= 55:
            return "C"
        elif self.marks >= 45:
            return "D"
        else:
            return "F"


# Objects
student1 = Student("Alex", 20, "Data Science", 85)
student1.display_details()
print("Grade:", student1.calculate_grade())

print()

student2 = Student("John", 22, "Software Engineering", 60)
student2.display_details()
print("Grade:", student2.calculate_grade())