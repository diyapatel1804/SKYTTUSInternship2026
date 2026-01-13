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


