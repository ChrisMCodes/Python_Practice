#This is a draft I made while sick
#Upon reaching the end, I realized it was about as inefficient as could be
#I am going to refactor when I am feeling better and have a little more clarity of thought.

#This program allows you to weigh your coins by type and outputs an estimate of the number of coin you have (by type), how many coin rollers you will need for them, what the value of the [type of coin] is, and what the total value of all coins comes out to
#First a function that looks at the type and weight of each coin and returns the number of coins of each type

def nums():
    coin_weight = {'pennies': 2.5, 'nickels': 5, 'dimes': 2.268, 'quarters': 5.67, 'half dollars': 11.34, 'dollar coins': 8.1}
    coin_nums = {}
    for coin in coin_weight:
        weight = 1500 #REMOVE THIS TEST CASE
        #weight = float(input('Please enter the weight of {} in grams: '.format(coin)))
        coin_nums[coin] = int(round(weight//(coin_weight[coin]), 0))
        print('You have approximately {} {}.'.format(coin_nums[coin], coin))
    return coin_nums #Returns the number of each type of coin


#A function that tells you the value of each of the coins

def vals(nums):
    coin_values = {'pennies': 0.01, 'nickels': 0.05, 'dimes': 0.10, 'quarters': 0.25, 'half dollars': 0.50, 'dollar coins': 1}
    coin_vals = {}
    for coin in nums:
        coin_vals[coin] = round((nums[coin] * coin_values[coin]), 2)
        print('Your {} are worth approximately ${}.'.format(coin, coin_vals[coin]))
    return coin_vals



#Defining the number of wrappers needed

def wrappers_needed(vals):
    wrapper_vals = {'pennies': 0.5, 'nickels': 2, 'dimes': 5, 'quarters': 10, 'half dollars': 10, 'dollar coins': 25}
    wrappers = {}
    for val in vals:
        value_by_coin = vals[val]
        value_by_wrapper = wrapper_vals[val]
        num_wrappers_needed = value_by_coin/value_by_wrapper
        wrappers[val] = int(num_wrappers_needed)
        print('You are going to need {} wrappers for your {}'.format(wrappers[val], val))
    return wrappers


#Next, a function that determines the total value of all the coins:

def total_vals(vals):
    totals = [vals[val] for val in vals]
    total = 0
    for tot in totals:
        total = total + tot
    print('The total value of all of your coins is ${}.'.format(total))
    return total

def whole_program(total_vals):
    print(wrappers_needed(vals(nums())))


#TO DO: Change dependencies on vals. It will be less accurate but it will fit better into the nesting.

whole_program()


