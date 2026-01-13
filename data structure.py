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

