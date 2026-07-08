def reverse_word(word):
    return word[::-1]

result = reverse_word("hello")
print(result)

# using a lambda function
reverse = lambda word: word[::-1]
result = reverse("world")
print(result)

