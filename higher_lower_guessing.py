import random

print('In this game, the computer will pick a number between 1 and 100.')
print('You will also pick a number.')
print('If the computer\'s number is lower than yours, this program will tell you so.')
print('Likewise if the computer\'s number is lower than yours.')
print('Are you ready to play? Good luck!')


def higher_lower(play_num, comp_num):
    highest = 100
    lowest = 1
    while play_num != comp_num:
        if play_num > comp_num:
            print('The computer\'s secret number is lower than yours.')
            highest = play_num
            play_num = play_num = int(input('Please enter a number between {} and {}: '.format(lowest, highest)))
        elif play_num < comp_num:
            print('The computer\'s secret number is higher than yours.')
            lowest = play_num
            play_num = play_num = int(input('Please enter a number between {} and {}: '.format(lowest, highest)))
    if play_num == comp_num:
        print('Congratulations! The computer\'s number was {}.'.format(comp_num))

while True:    
    comp_num = random.randrange(1, 100)
    play_num = int(input('Please enter a number between 1 and 100: '))

    higher_lower(play_num, comp_num)

    again = input('Would you like to play again? Type YES or NO: ').upper()
    if again == 'YES' or again == 'Y':
        print('Good luck!')
        continue
    else:
        print('Thanks for playing!')
        break
