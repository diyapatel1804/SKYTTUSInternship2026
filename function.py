# Function to check prime number

def is_prime(n):
    if n<=1:
        return  False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))

# Function to reverse a string

def reverse_string(s):
    return s[::-1]\
    
print(reverse_string("hello"))

# Function to find factorial

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factorial(5))

# Function to check palindrome

def is_palindromne(word):
    return word == word[::-1]

print(is_palindromne("madam"))

# function to count vowels

def count_vowels (s):
    count =0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count 

print(count_vowels("Hello"))

#  Function to merge two lists

def merge_lists(a,b):
    return a + b

print(merge_lists([1,2],[3,4]))

# Function to find GCD of two numbers

def gcd(a,b):
    while b !=0:
        a,b =b,a % b
    return a

print(gcd(12,18))

# Function to find area of rectangle

def area_rectangle(length,width):
    return length * width

print(area_rectangle(5,4))

# Function to check Armstrong number

def is_armstrong(num):
    s=0
    temp = num
    digits = len(str(num))
    while temp > 0:
        s += (temp % 10) ** digits
        temp //=10
    return s == num

print(is_armstrong(153))