def palindrome(s):
    if s == s[::-1]:
        return "palindrome"
    else:
        return "not a palindrome"
    
result = palindrome("racecar")
print(result)
result = palindrome("hello")
print(result)

# using a lambda function
palindrome_lambda = lambda s: "palindrome" if s == s[::-1] else "not a palindrome"
result = palindrome_lambda("level") 
print(result)
result = palindrome_lambda("world") 
print(result)