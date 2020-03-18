'''
These are the solutions to the Module 4 coding exercises from the Google IT Automation course on Coursera.
'''


'''
 The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
 '''
 def format_address(address_string):
  # Declare variables
  house = ""
  street = ""
  # Separate the address string into parts
  address = address_string.split()
  # Traverse through the address parts
  house = str(address[0])
  street = " ".join(address[1:])

  
  # Return the formatted string  
  return "house number {} on street named {}".format(house, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"





'''
The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line? 
'''

def highlight_word(sentence, word):
  word_index = sentence.index(word)
  new_word = word.upper()
  new_sentence = sentence[0:word_index] + new_word + sentence[word_index + len(word):]
  return new_sentence


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))



'''
A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
'''

def combine_lists(list1, list2):
  combined_list = list2
  
  # Reversing list1
  i = -1
  for item in list1:
    combined_list.append(list1[i])
    i = i - 1
  
  return combined_list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))




'''
Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].
'''

def squares(start, end):
	return [ n*n for n in range(start, end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]





'''
Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one. 
'''

def car_listing(car_prices):
  result = ""
  for car in car_prices:
    price = car_prices[car]
    result += "{} costs {} dollars".format(car, price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))






'''
Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.
'''

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  combined_guests = guests1

  for guest in guests2:
    if guest not in combined_guests:
      combined_guests[guest] = guests2[guest]
  return combined_guests

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))




'''
Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. 
'''

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.lower() in result and letter.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
      result[letter.lower()] += 1
    # Add or increment the value in the dictionary
    elif letter.lower() not in result and letter.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
      result[letter.lower()] = 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}





