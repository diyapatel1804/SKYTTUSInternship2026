name = "Diya"
age = 21
city = "Ahmedabad"

print(name, age, city)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

name = input("Enter your name: ")
print(name.upper())

birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year
print("Your age is:", age)

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("Area of rectangle:", area)

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

average = (a + b) / 2
print("Average =", average)

