# Check if a person is eligible to vote

age = int(input("enter the age:"))

if age >= 18:
   print("eligible to vote")

else:
   print("not eligible to vote")
    
# Grade calculator based on marks

marks = int(input("Enter the marks :"))

if marks >= 90:
   print("grade A")

elif marks >= 80:
   print("garde B")

else:
   print("garde C")

# Traffic light simulation

signal=input("enter signal colour:").lower()

if signal == "red":
   print("Stop")

elif signal ==" yellow":
   print("Wait")

elif signal == "green":
   print("Go")

else :
   print("invalid signal")

# ATM withdrawal check

balance = 10000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")

# Check positive, negative, or zero

num= int(input("Enter a number:"))

if num > 0:
   print("Positive")

elif num < 0:
   print("Negative")

else:
   print("Zero")

# Check number within a range

num= int(input("enter a number:"))

if  1 <= num <= 50:
   print("num is within range")

else:
   print("num is not in range")

# Username & password verification

username = input("Enter username: ")
password = input("Enter password: ")

if username == "Diya" and password == "9999":
    print("Login successful")
else:
    print("Invalid credentials")

# Electricity bill calculator

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("Electricity bill =", bill)

# Simple calculator(add,subtract,divide,mul)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")

# Check type of triangle

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
