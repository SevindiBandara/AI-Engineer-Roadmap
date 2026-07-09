class Student:
    
    school = "SLIIT"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old and I am in grade {self.grade}."
    
student1 = Student("Alice", 15, 10)
print(student1.introduce())
print(student1.school)

student2 = Student("Bob", 16, 11)
print(student2.introduce()) 
print(student2.school)