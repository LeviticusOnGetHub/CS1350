# Exercise 1
# Write a class called Dog (with just pass inside). Create two instances — one named "Buddy" (breed: Golden
# Retriever) and one named "Luna" (breed: Poodle). Set their name and breed attributes after creation, then
# print both names.
# Expected output:

# Exercise 2
# Take your Dog class from Exercise 1. Add a method called bark that prints "<name> says Woof!" using
# self.name. Call bark() on both of your dog instances.

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