def student():
    name = input("Enter student name: ")
    return name

def enter_marks():
    math = int(input("Enter marks for Math: "))
    science = int(input("Enter marks for Science: "))
    english = int(input("Enter marks for English: "))
    return math, science, english

def calculate_average(math, science, english):
    average = (math + science + english) / 3
    return average

def grade(average):
    if average >= 75:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 55:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"
    
def display_result(name, math, science, english, average, grade):
    print("\n============STUDENT REPORT ============")
    print(f"Name: {name}")
    print()
    print(f"Math: {math}")
    print(f"Science: {science}")
    print(f"English: {english}")
    print()
    print(f"Average: {average}")
    print(f"Grade: {grade}")
    print("========================================")
    
student_name = student()
math_marks, science_marks, english_marks = enter_marks()
average_marks = calculate_average(math_marks, science_marks, english_marks)
student_grade = grade(average_marks)
display_result(student_name, math_marks, science_marks, english_marks, average_marks, student_grade)    

