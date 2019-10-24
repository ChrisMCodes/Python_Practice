#More to do with this tomorrow :-) This is just a start and won't do anything functionally interesting yet.

#Hangman! This is just a first attempt at making this program work

#First, we'll import random so that we can choose from our word list at random
import random

#Next, we're defining our word list. This was originally going to be in a separate CSV file, but I think this works just as well:
word_list = ['abruptly', 'absurd', 'abyss', 'askew', 'avenue', 'awkward', 'axiom', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'bikini', 'blizzard', 'boggle', 'buffalo', 'buffoon', 'buzzard', 'cobweb', 'croquet', 'crypt', 'cycle', 'disavow', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'exodus', 'faking', 'fixable', 'fjord', 'flapjack', 'fluffiness', 'foxglove', 'fuchsia', 'funny', 'galaxy', 'galvanize', 'gazebo', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'larynx', 'lengths', 'lucky', 'luxury', 'matrix', 'microwave', 'mystify', 'oxygen', 'pajama', 'pixel', 'pneumonia', 'polka', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quorum', 'rhubarb', 'rhythm', 'rickshaw', 'scratch', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'subway', 'swivel', 'syndrome', 'transcript', 'transgress', 'transplant', 'twelfth', 'unknown', 'unworthy', 'unzip', 'uptown', 'voodoo', 'vortex', 'walkway', 'waltz', 'wave', 'wavy', 'wheezy', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'xylophone', 'youthful', 'yummy', 'zipper', 'zodiac', 'zombie']

#Next, we're choosing a word from the word list and calling it 'secret_word'
secret_word = random.choice(word_list)

#Here's a list containing all the letters in secret_word
secret_letters = [letter for letter in secret_word]

#And here's a list that mimicks secret_letters, except with the letters replaced by underscores
compare_letters = []
for letter in secret_letters:
    compare_letters = compare_letters + ['_']

#Here's the display version of this that we'll see when we actually make a guess:
display_letters = "".join(compare_letters)
len_letters = str(len(display_letters)) + ' letters in this word.'
display = display_letters + len_letters


#Guess parameters
guess_count = 10 #Limits the total number of guesses the player can make
guesses = [] #Keeps track of what the user has already guessed

while guess_count > 0:
    print('You have {} guesses remaining.\n'.format(guess_count))
    #This prints out a list of the user's guesses so far after the first guess
    if len(guesses) > 0:
        print('So far you have guessed: ', guesses)
    #Collects the user's guess
    guess = input('Please enter a letter to guess: ').lower()
    #Ensures that the guess is a single letter
    if len(guess) != 1:
        print('This is an invalid guess. Please enter only one letter and hit ENTER.')
        continue
    #Adds the guess to the list of guesses
    guesses = guesses + [guess]
    #Here begins the magic
    if guess in secret_word:
        print('Great job! There is a {} in the secret word!'.format(guess))
        '''This is where the magic will happen'''
    else:
        print('No. There is no {} in the secret word.'.format(guess))
    #Decrements the guess counter
    guess_count -= 1