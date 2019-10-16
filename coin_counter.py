#This program allows you to weigh your coins by type and outputs an estimate of the number of coin you have (by type), how many coin rollers you will need for them, what the value of the [type of coin] is, and what the total value of all coins comes out to
#This is a good example of why functional programming can sometimes get sticky.
#I instead used logical blocks offset by whitespace and comments so that variables were re-usable without complicating iterations



coins = ['pennies', 'nickels', 'dimes', 'quarters', 'half dollars', 'dollar coins']
total_vals = []
total_val = 0

#Iterates through coins
for coin in coins:
        
    #Nums function; determines the number of each type of coin by weight
    coin_weight = {'pennies': 2.5, 'nickels': 5, 'dimes': 2.268, 'quarters': 5.67, 'half dollars': 11.34, 'dollar coins': 8.1}    
    weight_divisor = coin_weight[coin]
    weight = float(input('Please enter the weight of {} in grams: '.format(coin)))
    num_coins = int(weight//(weight_divisor))
    print('You have approximately {} {}.'.format(num_coins, coin))
    nums = num_coins

    #Vals function; determines the value of each type of coin using the number in the nums function
    coin_values = {'pennies': 0.01, 'nickels': 0.05, 'dimes': 0.10, 'quarters': 0.25, 'half dollars': 0.50, 'dollar coins': 1}
    coin_val = round((nums * coin_values[coin]),2)
    print('The value of your {} is approximately ${}.'.format(coin, coin_val))
    vals = coin_val

    #Determines how many wrappers are needed based on the vals
    wrapper_vals = {'pennies': 0.5, 'nickels': 2, 'dimes': 5, 'quarters': 10, 'half dollars': 10, 'dollar coins': 25}
    wrappers = int(vals/wrapper_vals[coin])
    print('You are going to need approximately {} wrappers for your {}.'.format(wrappers, coin))

    #Adds val to the total_vals list
    total_vals = total_vals + [vals]

#Calculates values of all coins
for val in total_vals:
    total_val = total_val + val

#Prints the satisfying statement you were waiting for:
print('The total value of your change is ${}.'.format(total_val))

