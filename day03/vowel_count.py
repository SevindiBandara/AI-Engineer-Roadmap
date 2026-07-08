def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

result = count_vowels("hello")
print(result)

# using a lambda function
count_vowels_lambda = lambda s: sum(1 for char in s if char in "aeiouAEIOU")
result = count_vowels_lambda("world")
print(result)