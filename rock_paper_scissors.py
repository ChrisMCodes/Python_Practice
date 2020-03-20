# A simple, functional rock, paper, scissors text-based game

import random
        
        

def num_to_word(hand):
    """Converts numeric data into rock/paper/scissors as a string"""
    if hand == 1:
        return "rock"
    elif hand == 2:
        return "paper"
    else:
        return "scissors"

def get_hand():
    """gets user's hand"""
    user_num = -1
    while user_num < 1:
        try:
            user_num = int(input("Please enter 1 to choose rock, 2 to choose paper, or 3 to choose scissors: "))
            user_num = int(user_num) # controls for accidental spaces
            if user_num not in [1, 2, 3]:
                print("Hmmm, I didn't quite get that. Let's try again.")
                user_num = -1
        except ValueError:
            print("Whoops! Did you enter 1, 2, or 3? Let's try again!")
            user_num = -1
    return user_num



# Global vars, including loop, incrementing/tracker vars
win, lose, tie = 0, 0, 0
# a new variable called this_round will be used to call rps() after definition
play_again = True

# Vars for user and computer hand
computer_num = random.randint(1, 4)
user_num = -1
# Once converted to a string become
computer_hand = ""
user_hand = ""

# Main body of program
while play_again == True:

    # Input validation to ask user to choose hand from 1: rock, 2: paper, 3: scissors
    user_num = get_hand()

    # Sets computer_hand and user_hand into word values so that they can be printed more clearly
    computer_hand = num_to_word(computer_num)
    user_hand = num_to_word(user_num)

    # Displays both hands:
    print("You chose {} and the computer chose {}.".format(user_hand, computer_hand))

        # Determines whether the user wins, loses, or ties
    if user_num == computer_num:
        print("It's a tie.")
        this_round = "tie"
    elif (user_num == 1 and computer_num == 2) or (user_num == 2 and computer_num == 3) or (user_num == 3 and computer_num == 1):
        print("The computer won this time.")
        this_round = "lose"
    else:
        print("You won!")
        this_round = "win"
    

    # tracks values
    if this_round == 'win':
        win += 1
    elif this_round == 'tie':
        tie += 1
    else:
        lose += 1

    print("So far, you have won {} times, lost {} times, and tied {} times.\n".format(win, lose, tie))


    # resets play_again
    again = ""
    possible_answers = ['yes', 'y', 'no', 'n']
    while again.lower() not in ['yes', 'y', 'no', 'n']:
        try:
            again = input("Would you like to play again [yes/no]?  ")
            if again not in possible_answers:
                print("Whoops! I didn't get that. Let's try again.")
        except Exception:
            print("Whoops! I didn't get that. Let's try again.")
    if again.lower() == 'yes' or again.lower() == 'y':
        play_again = True
    else:
        play_again = False 
    
    
