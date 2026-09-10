# 1.1 Beginner Exercise
# Create a dictionary called my_info with:
# Your first name as key "name"
# Your age as key "age"
# Your major as key "major"

# Declaration of the dictionary
# Use dict for work cus its easier for me to read
My_info = dict(name="Leviticus", age=21, major="CyberSecurity")


# 1.1 Intermediate
# 1. Create a dictionary menu with at least 4 food items and their prices
# 2. Create a dictionary course_credits mapping course names to credit hours (e.g., "CS1350": 3)

# Spongebob refrances cus why not
menu = dict(
    Krabby_patty=1.25, Holographic_meatloaf=10.50, Chum_burger=2.75, Kelp_Shake=3.50
)

# Class course dictionary with my classes
course_credits = dict(CS1350=3, NET2300=3, IS2180=3, IS2350=3)


# 1.1 Advanced
# Create a dictionary weekly_temps that maps each day of the week to a temperature. Use the dict() function
# instead of curly braces.

# Tempature hell probably or maybe just death valley whats really the difference though already using dict function
weekly_temps = dict(
    Monday=103,
    Tuesday=112,
    Wednesday=107,
    Thursday=115,
    Friday=102,
    Saturday=99,
    Sunday=104,
)


# 1.2 Beginner
# Given this dictionary: pet = {"name": "Buddy", "type": "dog", "age": 3} Write code to print the pet's name and age.

# The given table obiously, dont know why im wasting time writng about it but i did
pet = {"name": "Buddy", "type": "dog", "age": 3}
# the print statement I need more time with f strings and i think using .get might be my prefered way to go about it makes things more readable
print(
    f"The name of the pet is {pet.get("name")} and the pet's age is {pet.get("age")}."
)


# 1.2 Intermediate
# 1. Given the pet dictionary above, use get() to safely access the "color" key (which doesn't exist). Print a
# default of "unknown".

# I think thats how you do it I dont really know what the point of that was what situation would I need the defualt for
print(f"The color of the pet is {pet.get("color", "unknown")}")

# 2. Create code that checks if a student passed a course. Use get() with a grades dictionary.

# making a dictionary that goes person then grade person than grade totaly not political by any means at all...
# keys automatically turn into the variable when you make a loop so i can just name something student and it will be the key in the dictionary and then I can use get to get the value of that key
grades = dict(Joe_Biden=68, Bill_Clinton=70, Donald_Trump=50)
for student in grades:
    grade = grades.get(student)
    if grade >= 60:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")

# 1.2 Advanced
# Write code that takes a products dictionary and a product name. Print the price if found, or "Product not available" if not found.
# Test with both existing and non-existing products.

# The worst fast food items I could think of.
Products = {
    "Burger King Taco": 1.99,
    "Taco Bell Crispy Chicken Sandwich Taco": 2.50,
    "Wendys Chili": 3.99,
}
product_name = input(
    "Enter a product name preferably Burger King Taco, Taco Bell Crispy Chicken Sandwich Taco or Wendys Chili: "
)
price = Products.get(product_name)
if product_name in Products:
    print(f"The price of {product_name} is ${price}.")
else:
    print("Product not available.")

# 1.3 Beginner
# Start with an empty dictionary called inventory. Add three items with their quantities (e.g., "apples": 10).
inventory = dict()
inventory["chowder"] = 5
inventory["mung_daal"] = 10
inventory["Truffles"] = 3
inventory["Shnitzels"] = 7

# 1.3 Intermediate
# 1. Given scores = {"Team A": 45, "Team B": 38}, update Team B's score to 52 and add "Team C"
# with 41 points.
# 2. Remove "Team A" using pop() and print what score they had
scores = {"Team A": 45, "Team B": 38}
scores["Team B"] += 14
scores["Team C"] = 41
removed_score = scores.pop("Team A")
print(f"Team A's now removed score was {removed_score}.")

# 1.3 Advanced
# Create a simple shopping cart system:
# 1. Start with an empty cart dictionary
# 2. Add 3 items with prices
# 3. Update the price of one item
# 4. Remove one item and print what was removed
# 5. Print the final cart
# Bonus: Calculate and print the total price of remaining items.

cart = {}
cart["Overly Expensive Framework Laptop"] = 2200.99
cart["Logitech Pro X2 Superstrike"] = 179.99
cart["Ninja Fx Zero Artisan Mousepad"] = 45.99

cart["Logitech Pro X2 Superstrike"] = 159.99

removed_item = cart.pop("Ninja Fx Zero Artisan Mousepad")
print(f"Removed item: {removed_item}")

total = sum(cart.values())
print(f"final total ${total}")
