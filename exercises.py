def power(x, n):
    """
    Calculate x raised to the power n recursively.
    Assume n is a non-negative integer.
    Example: power(2, 5) = 32
    Example: power(3, 0) = 1
    """
    # TODO: Implement this
    # Hint: x^n = x * x^(n-1)
    # Hint: What's x^0?
    
    # if n is 0 return 1
    if n == 0:
        return 1
    # if its clean return x multplied by power (x, n-1)
    return x * power(x, n - 1)

# 5 to the power of 5
n = 1
print(power(5, n))


# make a function to list all the binary strings/combonations of zeros and ones of in a desired set of character limits that would = n
def generate_binary_strings(n):
    """
    Generate all binary strings of length n.
    Example: generate_binary_strings(2) = ['00', '01', '10', '11']
    Example: generate_binary_strings(3) = ['000', '001', '010', '011', '100',
    '101', '110', '111']
    """
    # TODO: Implement this
    # Hint: For each position, you can place either '0' or '1'
    # Hint: Use a helper function that builds strings character by character
   
   # make a list to store the strings
    result = []
    
    # helper makes the binary strings recursively 
    # recursion is adding stuff retroactively to make all possible combonations
    def helper(current_string):
        # if the current string has reached the length of n when we classify it it will complete
        # n is the character limit for the binary strings
        if len(current_string) == n:
            # add the current valid string into the result list from the top
            result.append(current_string)
            return
        # if the current string has not reached the desired length add 0 and 1 to it
        helper(current_string + "0")
        helper(current_string + "1")
    # start with an empty string
    helper("")
    # display the result list
    return result
# print the generated binary strings
# ['00', '01', '10', '11'] because that is all possible zeros and ones you can add with a 2 character limit
# ['0', '1'] because that is all possible zeros and ones you can add with a 1 character limit
# ['000', '001', '010', '011', '100', '101', '110', '111'] because that is all possible zeros and ones you can add with a 3 character limit
print(generate_binary_strings(2))
print(generate_binary_strings(1))
print(generate_binary_strings(3))

 #Easy: Write recursive function to calculate sum of digits
def sum_of_digits(n):
   if n == 0:
       # if n is 0,
       return 0
   return n % 10 + sum_of_digits(n // 10)
   
#Medium: Implement recursive binary seaech
# binary search recursively add arrays to narrow the search space and look for the target element to search for
def binary_search(array,target):
     # if the array is empty or the target isn't found, return False
    if not array:
        return False
    # when looking for the target compare it with the mid most element to decide which half is to be searched
    mid = len(array) //2
    # if the target is less than the mid element, search the left half
    if array[mid] == target:
        return True
    # if the target is greater than the median element, search the right half and continue
    elif array[mid] < target:
        # the plus 1 makes sure that we dont use the mid element the side it chooses is based on colen placement partial to whatever side its closest to start with it for the left end with it for the right 
        return binary_search(array[mid+1:], target)
    # if the target is neither the same as or greater than the mid element search the left half
    else:
        return binary_search(array[:mid], target)
# looking for the target of 7 in a list of 1-5 if it it should be false
print(binary_search([1,2,3,4,67], 67))
