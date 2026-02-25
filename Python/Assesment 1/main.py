# PROGRAM 1: Create a custom math module and import it

print("Create a custom math module and import it")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(add(5, 3))
print(sub(10, 4))



# PROGRAM 2: Create a module to perform string operations

print("Create a module to perform string operations")

def to_upper(text):
    return text.upper()

def reverse(text):
    return text[::-1]

print(to_upper("hello"))
print(reverse("python"))


# PROGRAM 3: Use random module to generate 5 random integers

print("Use random module to generate 5 random integers")

import random
for i in range(5):
    print(random.randint(1, 100))


# PROGRAM 4: Use datetime module to display current date and time

print("Use datetime module to display current date and time")

from datetime import datetime
print(datetime.now())


# PROGRAM 5: Use math module to find factorial of a number

print("Use math module to find factorial of a number")

import math
print(math.factorial(5))


# PROGRAM 6: Create a package shapes with modules for circle and rectangle

print("Create a package shapes with modules for circle and rectangle")

def circle_area(r):
    return 3.14 * r * r

def rectangle_area(l, w):
    return l * w

print(circle_area(5))
print(rectangle_area(4, 6))



# PROGRAM 7: Import multiple functions from one module and use them

print("Import multiple functions from one module and use them")

print(add(8, 2))
print(sub(9, 3))



# PROGRAM 8: Write a program to shuffle a list using random module

print("Write a program to shuffle a list using random module")

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)


# PROGRAM 9: Write a program to calculate the difference between two dates

print("Write a program to calculate the difference between two dates")

from datetime import date
d1 = date(2025, 1, 1)
d2 = date(2025, 1, 10)
print("Days difference:", (d2 - d1).days)


# PROGRAM 10: Use os module to list files in a directory

print("Use os module to list files in a directory")

import os
print(os.listdir("."))
