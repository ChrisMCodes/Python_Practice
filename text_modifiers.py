# Just for fun, a program that allows you to modify text

run_again = True

while run_again == True:
    # global vars will come up at end to check whether to restart program
    ans = ""
    answers = ['YES', 'Y', 'NO', 'N']

    # ctrl and choice variables for exception handling
    ctrl = -1
    choice = -1


    # prints list_options and indexes
    def list_options(case_functions):
        list_of_options = enumerate(case_functions)

        #Displays options cleanly
        for num, option in list_of_options:
            print(str(num+1) + "   |   " + option)

        
        return ''

    # Introduces program
    print("This program helps you morph and format your text.\n")

    # Accepts user input
    print("Please choose the number corresponding to how you would like to modify your text: ")

    # Calls list_options to list possible functions
    print(list_options(["Reverse your phrase", "Strip your phrase of punctuation and spaces", "Strip your phrase of punctuation only (preserves spaces)", "Convert your phrase into aNnOyInG cAsE"]))


    # Input validation
    while ctrl < 0:
        try:
            choice = int(input())
            if choice in range(1, 5):
                print(' ')
                ctrl = 1
            else:
                print("I don't recognize that choice. Let's try again.\n")
                ctrl = -1
        except ValueError:
            print("I didn't recognize your input. Please input 1, 2, 3, or 4")
            ctrl = -1


    class PhraseOps:
        # self.phrase definition and initialization
        phrase = input("Type in your phrase here: ")
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alpha_space = alphabet + [" "]

        # reverses the phrase
        def turn_around(self):
            back_phrase = ""
            for letter in self.phrase:
                back_phrase = letter + back_phrase
            return back_phrase

        # strips phrase of all punctuation and spaces (good for palindromes)
        def stripped(self):
            stripped_phrase = ""
            for letter in self.phrase:
                if letter.lower() in self.alphabet:
                    stripped_phrase += letter
            return stripped_phrase
        
        # strips punctuation but not spaces (good for literally nothing)
        def stripped_with_spaces(self):
            space_phrase = ""
            for letter in self.phrase:
                if letter.lower() in self.alpha_space:
                    space_phrase += letter
            return space_phrase

        # converts phrase to aNnOyInG cAsE
        def annoying_case(self):
            annoying_phrase = ""
            i = 0
            while i < len(self.phrase):
                letter = self.phrase[i]
                for letter in self.phrase:
                    if i % 2 == 0:
                        annoying_phrase += letter.lower()
                    else:
                        annoying_phrase += letter.upper()
                    i += 1
            return annoying_phrase


    # defines new phrase object
    new = PhraseOps()

    # sets correct method:
    if choice == 1:
        print(new.turn_around())
    elif choice == 2:
        print(new.stripped())
    elif choice == 3:
        print(new.stripped_with_spaces())
    else:
        print(new.annoying_case())


    # validates answer to restart program
    while ans.upper() not in answers:
        print("\nWould you like to modify more text?")
        ans = input()
        if ans.upper() not in answers:
            print("Sorry, I didn't get that. Please type only yes or no")

    if ans.upper() == "YES" or ans.upper() == "Y":
        run_again == True
        print()
    else:
        run_again == False
        break
    
