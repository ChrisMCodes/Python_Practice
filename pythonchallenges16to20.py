# Here is the continuation of the Udemy course 100 Coding Challenges
# Questions 16 - 20

# Write a Python function that takes a division equation and checks
# if it returns a whole number without decimals after dividing

def check_division(num):
    """
    num is a division expression
    """
    return num % 1 == 0 
	

# Write a function that accepts an integer and returns True
# if the number is prime, else False.

def prime_number(num):
    """
    num is a non-negative integer
    """
    divisors = [n for n in range(1, (num//2) + 1) if num / n == 0]
    return True if len(divisors) == 1 else False

# Write a function that randomly chooses any number from 100 to 300 (inclusive)
# and then calculates the sum of the digits in the number
import random

def sum_digits():
    n = random.randint(100, 300)
    total = (n // 100) + ((n % 100) // 10) + ((n % 100) % 10)
    return n, total
    

# Write a function that generates a list, i, containing
# 10 random numbers from 0 - 100, and then returns
# a new list of numbers of all the values of i that
# are divisible by 15
import random
    
def divide_by_15():
    input_list = list()
    for i in range(11):
        input_list.append(random.randint(0, 100))
    output_list = [num for num in input_list if num % 15 == 0]
    return input_list, output_list
    
# Write a function that accepts an integer,
# converts the integer to its binary form,
# swaps the third and seventh bit,
# and returns the decimal form of the new
# binary number 

def swap_bits(num):
    """
    num is a positive int
    """
    bin_num = dec_to_bin(num)
    # swap variables
    a = bin_num[0:2]
    b = bin_num[2]
    c = bin_num[6]
    a += (c + bin_num[3:6])
    a += (b + bin_num[7:])
    return bin_to_dec(a)
    
def dec_to_bin(num):
    """
    num is a positive int
    """
    bin_string =bin(num).replace("0b", "")
    # I like binary numbers to be 8 bits
    while len(bin_string) < 8:
        bin_string = "0" + bin_string
    return bin_string
    
def bin_to_dec(num):
    """
    num is a binary number *as a string*
    """
    return int(num, 2)
