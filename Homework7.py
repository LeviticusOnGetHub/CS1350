# Rules
# Use a with statement for every file you open.
# Submission, you can choose either one of the two following options:
# One file per problem: CS1350_HW7_FirstLast_p1.py, CS1350_HW7_FirstLast_p2.py,
#CS1350_HW7_FirstLast_p3.py.

# One file for all three problems: CS1350_HW7_FirstLast.py
# Problem 1: Security Log Splitter and Status Report (50 points)
# File Lecture 1 — use only plain text file operations. Do not use csv, json, or pickle in this problem.
# Your company has two machines, and each one writes a security log. Every log line has this form:
# 2026-10-05 08:03:45 [WARNING] Failed login attempt for user root
# The level in square brackets is always [INFO], [WARNING], or [ERROR]. A log file may contain blank lines,
# which must be ignored.
# Write two functions.
# split_logs(machines)
# machines is a dictionary that maps a machine name to its log file name, for example {"server_a":
# "server_a.log", "server_b": "server_b.log"}.
# Read each machine's log line by line.
# Write every entry to one of three output files according to its level: info.log, warning.log, or
# error.log.

# In the output files, put the machine name and " | " in front of each line so you can tell where it came from.
# server_a | 2026-10-05 08:03:45 [WARNING] Failed login attempt for user root
# The three output files are created fresh on every run (old contents are replaced). Machines are
# processed in dictionary order, and lines keep their original order within each machine.
# Return a nested dictionary of counts: {machine: {"INFO": n, "WARNING": n, "ERROR": n}}.
# print_report(counts, error_file="error.log")
# Print a status report in exactly the format shown in the expected output.
# One line per machine with its total entries, the count for each level, and a status:
# CRITICAL — 2 or more errors
# NEEDS ATTENTION — fewer than 2 errors, but at least 1 error or warning
# OK — no errors and no warnings
# A totals line for all machines combined.
# Every line of error_file, indented by two spaces.
# The long separator lines are 40 characters (= and -).


# Hint: you can open all three output files in one with statement, and test for a level with "[ERROR]" in line.
# Grading:
# Reads both logs line by line with with and skips blank lines: 8 pts
# info.log, warning.log, error.log contain the correct lines with the machine prefix: 15 pts
# split_logs returns the correct nested counts dictionary: 7 pts
# print_report per-machine lines with correct status: 10 pts
# print_report totals line and error listing read from error_file: 7 pts
# Exact output format; clear, readable code: 3 pts

def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.
    Args:
    machines: dict mapping machine name -> log file name
    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    # open the output files for writing
    counts = {}
    pass

def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    # YOUR CODE HERE
    pass

# Test cases
with open("server_b.log", "w") as f:
    f.write("2026-10-05 09:01:12 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 09:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 09:04:10 [ERROR] Account root locked after repeated \\
failures\n")
    f.write("2026-10-05 09:15:30 [INFO] Firewall rules reloaded\n")