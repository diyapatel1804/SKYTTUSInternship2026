# Calculate the remainder of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

remainder = a % b
print("Remainder =", remainder)

# Check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Compare two numbers and print the larger one
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Larger number is:", a)
elif b > a:
    print("Larger number is:", b)
else:
    print("Both numbers are equal")

# Calculate square and cube of a number
num = int(input("Enter a number: "))

print("Square =", num * num)
print("Cube =", num * num * num)

# Check if two entered numbers are equal

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")

# Print True if both numbers are positive, else False

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a > 0 and b > 0)

# Convert float to integer

num = float(input("Enter a float number: "))

print("Integer value:", int(num))

# Take a number as string, convert to int, and multiply by 10

num_str = input("Enter a number: ")
num = int(num_str)

print("Result =", num * 10)

# Use AND (&) / OR operators to check multiple conditions

age = int(input("Enter age: "))
salary = int(input("Enter salary: "))

if age >= 18 and salary >= 10000:
    print("Eligible")
else:
    print("Not eligible")

# Divide two numbers and print quotient and remainder

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

quotient = a // b
remainder = a % b

print("Quotient =", quotient)
print("Remainder =", remainder)
