#This is a project to help you see the future! Is this Machine Learning?

#Don't mind this. The project sees the future for real. The time import is used to build tension
import random
import time

#This function does most of the heavy lifting
def see_the_future():
    #Here's where the computer senses your commitment to your desires
    user_question = input('Ask me a question about your future and I\'ll let you know whether it will come to pass: \n')
    #Here are several responses for the program to choose from
    responses = ['It shall be so', 'It shall not be so', 'It looks likely', 'It looks unlikely', 'You are in luck', 'Your luck will run short', 'Absolutely', 'Never', 'Your wish is my command', 'Perhaps you would do better to change your wish', 'Of course!', 'Of course not!', 'It is your lucky day', 'Today isn\'t your day', 'The odds are ever in your favor', 'You are more likely to be struck by lightning', 'Perhaps', 'Perhaps not', 'If you wish', 'Are you sure you do want to ask that?', 'Your happiness is ensured', 'Don\'t bet on it']
    print('Interesting question...')
    time.sleep(2)
    print('I am thinking about your question...')
    time.sleep(2)
    print('In regards to your question', user_question, 'I have determined the following: \n')
    print(random.choice(responses)+'!\n')

#Creating a loop so that the user can play as much as s/he wants:
while True:
    see_the_future()
    play_again = input('Would you like to play again? Type yes or no: ').lower()
    if play_again == 'yes' or play_again == 'y':
        print('Excellent. I am at your service.\n\n\n')
        continue
    else:
        print('Very well. I hope you have found this experience enlightening.')
        time.sleep(2)
        print('Goodbye')
        time.sleep(5)
        break


