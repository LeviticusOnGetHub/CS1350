### Exercise 2.2 (Beginner): Same Result, Comprehension Style

# List of numbers to square
numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))
print(squares)        # [1, 4, 9, 16]

# TODO: Build the same list with a list comprehension (no map, no lambda).
# we make x multiplied by every iteration of itself in the list 1 times 1 2 times 2 etc.
squares_comp = [x * x for x in numbers]
print(squares_comp)   # [1, 4, 9, 16]

### Exercise 2.3 (Intermediate): Filter and Sort


words = ["kiwi", "fig", "banana", "plum", "apple"]

# TODO 1: Use filter and a lambda to keep the words with more than 4 letters.
# lambda word for filtering words with more than 4 letters
# it returns True if the length of the word is greater than 4
long_words = list(filter(lambda lam_word: len(lam_word) > 4, words))
print(long_words)   # ['banana', 'apple']

# TODO 2: Use sorted() with key=lambda ... to order the words by length.
# sort to order words lambda to get their length in ascending order
by_length = sorted(words, key=lambda lam_word: len(lam_word))
print(by_length)    # ['fig', 'kiwi', 'plum', 'apple', 'banana']

### Exercise 3.1 (Beginner): Add the Missing Line


def count_up_to(n):
    """Yield 1, 2, 3, ... up to n."""
    i = 1
    while i <= n:
        # TODO: Hand back i with yield (one line).
        # yield i makes i possible to be returned one at a time
        yield i
        i += 1

print(list(count_up_to(3)))   # [1, 2, 3]

gen = count_up_to(2)
print(next(gen))              # 1
print(next(gen))              # 2

### Exercise 3.2 (Beginner): From List to Generator

# TODO: Change this list comprehension into a generator expression.
#       (You only need to change two characters.)
# they were initially a list comprehension, now changed to a generator expression with () instead of []
squares = (x * x for x in range(5))

print(next(squares))   # 0
print(next(squares))   # 1
print(list(squares))   # [4, 9, 16]  - only what is left

### Exercise 4.1 (Beginner): Any Number of Arguments


def total(*numbers):
    """Return the sum of all the arguments."""
    # TODO 1: Replace with your code (one line). Remember: numbers is a tuple.
    return sum(numbers)

print(total(1, 2, 3))   # 6
print(total())          # 0

prices = [5, 10, 15]
# TODO 2: Call total with the three prices by unpacking the list with *.
# the * unwraps the list into separate individual arguments
result = total(*prices)
print(result)           # 30


### Exercise 4.2 (Beginner): Unpack a Dictionary into a Call


def describe(name, age):
    return f"{name} is {age}"

person = {"name": "Ada", "age": 36}

# TODO: Call describe using the dictionary and the ** operator.
#       Do not type "Ada" or 36 yourself.
# the ** unwraps the dictionary into keyword arguments for the function call
result = describe(**person)
print(result)   # Ada is 36
