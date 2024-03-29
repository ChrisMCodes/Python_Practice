# 100 Python Challenges
# Challenges 26 - 30

# Write a function that accepts a string as an argument and modifies
# the string so as to remove all consecutive duplicate characters

def remove_duplicates(input_string):
    count = 1
    output_string = input_string[0]
    while count < len(input_string):
        if input_string[count] != input_string[count - 1]:
            output_string += input_string[count]
        count += 1
    return output_string

# Write a function that accepts a string as an argument and
# returns the words of the string in reverse order

def reverse_string(input_string):
    return " ".join(input_string.split()[::-1])


# Write a function to find the longest common prefix string between
# a given set of strings. If there is none, return an empty string


def longest_prefix(s1, s2, s3, s4):
    output_string = ""
    count = 0
    while s1[count] == s2[count] == s3[count] == s4[count]:
        output_string += s1[count]
        count += 1
    return output_string


# Given two strings s and t. String t generated by shuffling string s
# and then adding one more letter at a random position. Return the
# letter that was added to t

def new_letter(s, t):
    u = [i for i in t if i not in s]
    return u[0]


# Write a function that converts a string to a boolean value.

def string_to_bool(input_string):
    if input_string.lower() == "true":
        return True
    elif input_string.lower() == "false":
        return False
    return "Invalid input"
