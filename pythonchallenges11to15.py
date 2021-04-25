# Here are the latest problems from 100 Python Challenges

# "Write a function that accepts two arguments,"
# "year and month, and then checks if the month"
# "has Friday the 13th"

import datetime

def check_friday_13(yr, mon):
  """
  yr and mon are ints
  """
	get_day = datetime.datetime(yr, mon, 13)
	is_Fri = get_day.strftime("%A") == "Friday"
	return get_day, is_Fri


# "Given two numbers a and b, create a function"
# "that returns the next number greater than a and b"
# "and divisible by b"

def check_division(a, b):
  """
  a and b are ints
  """
    return (max(a, b) // b + 1) * b
  
  
# Write a function that chooses a random number 'n'
# from 1 to 5000 (inclusive) and then calculates
# the length of this number. Do not use the built-in
# len function to calculate the length

import random


def calculate_length():
    num = random.randint(1, 5000)
    new_num = num
    count = 0
    while new_num > 0:
        new_num = new_num // 10
        count += 1
    return num, count
  
  
# Write a function that accepts three boolean variables.
# The function should return True if at least two out
# of the three variables are true 

def booleans(x, y, z):
    """
    x, y, z are all booleans
    """
    return x, y, z, int(x + y + z) > 1 
  
  
  # Given a num, return the factorial of that num
  
  # Chris says: I'm doing this one twice.
  # First, I'll do it recursively just to practice.
  # Then, I'll do it with a loop so that I can
  # also return the original num

def factorial(num):
    """
    num is an int
    """
    total = num
    if num == 1:
        return total
    return total * factorial(num - 1)
  
# Second implementation

def factorial(num):
    """
    num is an int
    """
    total = num
    end_num = num 
    while num > 1:
        num -= 1
        total *= num
    return end_num, total
