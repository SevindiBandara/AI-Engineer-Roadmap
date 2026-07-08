def word_count(sentence):
    words = sentence.split()
    return len(words)

result = word_count("Hello, how are you?")
print(result)

# using a lambda function
word_count_lambda = lambda sentence: len(sentence.split())
result = word_count_lambda("This is a test sentence.")
print(result)

