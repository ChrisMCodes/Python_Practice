# Another from the Google IT Automation challenges

# Just a bit of fun here


def pig_latin(text):
  say = []
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    pl_word = word[1:] + word[0] + "ay"
    # Turn the list back into a phrase
    say.append(pl_word)
    pl_say = " ".join(say)
  return pl_say
		
'''
# test cases
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
'''
