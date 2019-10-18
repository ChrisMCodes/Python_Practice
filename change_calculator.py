#This program tells you the most efficient way to return change

change = float(input('Input the change amount and press ENTER: $'))


quarters = int(change/0.25)
rem_change = change - quarters*0.25

dimes = int(rem_change/0.10)
rem_change = rem_change - dimes*0.1

nickels = int(rem_change/0.05)
rem_change = rem_change - nickels*0.05

pennies = round(rem_change/0.01)



print('For {}, you will need {} quarters, {} dimes, {} nickels, and {} pennies.'.format(change, quarters, dimes, nickels, pennies))
