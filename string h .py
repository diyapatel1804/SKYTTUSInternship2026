# Take a string input and print its length

text = input("Enter a string: ")
print("Length:", len(text))

# Convert a sentence to lowercase

sentence = input("Enter a sentence: ")
print(sentence.lower())

# Replace spaces with underscores

text = input("Enter a string: ")
print(text.replace(" ", "_"))

# Extract first and last character of a string

text = input("Enter a string: ")

if len(text) > 0:
    print("First character:", text[0])
    print("Last character:", text[-1])

# Reverse a string using slicing

text = input("Enter a string: ")
print("Reversed string:", text[::-1])

# Count how many times a letter appears in a string

text = input("Enter a string: ")
letter = input("Enter a letter to count: ")

print("Count:", text.count(letter))

# Check if a word is present in a sentence

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print("Word is present")
else:
    print("Word is not present")

# Take name & age and print using f-string

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")

# Remove extra spaces from start and end

text = input("Enter a string with spaces: ")
print(text.strip())

# Join list of words into single string with 

words = ["Python", "is", "easy"]
result = "-".join(words)

print(result)

# 2
 # Create a list of your 5 favorite movies

movies = ["Movie1", "Movie2", "Movie3", "Movie4", "Movie5"]
print(movies)

# Add a new movie to the list

movies = ["Movie1", "Movie2", "Movie3"]
movies.append("NewMovie")

print(movies)

# Remove the first movie from the list

movies = ["Movie1", "Movie2", "Movie3"]
movies.pop(0)

print(movies)

# Sort a list of numbers in ascending order

numbers = [5, 2, 9, 1, 3]
numbers.sort()

print(numbers)

# Reverse a list

numbers = [1, 2, 3, 4, 5]
numbers.reverse()

print(numbers)

# Find the largest number in a list

numbers = [10, 45, 23, 89, 5]
print("Largest number:", max(numbers))

# Merge two lists into one

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
print(merged_list)

# Access the last element without using index number

numbers = [10, 20, 30, 40]

print(numbers[-1])

# Create a nested list and access inner element

nested_list = [[1, 2], [3, 4], [5, 6]]

print(nested_list[1][0])   # Output: 3

# Count how many times an element appears in a list

numbers = [1, 2, 3, 2, 4, 2]
element = 2

print("Count:", numbers.count(element))





