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

# Beginner
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

# Intermediate
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

# Advanced
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
most_paid_employee, most_paid_salary = max(((employee, salary)
        for employees in company.values()
        for employee, salary in employees.items()
    ),
    key=lambda item: item[1],
)
print(f"The highest-paid employee is {most_paid_employee} with ${most_paid_salary}")
