import random

cont = 'Y'
num_sides = int(input('How many sides would you like your die to have? '))
vals = {}

while cont == 'Y' or cont == 'YES':    
    d1 = random.randrange(1, num_sides+1)
    print('Your roll was: ', d1)
    if d1 in vals:
        vals[d1] += 1
    else:
        vals[d1] = 1
    if vals[d1] == 1:
        print('You have rolled {} {} time.\n'.format(d1, vals[d1]))
    else:
        print('You have rolled {} {} times.\n'.format(d1, vals[d1]))
    cont = input('Would you like to play again? Y/N ').upper()
    print(cont)
    if cont == 'Y' or cont == 'YES':
        print('Ok, starting again!\n')
        continue
    else:
        print('Here is what you rolled:')
        for val in vals:
            if vals[val] == 1:
                print('You rolled {} {} time'.format(val, vals[val]))
            else:
                print('You rolled {} {} times.'.format(val, vals[val]))
        print('Thanks for playing! Goodbye!')
        exit()


        


