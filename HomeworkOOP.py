# Exercise 1
# Write a class called Dog (with just pass inside). Create two instances — one named "Buddy" (breed: Golden
# Retriever) and one named "Luna" (breed: Poodle). Set their name and breed attributes after creation, then
# print both names.
# Expected output:

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


class Car:
    def set_info (self,color,brand):
        self.color = color
        self.brand = brand
        
    