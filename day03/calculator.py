def calculator(a,b, operation):
    if operation == "add":
        return a+b
    elif operation == "subtract":
        return a-b
    elif operation =="multiply":
        return a*b
    elif operation == "divide":
        if b != 0:
            return a/b
        else:
            return "error: division by zero"
 
calculator_result = calculator(10, 5, "add")
print(calculator_result)
calculator_result = calculator(10, 5, "subtract")
print(calculator_result)
calculator_result = calculator(10, 5, "multiply")
print(calculator_result)
calculator_result = calculator(10, 5, "divide")
print(calculator_result)
calculator_result = calculator(10, 0, "divide")
print(calculator_result)
