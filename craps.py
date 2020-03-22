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
        print("You have a budget of $100 to start. Bet carefully!")
        print("If you need more information about the pass line bet, type [y]es. Otherwise, type [n]o.")
        to_additonal = input("")
        while to_additional.lower() not in ["y","yes", "n", "no"]:
            print("Sorry! I didn't get that. Did you want additional instructions? Please type yes or no.")
            to_additonal = input("")

     def additional_instructions(self):
        print("This bet is the most fundamental, but also the complex bet in craps.")
        print("In the first part of the game, this bet pays on 7 or 11.")
        print("It loses on 2, 3, or 12")
        print("Any other roll moves onto the second part of the game.")
        print("This bet then pays off on the number you originally rolled (the line number).")





# main body of game
while play_again == "YES":
