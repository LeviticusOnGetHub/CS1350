# 3.1 Beginner
# Given:
# inventory = {"apples": 50, "bananas": 30, "oranges": 25}
# 1. Print each product name using default iteration.
# 2. Calculate total items using values().
# 3. Print each product with quantity using items().

# The opening dictionary
inventory = {"apples": 50, "bananas": 30, "oranges": 25}

# Print names with defualt iteration
print("Product names:")
for product in inventory:
    print(product)

# Printing
total_count = sum(inventory.values())
print("Total items:", total_count)

print("Products with quantity:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

# Intermediate
# Given:
# prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
# 1. Print products sorted alphabetically.
# 2. Print products sorted by price (cheapest first).
# 3. Find and print the most expensive item using items().

# The initial dictionary
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

# print products alphabetical order
print("Products sorted alphabetically:")
for product in sorted(prices):
    print(f"{product}: ${prices[product]}")

print("Products sorted by price (cheapest first):")
for product, price in sorted(prices.items(), key=lambda item: item[1]):
    print(f"{product}: ${price}")

most_expensive_product, most_expensive_price = max(
    prices.items(), key=lambda item: item[1]
)
print(
    "Most expensive item:",
    f"{most_expensive_product}: ${most_expensive_price}",
)

# Advanced
# Given: temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}
# 1. Calculate average temperature using values().
# 2. Find the hottest and coldest days in a single loop.
# 3. Count how many days were above the average.

temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

# calculating the avarage temprture
# take the sum of everything and divide them by the number of days using len
avg_temp = sum(temps.values()) / len(temps)

print("The average trmpature is:", avg_temp)

# finding the hottest and coldest days in a loop
hottest_day = max(temps, key=temps.get)
coldest_day = min(temps, key=temps.get)
print("The hottest day is:", hottest_day)
print("The coldest day is:", coldest_day)

# counter for how many days were above the average tempature
outlier_days = 0
for temp in temps.values():
    if temp > avg_temp:
        outlier_days += 1
print("The number of outlier days is:", outlier_days)

# Beginner 3.2
# Given:products = {"laptop": {"price": 999, "stock": 15},"phone": {"price": 699, "stock": 50}}
# 1. Print the laptop's price.
# 2. Print each product with its stock level.

# The initial dictionary
products = {"laptop": {"price": 999, "stock": 15}, "phone": {"price": 699, "stock": 50}}

print("The laptops price is:", products["laptop"]["price"])

# each proudcts and the quantity of stock
print("The quantity of the items are below:")
for product, details in products.items():
    print(f"{product}: {details["stock"]}")

# Intermediate 3.2
# 1. Given two lists, create a dictionary using zip():
# countries = ["USA", "Canada", "Mexico"]
# capitals = ["Washington", "Ottawa", "Mexico City"]
# 2. Add a new product "tablet": {"price": 449, "stock": 30} to products.
# 3. Safely remove all products with stock < 20 from a dictionary.

# Creating the two dictionaries using zip()
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]
countries_with_capitals = dict(zip(countries, capitals))
print("The given countries with their capitals are:", countries_with_capitals)

# adding a new product to the previous products dictionary
products["tablet"] = {"price": 449, "stock": 30}

# removing everything with more than 20 units
# should of named that differently looks like a tounge twister
for product in list(products.keys()):
    if products[product]["stock"] < 20:
        del products[product]

# Advanced 3.2
# Given: company = {"Engineering": {"Alice": 95000, "Bob": 85000}, "Marketing": {"Carol": 75000, "Dave": 70000}}
# 1. Print all employees with their salaries (nested iteration).
# 2. Calculate the average salary per department.
# 3. Find the highest-paid employee across all departments.

company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000},
}

# printing all workers and their salaries
print("Every worker and their salary grouped by department down below:")
for department, employees in company.items():
    print(f"department: {department}")
    for employee, salaries in employees.items():
        print(f"{employee} {salaries}")

# looking for the avarage salary per department
most_paid_employee, most_paid_salary = max(
    (
        (employee, salary)
        for employees in company.values()
        for employee, salary in employees.items()
    ),
    key=lambda item: item[1],
)
print(f"The highest-paid employee is {most_paid_employee} with ${most_paid_salary}")


# Week 2 part 2
# Beginner 3.1
# 1. Create a set called vowels containing all vowels (a, e, i, o, u).
# 2. Create a set from the list [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]. How many elements does it have?
# 3. What's wrong with this code? empty = {}

vowels = set({"a", "e", "i", "o", "u", "y"})

number_list = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print("The number list has", len(number_list), "unique elements in it")
print("The set of vowels is", vowels)

# it makes an empty dictionary and I assume you wanted us to make sets

# Intermediate 3.1
# 1. Given text = "mississippi", create a set of all unique characters. How many unique letters are there?
# 2. Remove duplicates from this list and convert back to a list: emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
# 3. Why does this fail? s = {[1, 2], [3, 4]}

