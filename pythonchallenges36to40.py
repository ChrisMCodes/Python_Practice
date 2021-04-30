# More Python challenges from the Udemy course
# 100 Python Challenges.
#
# 36 - 40
@author ChrisMCodes

# Write a function to separate the digits
# of an integer. Return the digits in the
# form of a list.

def separate_digits(num):
    return [int(n) for n in str(num)]

# Given a string, determine whether it is
# a pangram in the English alphabet.

# Chris notes: I'm assuming spaces but
# no punctuation. We could certainly
# exclude punctuation with regex
# if that was in the prompt.

def pangram(sample_string):
    letters = set(i.lower() for i in sample_string.replace(" ", ""))
    return len(letters) == 26

# Write a function that accepts a string
# and a character. The function should
# remove all occurrences of the given
# character from the input string and
# return the string.

def remove_char(input_string, char):
    return input_string.replace(char, "")

# Write a function that tests if a string
# is a valid pin or not. For our purposes,
# a valid pin has 5 characters, all numeric,
# and no whitespace.

def valid_pin(input_string):
    all_numeric = True
    for i in input_string:
        if not i.isnumeric():
            return False
    return len(input_string) == 5

# Write a function that finds the number of times
# a substring occurs in a given string and also
# the position at which the sub-string is found

# Chris says: definitely simplifying this one with
# regex. 

def find_substring(main_string, sub_string):
    import re
    indices = [m.start() for m in re.finditer(sub_string, main_string)]
    return len(indices), indices
