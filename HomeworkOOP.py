# Exercise 1
# Write a class called Dog (with just pass inside). Create two instances — one named "Buddy" (breed: Golden
# Retriever) and one named "Luna" (breed: Poodle). Set their name and breed attributes after creation, then
# print both names.
# Expected output:

# Exercise 2
# Take your Dog class from Exercise 1. Add a method called bark that prints "<name> says Woof!" using
# self.name. Call bark() on both of your dog instances.

from unicodedata import name


class Dog:
    def bark (self):
        print(f"{self.name} says Woof!")

buddy = Dog()
buddy.name = "Buddy"
buddy.breed = "Golden Retriever"

Luna = Dog()

Luna.name = "Luna"
Luna.breed = "Poodle"

print(buddy.name)
print(Luna.name)
buddy.bark()
Luna.bark()

# Exercise 3
# 1. Starting from your Car class, add a method set_info(self, color, brand).
# 2. Create two cars. Give one "red", "Toyota" and the other "blue", "Honda".
# 3. Print each car's color and brand.

# Exercise 3 continued
# 1. Rewrite your Car class so color and brand are set inside __init__.
# 2. Create a car: my_car = Car("Green", "Toyota").
# 3. Print my_car.color and my_car.brand to confirm it works.

class Car:
    def set_info (self,color,brand):
        self.color = color
        self.brand = brand

MyCar = Car()
MyCar.color = "red"
MyCar.brand = "Toyota"

MomsCar = Car()
MomsCar.color = "blue"
MomsCar.brand = "Honda"

print("The first car is a:", MyCar.color, MyCar.brand)
print("The second car is a:", MomsCar.color, MomsCar.brand)


# I made it another color so i wouldnt get confused     
class Car:
    def __init__ (self,color,brand):
        self.color = color
        self.brand = brand

My_Car = Car("Green","Toyota")

print("The new car is a:", My_Car.color, My_Car.brand)

# Create a Person class where _age is private. Add a get_age() method that returns the age, and a set_age()
# method that only allows ages between 0 and 150. Test with valid and invalid values.


class Person:
    def __init__ (self,name,age):
        self.name = name
        self._age = age
    def get_age(self):
        return self._age

    def set_age(self, age):
        if 0 <= age <= 150:
            self._age = age
        else:
            print("an age is beyond the 0-150 range it is invalid")
            return

Unc = Person("Unc",0)
Og = Person("Og",0)

Unc.set_age(50)  # a working age
Og.set_age(200)  # Og is dead

# Exercise 2 (5 min)
# Create a Rectangle class that stores width and height. Add an area property that calculates and returns the
# area. Then add a perimeter property that calculates the perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        # Calculate and return width * height
        return self.width * self.height

    @property
    def perimeter(self):
        # Calculate and return 2 * (width + height)
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print("the area of the sample rectangle:", rect.area)
print("The perimeter of the sample rectangle:", rect.perimeter)


# Exercise 3 (5 min)
# Create a Score class for test scores (0–100). Use @property for the getter and @value.setter for a setter
# that rejects values outside the range. Also add a letter_grade read-only property.

class Score:
    def __init__(self, value=0):
        self._value = 0
        self.value = value # Use setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # Accept only values between 0 and 100
        # Print error if invalid
        if 0 <= new_value <= 100:
            self._value = new_value
        else:
            print("Invalid score. Must be between 0 and 100.")

    @property
    def letter_grade(self):
        # Return "A" for 90+, "B" for 80+, "C" for 70+, "D" for 60+, "F" otherwise
        if self._value >= 90:
            return "A"
        elif self._value >= 80:
            return "B"
        elif self._value >= 70:
            return "C"
        elif self._value >= 60:
            return "D"
        else:
            return "F"
        
A_Score = Score(92)
B_Score = Score(85)
C_Score = Score(72)
D_Score = Score(60)
F_Score = Score(50)

