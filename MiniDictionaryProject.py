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
print("Phase 1 Contact Manager")
print(quick_contacts)
# 2. Print Mom's number using bracket notation.
print("Ya ma's number is:", quick_contacts["Mom"])

# 3. Update Dad's number to "555-4321".
contact_book["Dad"]["phone"] = "555-4321"
# 4. Add "Dentist": "555-2222".
quick_contacts["Dentist"] = "555-2222"
# 5. Look up "Grandma" with get(), printing Contact not found when the key is missing. Do not let the program crash.
# How would it crash in the first place
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

print("Phase 2 Contact Activity")

# total minutes gonna be used a ton later make it a dictionary
total_minutes = {}
# looking in call log seperating people who are the keys into contacts and calltime as the items
for contact, calltime in call_log.items():
    # making variables to ilatalize months called
    months_called = 0
    total_time = 0
    # to find busiest times and month in one line using lambda dont know what it did this justin but it got the max values of the for both month and time in one line which is cool still dont know how to use it
    busiest_month, busiest_time = max(calltime.items(), key=lambda x: x[1])
    average = sum(calltime.values()) / len(calltime.values())
    for month, time in calltime.items():
        months_called += 1
        total_time = total_time + time
    print(
        f"{contact}: {months_called} month(s), {total_time} min total, avg: {average:.2f}, busiest: {busiest_month} ({busiest_time})"
    )
    total_minutes[contact] = total_time

# Phase 3 — Flipping the Data & Aggregating with get() (40 points)
# Part A — Month statistics (20 pts)
# call_log is organized by contact. Build a dictionary organized by month instead. Name it month_stats;
# each month maps to a dictionary containing:
# "minutes" — a list of every minute-value recorded that month,
# "total" — the sum of those minutes,
# "avg" — the average, and
# "contacts" — how many contacts were called that month.
# Then print each month sorted by average, highest first, using sorted() with a lambda key.

# new dictionary to hold month stats
month_stats = {}
# for each contact in the call log, process their call times
for contact, calltime in call_log.items():
    # for each month and time in the calltime dictionary
    for month, time in calltime.items():
        # if the month is not already in month_stats, add default values
        if month not in month_stats:
            month_stats[month] = {"minutes": [], "total": 0, "avg": 0, "contacts": 0}
        month_stats[month]["minutes"].append(time)
        month_stats[month]["total"] += time
        month_stats[month]["contacts"] += 1

# calculate the average number of minutes for each month
for month in month_stats:
    # dont count the contacts with 0 minumum 1
    if month_stats[month]["contacts"] > 0:
        month_stats[month]["avg"] = (
            month_stats[month]["total"] / month_stats[month]["contacts"]
        )

print("Phase 3: Aggregations")
# sorting months reversing it because it normally starts from greatest to least and you wanted it other way
for month in sorted(
    month_stats, key=lambda month: month_stats[month]["avg"], reverse=True
):
    # print total of everything avg of everything as floats
    print(
        f"{month}: {month_stats[month]['total']} min total, {month_stats[month]['avg']:.2f} avg ({month_stats[month]['contacts']} contacts)"
    )
# Using the get() accumulation pattern — totals[key] = totals.get(key, 0) + value — and pulling
# each contact's details out of contact_book, build:

# intilialize the dictionaries for our questions from the expected output
minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

# grabbing names and whatever data is in the rest of the contact book dictionary numbers cities and whatnot
for contact, details in contact_book.items():
    # grabbing and going using get and popping in unknown if the key is not found in the contact_book dictionary
    category = details.get("category", "Unknown")
    city = details.get("city", "Unknown")
    # same thing as before but defulting to 0 if tings are not found since were dealing with intergera maybe floats too idk nah just ints i looked
    minutes = total_minutes.get(contact, 0)

    # 1. getting the total minutes per category, using the get() adding minutes to the total for each contact in the category
    minutes_by_category[category] = minutes_by_category.get(category, 0) + minutes

    # 2. getting the total minutes per city, using the get() adding minutes to the total for each contact in the city
    minutes_by_city[city] = minutes_by_city.get(city, 0) + minutes

    # 3. getting the contact count per city, using the get() andding one to the count for each contact in the city
    contacts_per_city[city] = contacts_per_city.get(city, 0) + 1
