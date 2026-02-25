# Handle divison by zero

try:
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    print(a/b)

except ZeroDivisiorError:
    print("Cannot divide by zero")

# Handle invalid integer input

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid integer input")

# Handle file not found error

try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")

# Demonstrate multiple exception blocks

try:
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    print(x / y)
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid input")

# Use finally for resource cleanup

try:
    file = open("test.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program ended")

# Custom exception for invalid age (<18)

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError
    print("Valid age")
except InvalidAgeError:
    print("Age must be 18 or above")

# Handle IndexError in list

try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")

# Two numbers & handle all possible errors

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except Exception as e:
    print("Error:", e)

# Log errors to a file

try:
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    print(x / y)
except Exception as e:
    file = open("error.log", "a")
    file.write(str(e) + "\n")
    file.close()

# Email validation with exception

class InvalidEmail(Exception):
    pass

try:
    email = input("Enter email: ")
    if "@" not in email or "." not in email:
        raise InvalidEmail
    print("Valid email")
except InvalidEmail:
    print("Invalid email format")
