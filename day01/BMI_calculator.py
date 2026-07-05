height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height / 100) ** 2
print("Your BMI is:", bmi)