# Continuing on my 100 Python Challenges Udemy course...
# Here are the next questions

# Write a function that randomly chooses any number from 5 to 10 (inclusive)
# and then generates a Fibonacci sequence up to that number.
# The sequence should be returned as a list


def Fibonacci():
    import random
    n = random.randint(5, 10)
    a, b = 0, 1
    count = 0
    fib = list()
    while count < n:
        fib.append(a)
        a, b = b, a + b
        count += 1
    return n, fib



# Write a function that accepts two strings (first_name, last_name)
# The function should concatenate these two strings by inserting a space
# between the strings and then reverse the resulting string.

def string_reverse(first_name, last_name):
    """
    first_name is a string
    last_name is a string
    """
    full_name = first_name + " " + last_name
    return full_name[::-1]


# Write a function that swaps two strings without using a third variable

# ...does the creator of this challenge know that Python can do this pretty straightforwardly?

def swap_strings(s1, s2):
    """
    s1 is a string
    s2 is a string
    """
    s1, s2 = s2, s1
    return s1, s2


# Write a function to count the number of vowels in a given string

def count_vowels(input_string):
    """
    input_string is a string
    """
    vowels = [a, e, i, o, u]
    num_vowels = 0
    for letter in input_string:
        if letter in vowels:
            num_vowels += 1
    return num_vowels

# Write a function to remove duplicate elements from a Python string
def remove_duplicates(input_string):
    """
    input_string is a string
    """
    in_string = list()
    new_string = str()
    for letter in input_string:
        if letter not in in_string:
            in_string.append(letter)
            new_string += letter
    return new_string
    
