# 100 Python Challenges Udemy course

# Write a function that removes white spaces from an input string

def remove_spaces(input_string):
    return input_string.replace(" ", "")


# Write a function that accepts a string with decimals and converts
# it to an integer

def str_to_int(input_string):
    with_dec = float(input_string)
    return int(with_dec)

# Return num copies of a given string

def copies_of_string(input_string, num):
    return input_string * num


# Write a function that accepts a string and calculates the number
# of upper-case letters

def count_case(sample_string):
    count = 0
    for i in sample_string:
        if i.isupper():
            count += 1
    return count


# Write a function that takes string characters as input
# and returns each character's hexadecimal value. The output
# should be in the form of a string, and should not include
# 0x at the beginning of each hexadecimal value

def convert_to_hex(input_string):
    output = ""
    count = 0
    last = len(input_string) - 1
    for i in input_string:
        output += hex(ord(i)).replace("0x", "")
        if not count == last:
            output += " "
        count += 1
    return output


