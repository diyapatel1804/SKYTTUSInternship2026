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