print("a great score is:", A_Score.letter_grade)
print("a good score is:", B_Score.letter_grade)
print("an average score is:", C_Score.letter_grade)
print("a passable score is:", D_Score.letter_grade)
print("a bad score is:", F_Score.letter_grade)

# Exercise 4 (5 min)
# Refactor this flat, procedural student-record script into a Student class with encapsulation. The GPA should be
# private with a setter that rejects values outside 0.0–4.0. Add a display() method and an honors read-only
# property (True if GPA >= 3.5).

# Expected output:
# Alice — Computer Science, GPA: 3.8 (Honors)
# Error: GPA must be between 0.0 and 4.0
# Alice — Computer Science, GPA: 3.2

class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        # Make gpa private with validation (0.0 - 4.0)
        self._gpa = 0.0
        self.gpa = gpa
    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self._gpa = value
        else:
            print("Invalid GPA. Must be between 0.0 and 4.0.")
    @property
    def honors(self):
        # Return True if gpa >= 3.5
        return self._gpa >= 3.5

    def display(self):
        # Print name, major, gpa, and "(Honors)" if applicable
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")
        print(f"GPA: {self._gpa}")
        if self.honors:
            print("(Honors)")
        print()
Alice = Student("Alice", "Computer Science", 3.9)
Alice.display()
Alice.gpa = 4.1
Alice.display()
Alice.gpa = 3.2
Alice.display()


# Exercise 1
# Create an Animal base class with name and a speak() method that prints "<name> makes a sound". Then
# create two derived classes — Cat (with a purr() method) and Dog (with a fetch() method). Instantiate one
# of each and call speak() on both to confirm they inherited it.

# Expected output:
# Whiskers makes a sound
# Buddy makes a sound
# Whiskers is purring
# Buddy is fetching!

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")  
                 
class Cat(Animal):
    def purr(self):
        
        # Print "<name> is purring"
        print(f"{self.name} is purring")
        
class Dog(Animal):
    def fetch(self):
        # Print "<name> is fetching!"
        print(f"{self.name} is fetching!")
        

# Instantiate and test
whiskers = Cat("Whiskers")
buddy = Dog("Buddy")
whiskers.speak()
buddy.speak()
whiskers.purr()
buddy.fetch()

# Exercise 2
# Override the speak() method from Exercise 1 so that Cat.speak() prints "Meow!" and Dog.speak() prints
# "Woof!". Create a list containing one Cat and one Dog, loop over it, and call speak() on each.

# Expected output:
# Whiskers says Meow!
# Buddy says Woof!

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
class Cat(Animal):
    def speak(self):
        # Print "<name> says Meow!"
        print(f"{self.name} says Meow!")
class Dog(Animal):
    def speak(self):
        # Print "<name> says Woof!"
        print(f"{self.name} says Woof!")
        
Whiskers = Cat("Whiskers")
Buddy = Dog("Buddy")
# used print so i can get get a blank line so i can read it better
print()
Whiskers.speak()
Buddy.speak()

# Exercise 3
# Create an Employee class with name and salary set in __init__. Then create a Manager subclass that uses
# super().__init__() to set name and salary, and adds a department attribute. Give Manager a display()
# method that prints all three.

# Expected output:
# Sarah — $85,000, Engineering


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Call super().__init__() for name and salary
        super().__init__(name, salary)
        # Add department
        self.department = department

    def display(self):
        # Print name, salary, and department
        print(f"{self.name} — ${self.salary:,}, {self.department}")
        
Sarah = Manager("Sarah", 85000, "Engineering")

print()
Sarah.display()

# Exercise 4
# Given this diamond hierarchy, predict the MRO of D, then verify by running D.mro(). After that, call
# d.greet() and confirm which class's version runs.

# Expected output:
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]

class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
class C(A):
    def greet(self):
        print("Hello from C")
class D(B, C):
    def greet(self):
        super().greet()

d = D()
print()
print(D.mro())
d.greet()


