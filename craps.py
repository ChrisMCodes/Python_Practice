'''
 This will be a multi-part/multi-day project I'm working on.

 Things I need this to do:
 print instructions
 set budget
 create method to increment/decrement budget according to bet
 have both 'games' (on and off) callable in a class
 '''

# random for the dice
import random
# global vars (instance variables for classes are defined in main)
play_again = "YES"



class Instructions:
     
    def opening(self):
        '''Prints the initial instructions when the game starts'''
        to_additional = "" # var to determine whether to print additional instructions
        print("This is the game of craps.")
        print("If you aren't familiar, don't worry!")
        print("We'll walk you through it.")
        print("This version is very simple.\n\n")
        print("First, we'll collect your pass line bet.")
        print("You have a budget of $100 to start. Bet carefully!\n")
        print("The pass line bet bet is the most fundamental, but also the complex bet in craps.")
        print("In the first part of the game, this bet pays on 7 or 11.")
        print("It loses on 2, 3, or 12")
        print("Any other roll moves onto the second part of the game.")
        print("This bet then pays off on the number you originally rolled (the line number).\n")
        return 0


class Bet:

    budget = 100

    def show_budget(self):
        '''Prints the current budget'''
        return "${:.2f}".format(self.budget)

    def take_bet(self):
        '''Sets new bet for user'''
        new_bet = -1
        print("How much would you like to bet?")
        try:
            while new_bet < 0:
                new_bet = float(input("$"))
                if new_bet < 0 or new_bet > self.budget:
                    print("\nSorry! I can only accept bets greater than $0 and within your budget.\n")
                    new_bet = -1
                    print("Please enter your bet: ")
        except ValueError:
            print("\nYour input was not recognized. The default value of your bet is now $1.\n")
            new_bet = 1
        # changes budget according to bet
        self.budget = self.budget - new_bet
        print("Your bet is " + str(new_bet) + " and your remaining budget is " + self.show_budget() + ".")
        print(self.show_budget())
        return new_bet







# main body of game

# instance variables
inst = Instructions()
money = Bet()


# prints opening instructions
inst.opening()

# sets opening bet
bet = money.take_bet()


# main body of game
while play_again == "YES":
