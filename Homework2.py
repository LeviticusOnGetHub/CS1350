# 2.1 Beginner Exercise
# Which of these are valid dictionary keys? Write "valid" or "invalid" and explain why:
# a) "student_name" # valid (because strings are immutable you put it in the notes)
# b) [1, 2, 3] # invalid (lists are mutable you put it in the notes)
# c) 100 # valid (reason: integers are immutable you put it in the notes)
# d) ("x", "y") # valid (reason: tuples are immutable you put it in the notes)
# e) {"a": 1} # invalid (dictionaries are mutable you put it in the notes)
# f) frozenset({1,2}) # valid (reason: frozensets are immutable you put it in the notes)

# 2.1 Intermediate Exercise
# 1. This code has an error. Find and fix it:
# locations = {[40.7, -74.0]: "New York", [34.0, -118.2]: "Los Angeles"}

locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}

# 2. What will this print? Predict the output, then verify:
data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)
print(len(data))
# ANSWER a:3 and b:4 because its following the latest change to the key the length is probably 2 because the values got updated rather than making new ones

# 3. Investigate: What is the hash value of your name? What about the number 100?
my_name = {"Leviticus": 100}
print(hash("Leviticus"))
print(hash(100))

# 2.1 Advanced Exercise
# 1. Create a dictionary that tracks game high scores using tuples as keys where each tuple contains
# (player_name, game_name), and values are the scores. Add at least 3 entries and retrieve one score.

# Monster hunter characters boo Nata
Scores = {
    ("Gemma", "Monster Hunter Wilds"): 8008132,
    ("Alma", "Monster Hunter Freedom_Unite"): 943534,
    ("Nata", "Monster Hunter Dos"): -9999999,
    ("Arkveld", "Monster Hunter World"): 69696969,
}
# alma plays freedom unite and gets a score of 943534 shes a tryhard
player_name = "Alma"
game_name = "Monster Hunter Freedom_Unite"
score = Scores.get((player_name, game_name))
print(f"Score for {player_name} in {game_name}: {score}")

# 2. Write code that compares the time to check if an element exists in a list vs a dictionary with 100,000
# elements. Print which is faster and by how much.
# Not gonna lie I dont know how to do that heres what I can do


#List_Data = list(range(100000))
#Dict_Data = dict(range(100000))


# 2.2 Beginner Execerise
# Given this dictionary:
# temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
# Write code to:
# 1. Print all the day names using keys()
# 2. Print all the temperatures using values()
# 3. Print how many days are in the dictionary

# dictionary restated again very redudant notes
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
# printing the keys, values, and length of the dictionary
print("the days are:", list(temps.keys()))
print("the temperatures are:", list(temps.values()))
print("The amount of days in the list is:", len(temps))

# 2.2 Intermediate
# 1. Find and print the highest and lowest temperatures from temps.
# 2. Check if "Friday" is in the dictionary using the in operator. Print an appropriate message.
# 3. Use setdefault() to add "Thursday" with a value of 70, but only if it doesn't exist.
# 4. Demonstrate that views are dynamic: create a keys view, add a new day, show the view updated.

# finding the highest and lowest temperatures and than print
highest_temp = max(temps.values())
lowest_temp = min(temps.values())
print(f"Highest: {highest_temp}, Lowest: {lowest_temp}")

#checking if friday is in the dictionary and nah print nah 
if "Friday" in temps:
    print("Friday is in the dictonary")
else:
    print("Friday is not in the dictionary")

# using setdefault to add thursday because it doesnt exist you knew that whyd you word it like that
temps.setdefault("Thursday", 70)
print(temps)

# making key views and printing it as is pre addition
keys_view = temps.keys()
print("Keys before:", keys_view)
# adding friday and printing again shoud of probably done this using setdefault but oh well
temps["Friday"] = 76
print("Keys after:", keys_view)

# 2.2 Advanced
# Given a prices dictionary:
# prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
# Write code that:
# 1. Calculates the total value and average price
# 2. Finds the most and least expensive items (both name and price)
# 3. Compares memory usage between prices.keys() and list(prices.keys())
# 4. Uses update() to add 3 new products, then shows all products

# importing sys it checks the memory usage that explanation is more for me when i look this over later
import sys

# dictionary
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

# calculating total and avarage price used len because dictionaries can change instead of using 4
total = sum(prices.values())
average = total / len(prices)

# finding most and expensive items using max and min I have no clue what lambda does just added it through the notes
# im not sure but i think it has somthing to do with .items and item [1] prints the values of whatever shows up first with the constraints
most_expensive_item = max(prices.items(), key=lambda item: item[1])
least_expensive_item = min(prices.items(), key=lambda item: item[1])

# orinting all the things you wanted
print("Total value:", total)
print("Average price:", average)
# Lambda made them tuples so I had to use indexing
print("Most expensive item:", most_expensive_item[0], most_expensive_item[1])
print("Least expensive item:", least_expensive_item[0], least_expensive_item[1])

keys_view = prices.keys()
keys_list = list(prices.keys())
print("Memory of keys,:", sys.getsizeof(keys_view), "bytes")
print("Memory of list:", sys.getsizeof(keys_list), "bytes")

prices.update(
    {
        "Electric Automatic Litter Box": 199,
        "Air Pods Pro 2": 129,
        "Artaisan Mousepad": 39,
    }
)
print("All products after update:", prices)

# 2.3 Beginner
# colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
# 1. Use a for loop with .items() to print each fruit and its color:

colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for fruit, color in colors.items():
    print(fruit, ":", color)

# 2. 

# 2.2 Intermediate
# Given prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}, write a loop using items()
# that prints each item with 10% tax added:
# coffee: $4.50 + tax = $4.95
# 2. Count how many items cost more than $4.00 using iteration.
# 3. Use tuple unpacking to swap two variables x = 10 and y = 20 in one line.
# 4. Given a list [1, 2, 3, 4, 5], use extended unpacking to get the first element, last element, and
# middle elements separately.


prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}

# Items automatically assign to the keys 
for item, price in prices.items():
    total_price = price * 1.10
    print(f"{item}: ${price} + tax = ${total_price}")
    
    
count = 0
for price in prices.values():
    if price > 4.00:
        count += 1

print("Items over $4.00:", count)

x = 10
y = 20

x, y = y, x

print("x:", x)
print("y:", y)

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)

# 2.3 Advanced
# Given a scores dictionary:
# scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
# 1. Use items() with the max() function and a lambda to find the student with the highest score.
# 2. Create two new dictionaries: passed (grade ≥ 70) and failed (grade < 70) using iteration.
# 3. Calculate the class average and create a dictionary showing each student's deviation from the average.
# 4. Write a performance test comparing items() iteration vs keys() with lookup for a dictionary with
# 50,000 entries.


scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

# top student matches to whatever key variable comes out on t
top_student, top_score = max(scores.items(), key=lambda item: item[1])

print(f"Top Student: {top_student} with a score of {top_score}")

passed = {}
failed = {}

for student, score in scores.items():
    if score >= 70:
        passed[student] = score
    else:
        failed[student] = score

print("Passed:", passed)
print("Failed:", failed)

class_average = sum(scores.values()) / len(scores)

deviations = {student: round(score - class_average, 2) for student, score in scores.items()}

print(f"Class Average: {class_average}")
print("Deviations from Average:", deviations)

# I dont know how to do 4 

