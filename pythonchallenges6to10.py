# Questions 6 - 10 from the Udemy Course "100 Python Challenges"


# "Write a function to find any number x ^ y"

def power(x, y):
    return x ** y


# "Write a function that returns the decimal part of a number to two decimal places"
def decimal_part(num):
    return "INTEGER" if num % 1 == 0 else round(num % 1, 2)
    

# This is a classic FizzBuzz
def fizzbuzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num
    
    
# "Return the number of numerical digits in a string"
    
def count_num_digits(input_string):
    nums = [c for c in input_string if c.isnumeric()]
    return len(nums)
        

# "Write a function that checks if a number is equal to the sum"
# "of its positive divisors, except itself"

def sum_pos_divisor(num):
    total = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            total += i 
        if total > num:
            return False
    if total == num:
        return True
    return False
