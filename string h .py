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


