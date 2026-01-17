# Create base class animal and subclasses dog and cat
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

Dog().speak()
Cat().speak()

# Create class hiearchy for vehicle ,car ,electric car

class Vehicle:
    def move(self):
        print("Vehicle moving")

class Car(Vehicle):
    def fuel(self):
        print("Car uses fuel")

class ElectricCar(Car):
    def charge(self):
        print("Electric car charging")

e = ElectricCar()
e.move()
e.fuel()
e.charge()

# method overriding

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

Child().show()

# Multiple Inheritance

class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()

# Polymorphism

class Circle:
    def area(self):
        print("Circle area")

class Rectangle:
    def area(self):
        print("Rectangle area")

def find_area(shape):
    shape.area()

find_area(Circle())
find_area(Rectangle())

# Bank system

class BankAccount:
    def interest(self):
        pass

class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings interest applied")

class CurrentAccount(BankAccount):
    def interest(self):
        print("No interest for current")

SavingsAccount().interest()
CurrentAccount().interest()

# private attributes and getter methods

class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

p = Person()
p.set_age(21)
print(p.get_age())

# teacher and student

class Teacher:
    def teach(self):
        print("Teaching")

class Student(Teacher):
    def study(self):
        print("Studying")

s = Student()
s.teach()
s.study()

# Music player

class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing from Spotify")

Spotify().play()

# Super() Inheritance

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

B().show()
