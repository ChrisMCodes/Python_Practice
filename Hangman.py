#Hangman is now functional! No graphics yet, but I think it handles most cases. Please let me know if/when you find a bug.
#First, we'll import random so that we can choose from our word list at random
import random

#Next, we're defining our word list. This was originally going to be in a separate CSV file, but I think this works just as well:
word_list = ['abruptly', 'absurd', 'abyss', 'askew', 'avenue', 'awkward', 'axiom', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'bikini', 'blizzard', 'boggle', 'buffalo', 'buffoon', 'buzzard', 'cobweb', 'croquet', 'crypt', 'cycle', 'disavow', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'exodus', 'faking', 'fixable', 'fjord', 'flapjack', 'fluffiness', 'foxglove', 'fuchsia', 'funny', 'galaxy', 'galvanize', 'gazebo', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'larynx', 'lengths', 'lucky', 'luxury', 'matrix', 'microwave', 'mystify', 'oxygen', 'pajama', 'pixel', 'pneumonia', 'polka', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quorum', 'rhubarb', 'rhythm', 'rickshaw', 'scratch', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'subway', 'swivel', 'syndrome', 'transcript', 'transgress', 'transplant', 'twelfth', 'unknown', 'unworthy', 'unzip', 'uptown', 'voodoo', 'vortex', 'walkway', 'waltz', 'wave', 'wavy', 'wheezy', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'xylophone', 'youthful', 'yummy', 'zipper', 'zodiac', 'zombie']

#Next, we're choosing a word from the word list and calling it 'secret_word'
secret_word = random.choice(word_list)
#print('TEST: LINE 13. THE SECRET WORD IS: ', secret_word)
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
guess = ''


while guess_count > 0:
    print('You have {} guesses remaining.\n'.format(guess_count))
    #This prints out a list of the letters guessed so far after the first guess
    if len(guesses) > 0:
        print('So far you have guessed: ', guesses)
        print('The word so far is ', display_letters)
        if display_letters == secret_word:
            print('Congratulations! You have guessed the secret word!')
            break
    #Collects the user's guess
    guess = input('Please enter a letter to guess: ').lower()
    #Ensures that the guess is a single letter
    if len(guess) != 1:
        print('This is an invalid guess. Please enter only one letter and hit ENTER.')
        continue
    #Ensures that the user does not waste a guess
    if guess in guesses:
        print('You have already guessed this letter. Please choose another letter and hit ENTER.')
        continue
    #Adds the guess to the list of guesses
    guesses = guesses + [guess]
    #Here begins the magic
    if guess in secret_word:
        print('Great job! There is a {} in the secret word!'.format(guess))
        new_idx = 0 #Sets an index incrementing variable for the for loop that follows
        for letter in secret_letters:
            if letter == guess:
                #Sets compare_letters[same index as letter] to the letter
                compare_letters[new_idx] = letter
                #Converts compare_letters into a string
                display_letters = "".join(compare_letters)
                #Checks to see whether this solves the word
                if display_letters == secret_word:
                    print('You have successfully guessed the word!')
                    break
            new_idx += 1
    else:
        print('No. There is no {} in the secret word.'.format(guess))
    #Decrements the guess counter
    guess_count -= 1

if guess_count == 0:
    print('Better luck next time! The word was {}.'.format(secret_word))
