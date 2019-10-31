'''
Between 1 and 1000, there is only 1 number that meets the following criteria. While it could be manually figured out with pen and paper, it would be much more efficient to write a program that would do this for you. With that being said, your goal is to find out which number meets these criteria. To find out if you have the correct number, click the link at the bottom of this main post.

    The number has two or more digits.

    The number is prime.

    The number does NOT contain a 1 or 7 in it.

    The sum of all of the digits is less than or equal to 10.

    The first two digits add up to be odd.

    The second to last digit is even.

    The last digit is equal to how many digits are in the number.
'''

#Has two or more digits, creating list of integers between 10 and 1000
nums = []
for num in range(10, 1001):
    nums.append(num)


#The number is prime
def is_prime(nums):
    primes = []
    for num in nums:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(str(num))
    return primes


#The number does not contain 1 or 7 in it
def no_one_or_seven(nums):
    new_nums = []
    for num in nums:
        if '1' not in num and '7' not in num:
            new_nums = new_nums + [num]
    return new_nums

#The sum of all of the digits is less than or equal to 10.

def less_than_11(nums):
    final_list = []
    for num in nums:
        new_list = []
        num_sum = 0
        for digit in num:
            new_list = new_list + [digit]
        for i in new_list:
            num_sum = num_sum + int(i)
        if num_sum < 11:
            final_list = final_list + [num]
    return final_list 

#The first two digits add up to be odd.
def first_two_odd(nums):
    final_list = []
    for num in nums:
        if (int(num[0]) + int(num[1])) % 2 == 1:
            final_list = final_list + [num]
    return final_list

#The second to last digit is even.
def penultimate_even(nums):
    final_list = []
    for num in nums:
        if int(num[-2]) % 2 == 0 and int(num[-2]) != 0:
            final_list = final_list + [num]
    return final_list

#The last digit is equal to how many digits are in the number.
def num_digits(nums):
    for num in nums:
        if int(num[-1]) == len(num):
            winner = 'The magic number is...' + num + '!'
            return winner

print(num_digits(penultimate_even(first_two_odd(less_than_11(no_one_or_seven(is_prime(nums))))))) #TEST