text = "mississippi"
unique_characters = set(text)
print(
    "the unique characters in the word mississippi are:",
    sorted(
        unique_characters,
    ),
)
print(
    "the amount of unique characters in the word mississippi is:",
    len(unique_characters),
)

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = list(set(emails))
print("The list of unique emails are:", unique_emails)

# number three fails because sets cant have maluable elaments
# the numberlist from before was made into a set to remove duplicates
# It still exists as a list

# Advanced 3.1
# 1. Compare the time to check if 999999 is in a set vs a list of 1 million numbers.
# 2. Create a frozenset and use it as a dictionary key.
# 3. Given a list of tuples representing edges in a graph, create a set of unique nodes:
# edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
# Expected: {1, 2, 3, 4}

# import system time so we can measure for later
import time

# start the number list variable and make it fat using range and we dont eant to type out a million numbers
# we can turn it into a set rather easy by just making a new variable and start calling the list a set with set()
number_list = list(range(1, 1000001))
number_set = set(number_list)

# make a start time variable to start the stopwatch
stopwatch_go = time.time()
999999 in number_list
stopwatch_stop = time.time()
print(
    "The time taken to see if 999999 is in the list is", stopwatch_stop - stopwatch_go
)

stopwatch_go = time.time()
999999 in number_set
stopwatch_stop = time.time()
print("The time taken to see if 999999 is in the set is", stopwatch_stop - stopwatch_go)

Flying_Wyverns = frozenset(
    [
        "Arkveld",
        "Rey Dau",
        "Astalos",
        "Seething Bazelgeuse",
        "Silverwind Nargacuga",
        "Gogmazios",
    ]
)
Flying_Wyverns = {Flying_Wyverns: "all flying wyverns"}
print("The dictionary is:", Flying_Wyverns)

edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
unique_nodes = set()
for edge in edges:
    unique_nodes.update(edge)
print("The list of unique nodes are:", unique_nodes)

# Beginner
# Given:a = {1, 2, 3, 4} b = {3, 4, 5, 6}
# 1. Find all unique numbers (union).
# 2. Find numbers in both sets (intersection).
# 3. Find numbers only in set a (difference).

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# the union sign took me a weird amount of time to find on my keyboard thought it was a backslash for a week stright
print("the uniuon numbers are", a | b)
print("the intersecting numbers between sets are:", a & b)
print("the numbers only in set a are", a - b)
# just going above and beyond look at me shooting for the stars
print("the numbers only in set b are", b - a)

# Intermediate
# Given: morning_shift = {"Alice", "Bob", "Carol"} evening_shift = {"Carol", "Dave", "Eve"} weekend_shift = {"Alice", "Eve", "Frank"}
# 1. Find employees who work ALL shifts.
# 2. Find employees who work at least one shift (any shift).
# 3. Find employees who ONLY work morning (not evening or weekend).
# 4. Find employees who work exactly one shift.

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

all_shifts = morning_shift & evening_shift & weekend_shift
print("The employees who work all shifts are", all_shifts)

any_shift = morning_shift | evening_shift | weekend_shift
print("the employees that yk actually work are", any_shift)

only_morning = morning_shift - evening_shift - weekend_shift
print("the employees that only work the morning shift are ", only_morning)

exactly_one_shift = (
    morning_shift - evening_shift - weekend_shift
    | evening_shift - morning_shift - weekend_shift
    | weekend_shift - morning_shift - evening_shift
)
print("the employees that only work one shift are", exactly_one_shift)

# Advanced
# Given: prereqs_met = {"Alice", "Bob", "Carol", "Dave"} has_space = {"Bob", "Carol", "Eve", "Frank"} paid_tuition = {"Alice", "Carol", "Eve"}
# 1. Find students eligible to enroll (must meet ALL three criteria).
# 2. Find students who met prereqs but haven't paid tuition.
# 3. Find students who need to meet prereqs OR pay tuition (missing at least one).

prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

eligible_students = prereqs_met & has_space & paid_tuition
print("the students completely eligible for enrollment are:", eligible_students)

qualified_but_unpaid = prereqs_met - paid_tuition
print(
    "the students who are qualified but havent paid tuition are:", qualified_but_unpaid
)

# I did it for fun
paid_but_unqualified = paid_tuition - prereqs_met
print("the students who have paid but arent qualified are:", paid_but_unqualified)

missing_either_or = (
    (prereqs_met - has_space - paid_tuition)
    | (has_space - prereqs_met - paid_tuition)
    | (paid_tuition - prereqs_met - has_space)
)
print("the students missing something are", missing_either_or)

# Beginner
# 1. Create a set {1, 2, 3}, add 4, and remove 1.
# 2. Create a set comprehension that generates all even numbers from 0-20.
# 3. Use discard() vs remove() to safely try removing an element that doesn't exist.
