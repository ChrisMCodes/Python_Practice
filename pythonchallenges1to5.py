#!/usr/bin/var python

# Just some fun Python exercises
# From the Udemy course "100 Python Challenges"

# Function for challenge #1
# "Write a function that accepts three variables a, b, and c, and returns the sum of these variables"
# "If the values are equal, then return two times their sum"

def sum_num(a, b, c):
    """
    a, b, c are all integers or floats
    """
    return 6 * a if a == b == c else (a + b + c)
    
# Function for challenge #2
# "Write a function that accepts a number and returns its square root, rounded to three decimal places"

def sqrt(num):
    """
    num is integer or float
    """
    return round(num ** 0.5, 3)
    
# Function for challenge #3
# "Write a function that accepts two integers, num 1 and num2."
# "The function should divide num1 by num2 and return the quotient and remainder."
# "The output should be rounded to two decimal places."

def quot_rem(num1, num2):
    """
    num1, num2 are integers or floats
    """
    return round(num1 / num2, 2), round(num1 % num2, 2) 

# Function for challenge #4
# "Write a function to check whether a number is even or odd"

def even_odd(num):
    """
    num should be an integer
    """
    return "Even" if num % 2 == 0 else "Odd"
    
# Function for challenge #5
# "Write a function to determine the factors of a number as a list."

def factors(num):
    """
    num should be an integer
    """
    facs = list()
    for i in range(1, num + 1):
        if num % i == 0:
            facs.append(i)
    return facs
