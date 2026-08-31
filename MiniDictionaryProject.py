# Contact records: name -> dictionary of details
contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}
# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.

call_log = {
    "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
    "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
    "Sister": {"Jan": 80, "Mar": 70},
    "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
    "Roommate": {"Feb": 15, "Mar": 25},
    "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
    "Professor": {"Feb": 20, "Mar": 35},
    "Dentist": {"Jan": 10},
}

# Phase 1 — Creating Contact Manager (30 points)
# 1. Create an empty dictionary quick_contacts and add five entries (name → phone string):
# "Mom":"555-1234", "Dad": "555-5678", "Best Friend": "555-8888", "Pizza Place": "555-9999",
# "Work": "555-0000". Print the whole dictionary.
quick_contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Best Friend": "555-8888",
    "Pizza Place": "555-9999",
    "Work": "555-0000",
}
print(quick_contacts)
# 2. Print Mom's number using bracket notation.
print("Ya ma's number is:", quick_contacts["Mom"])

# 3. Update Dad's number to "555-4321".
contact_book["Dad"]["phone"] = "555-4321"
# 4. Add "Dentist": "555-2222".
quick_contacts["Dentist"] = "555-2222"
# 5. Look up "Grandma" with get(), printing Contact not found when the key is missing. Do not let the
# program crash.
print("Grandma's number is:", quick_contacts.get("Grandma", "Not found"))

# 6. Print the updated dictionary.
print("The updated quick contact dictionary is:", quick_contacts)

# 7. Remove "Pizza Place" with del.
del quick_contacts["Pizza Place"]
# 8. Remove "Work" with pop(), saving the old number in old_work, and print it.
old_work = quick_contacts.pop("Work")
print("Your old work number was:", old_work)
# 9. Print the number of contacts left with len(), then the names with keys() and the numbers with
# values(), each wrapped in list().
print("The number of quick contacts left is:", len(quick_contacts))
# We lost the pizza place :( and replaced the work number
print("The names of those contacts are:", list(quick_contacts.keys()))
print("The numbers of those contacts are:", list(quick_contacts.values()))

# Phase 2 — Per-Contact Statistics: Nested Iteration (40 points)
# Loop over call_log (given above) with items(). The value of each entry is itself a dictionary, so you will need
# a second, inner loop (or sum() / len()on the inner dictionary).
# For each contact, compute and print:
# how many months they were called (month(s)),
# total minutes across all months,
# average minutes per month, to 2 decimal places,
# their busiest month and its minutes.
# While you are here, build a dictionary named total_minutes mapping each contact name to their total
# minutes. Every later phase depends on total_minutes, so build it now.
