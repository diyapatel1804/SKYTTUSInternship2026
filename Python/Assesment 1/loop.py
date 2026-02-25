# print numbers from 1 to 10

for i in range(1,11):
 print(i)

# Multiplication number for a given number

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# Factorial of number

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial =", fact)

# First N fibonacci numbers

n = int(input("Enter N: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Check if a number is prime

n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

# Reverse a number (e.g., 123 → 321)

n = int(input("Enter a number: "))
rev = 0

while n != 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reversed number =", rev)

# Count digits in a number

n = int(input("Enter a number: "))
count = 0

while n != 0:
    count += 1
    n //= 10

print("Number of digits =", count)

# Sum of even numbers between 1 and 100

sum_even =0
for i in range (1,101):
    if i % 2==0:
        sum_even +=i

print("sum of even numbers =",sum_even)

# Pyramid Pattern

rows = int(input("enter number of rows:"))

for i in range(1,rows+1):
    print("* "* i)

# Find all divisors of a number

n=int(input("Enter a number: "))

print("Divisors are: ")
for i in range (1,n+1):
    if n % i == 0:
        print(i)