# printing all the goobldy gook
print("Minutes by category:", minutes_by_category)
print("Minutes by city:", minutes_by_city)
print("Contacts per city:", contacts_per_city)

# Expected Output
# === Phase 3: Aggregations ===
# Monthly summary (sorted by average, highest first):
# Jan: 515 min total, 85.83 avg (6 contacts)
# Feb: 460 min total, 76.67 avg (6 contacts)
# Mar: 595 min total, 85.00 avg (7 contacts)
# Minutes by category: {'Family': 640, 'Friend': 640, 'Work': 280, 'Business': 10}
# Minutes by city: {'Fort Wayne': 585, 'Chicago': 375, 'Indianapolis': 610}
# Contacts per city: {'Fort Wayne': 4, 'Chicago': 2, 'Indianapolis': 2}

# Phase Fore
# Each of the following must be a one-line dictionary comprehension. A for loop that produces the same
# answer earns half credit.
# 1. phone_book — every contact name mapped to just their phone number.

print("Phase 4")

# we get to use details again instead of using new crap pop in phone to get the spefic phone numbers
phone_book = {name: details["phone"] for name, details in contact_book.items()}

# 2. local_contacts — name → phone, but only for contacts whose city is "Fort Wayne".
#  on to local contacts we go, same song and dance as before but throw in an if statement to filter for the Fort Wayne
local_contacts = {
    name: details["phone"]
    for name, details in contact_book.items()
    if details.get("city") == "Fort Wayne"
}

# 3. activity_level — every contact mapped to "Frequent" if their total minutes are 200 or more,
# otherwise "Occasional". (Build this from total_minutes.)

# same bones as before yet again but we use everything from before in bits use total minutes from before to get all our numbers
# and see if there over 200 minutes to calssify them as frequent or occasional callers
activity_level = {
    name: "Frequent" if total_minutes.get(name, 0) >= 200 else "Occasional"
    for name in contact_book
}
# Print
print("Phone book:", phone_book)
print("Local contacts (Fort Wayne):", local_contacts)
print("Activity level:", activity_level)

# Expected Output
# === Phase 4: Comprehensions ===
# Phone book: {'Mom': '555-1234', 'Dad': '555-4321', 'Sister': '555-7777', 'Best
# Friend': '555-8888', 'Roommate': '555-3141', 'Boss': '555-0000', 'Professor':
# '555-2718', 'Dentist': '555-2222'}
# Local contacts (Fort Wayne): {'Mom': '555-1234', 'Dad': '555-4321', 'Roommate':
# '555-3141', 'Professor': '555-2718'}
# Activity level: {'Mom': 'Frequent', 'Dad': 'Occasional', 'Sister': 'Occasional',
# 'Best Friend': 'Frequent', 'Roommate': 'Occasional', 'Boss': 'Frequent',
# 'Professor': 'Occasional', 'Dentist': 'Occasional'}

# Phase five
# Part A — Classify (14 pts)
# Write a helper function get_tier(minutes) that returns:
# Tier Total minutes
# Platinum 400 or more
# Gold 200 – 399
# Silver 100 – 199
# Bronze 50 – 99
# Inactive below 50
# Print every contact with their total and tier, formatted Mom: 355 min (Gold).

print("Phase 5")

# turing contacts into tiers based on total time talked to very human throw it in a dicronary
contact_tiers = {}


# get tiers using minutes that weve been using for awhile luckly we can throw this into a pretty short if statement to get the tiers and print them out in the format you wanted
def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"


# Part B — Count (12 pts)
# Count how many contacts fall in each tier using a loop and if/elif. Print each count.

