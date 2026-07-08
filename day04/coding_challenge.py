#find the largest number in a list and count the occurrences of each number
numbers = [10,60,78,90,66,38,69,30,69,35,90,100,78,60,10]
largest_number = max(numbers)
print("The largest number in the list is:", largest_number)

#count occurrences of each number
# method 1
frequent = {}
for number in numbers:
    if number in frequent:
        frequent[number] += 1
    else:
        frequent[number] = 1

for number, count in frequent.items():
    print(number, "is repeated", count, "times")
 
 #method 2
numbers = [10, 20, 30, 20, 40, 10, 20, 30]

frequency = {}

for number in numbers:
    if number not in frequency:
        frequency[number] = numbers.count(number)

for key, value in frequency.items():
    print(key, "appears", value, "times")
    
#reversed list
print(numbers[::-1])

#remove duplicates
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)

#merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

