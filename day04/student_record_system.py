students = {
    "name": input("enter student name: "),
    "age": int(input("enter student age: ")),
    "course": input("enter student course: "),
    "GPA": float(input("enter student GPA: "))
}

print("\n===========student details===========")
print("Name:", students["name"])
print("Age:", students["age"])
print("Course:", students["course"])
print("GPA:", students["GPA"])
print("====================================")