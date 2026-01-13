# Create a tuple with 5 numbers

numbers = (1, 2, 3, 4, 5)
print(numbers)

# Access the third element in a tuple

numbers = (10, 20, 30, 40, 50)
print(numbers[2])

# Unpack a tuple into separate variables

data = (1, 2, 3)
a, b, c = data

print(a, b, c)

# Create a set of 5 fruits

fruits = {"apple", "banana", "mango", "orange", "grapes"}
print(fruits)

# Add a new fruit to the set

fruits = {"apple", "banana", "mango"}
fruits.add("pineapple")

print(fruits)

# Remove an element from a set

fruits = {"apple", "banana", "mango"}
fruits.remove("banana")

print(fruits)

# Find union of two sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)

# Find intersection of two sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 & set2)

# Check if one set is subset of another

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))

# Convert a list with duplicates into a set

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print(unique_numbers)

# 2

# Create a dictionary storing student names and marks

students = {
    "Diya": 85,
    "Shreya": 78,
    "Grishma": 92
}

print(students)

# Add a new key-value pair

students = {"Diya": 85, "Shreya": 78}
students["Grishma"] = 90

print(students)
['']
# Delete a key-value pair

students = {"Diya": 85, "Shreya": 78}
del students["Shreya"]

print(students)

# Merge two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1 | dict2
print(merged)

# Check if a key exists in a dictionary

students = {"Diya": 85, "Shreya": 78}

print("Diya" in students)


# Count word frequency using dictionary

text = "python is easy and python is powerful"
words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# Find the key with maximum value

students = {"Diya": 85, "Amit": 78, "Riya": 92}

max_key = max(students, key=students.get)
print(max_key)

# Reverse keys and values in a dictionary

data = {"a": 1, "b": 2, "c": 3}

reversed_dict = {value: key for key, value in data.items()}
print(reversed_dict)

# Update value for a specific key

students = {"Diya": 85, "Shreya": 78}
students["Diya"] = 90

print(students)

# Convert list of tuples into a dictionary

data = [("a", 1), ("b", 2), ("c", 3)]
dictionary = dict(data)

print(dictionary)





