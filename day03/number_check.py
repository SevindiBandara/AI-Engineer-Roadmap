check = lambda number: "positive" if number > 0 else "negative"  if number < 0 else "zero"
print(check(10))

# using a function to check if a number is positive, negative, or zero
def check(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
    
result = check(10)
print(result)
result = check(-5)
print(result)
result = check(0)
print(result)