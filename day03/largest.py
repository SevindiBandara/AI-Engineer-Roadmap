def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
result = largest(10, 5, 8)
print(result)

# using a lambda function to find the largest number
check_largest = lambda a, b, c: a if a >= b and a >= c else b if b > a and b > c else c
result = check_largest(10, 20, 30)
print(result)
