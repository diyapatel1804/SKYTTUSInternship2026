# Car class with atributes like brand,model..

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 5

car = Car("Toyota", "Fortuner")
car.accelerate()
print("Speed:", car.speed)

# Bank account class 

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.balance)

# Student class

class Student:
    def __init__(self, marks):
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s = Student([80, 90, 85])
print("Average:", s.average())

# Rectangle class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(5, 3)
print("Area:", r.area())
print("Perimeter:", r.perimeter())

# Employee class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

e = Employee("Diya", 25000)
e.display()

# Book class

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(self.title, self.author, self.price)

b = Book("Python Basics", "Guido", 499)
b.display()

# Circle class

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

c = Circle(7)
print("Area:", c.area())
print("Circumference:", c.circumference())


# Laptop class

class Laptop:
    def __init__(self, price):
        self.price = price

    def discount(self, percent):
        self.price -= self.price * percent / 100

l = Laptop(50000)
l.discount(10)
print("Price after discount:", l.price)


# Flight class

class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked")
        else:
            print("No seats available")

f = Flight(2)
f.book_seat()

# Shop class

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print(self.products)

s = Shop()
s.add_product("Mobile")
s.add_product("Laptop")
s.show_products()