# kinda the same as before but we start with a counter dictionary to get all the minutes for parcing through each tier
tier_counter = {"Platinum": 0, "Gold": 0, "Silver": 0, "Bronze": 0, "Inactive": 0}
for contact, minutes in total_minutes.items():
    if minutes >= 400:
        tier = "Platinum"
    elif minutes >= 200:
        tier = "Gold"
    elif minutes >= 100:
        tier = "Silver"
    elif minutes >= 50:
        tier = "Bronze"
    else:
        tier = "Inactive"

    tier_counter[tier] += 1
    contact_tiers[contact] = tier

# Part C — Rank (14 pts)
# Using loops over total_minutes.items():
# 1. Find and print the most-contacted person and their minutes.
# 2. Find and print the least-contacted person and their minutes.
# 3. Print the grand total of all minutes and the average per contact (2 decimal places).
# 4. Print every contact whose total is above that average.

# finding the most and least contacted people using min and max and inatilitizing them as variables to be used later
most_name = max(total_minutes, key=total_minutes.get)
least_name = min(total_minutes, key=total_minutes.get)

# finding most and least contacted as variables to be used later in the print statements
most_contacted = (most_name, total_minutes[most_name])
least_contacted = (least_name, total_minutes[least_name])

# calculating the total and average minutes using sum and len to get the total minutes and average per contact
total_minutes_sum = sum(total_minutes.values())
average_minutes = total_minutes_sum / len(total_minutes)


print(f"Most contacted: {most_contacted[0]} ({most_contacted[1]} min)")
print(f"Least contacted: {least_contacted[0]} ({least_contacted[1]} min)")
print(f"Total minutes: {total_minutes_sum}")
print(f"Average per contact: {average_minutes:.2f}")


for contact, minutes in total_minutes.items():
    if minutes > average_minutes:
        print(f"{contact}: {minutes}")


# Sister: 150 min (Silver)
# Best Friend: 600 min (Platinum)
# Roommate: 40 min (Inactive)
# Boss: 225 min (Gold)
# Professor: 55 min (Bronze)
# Dentist: 10 min (Inactive)
# --- Tier Distribution ---
# Platinum: 1
# Gold: 2
# Silver: 2
# Bronze: 1
# Inactive: 2
# --- Top and Bottom ---
# Most contacted: Best Friend (600 min)
# Least contacted: Dentist (10 min)
# Total minutes: 1570
# Average per contact: 196.25
# --- Above Average Contacts ---
# Mom: 355
# Best Friend: 600
# Boss: 225

# --- Above Average Contacts ---
# Mom: 355
# Best Friend: 600
# Boss: 225

# Phase 6 — The Contact Hub Report (20 points)
# Bring it together. Print one aligned table of every contact, sorted by total minutes, highest first, using
# sorted() with a lambda. Each row shows name, category, city, total minutes, and tier. Finish with a one-line
# summary.
# Use f-string field widths for alignment: f"{name:<12}" left-aligns in 12 characters, f"{total:>8}" right-
# aligns in 8.

# printing the name, category, city, minutes, and tier of each contact in a formatted table and using allignment

print("Phase 6")
print(f"{'Name':<12} {'Category':<10} {'City':<15} {'Minutes':<8} {'Tier':<10}")

#
for name, total in sorted(
    total_minutes.items(), key=lambda item: item[1], reverse=True
):
    details = contact_book[name]
    print(
        f"{name:<12} {details['category']:<10} {details['city']:<15} {total:>8} {contact_tiers[name]:<10}"
    )

print(
    f"{len(total_minutes)} contacts | {total_minutes_sum} total minutes | {average_minutes:.2f} average"
)

# Expected Output
# === Phase 6: Contact Hub Report ===
# Name Category City Minutes Tier
# -------------------------------------------------------
# Best Friend Friend Indianapolis 600 Platinum
# Mom Family Fort Wayne 355 Gold
# Boss Work Chicago 225 Gold
# Sister Family Chicago 150 Silver
# Dad Family Fort Wayne 135 Silver
# Professor Work Fort Wayne 55 Bronze
# Roommate Friend Fort Wayne 40 Inactive
# Dentist Business Indianapolis 10 Inactive
# -------------------------------------------------------
# 8 contacts | 1570 total minutes | 196.25 average
