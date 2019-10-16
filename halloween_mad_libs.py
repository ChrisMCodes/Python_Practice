animal = input('Type of animal: ').upper()
name = input('Name for a boy: ').upper()
activity = input('After-school activity: ').upper()
weather = input('Word to describe the weather: ').upper()
monster = input('Type of monster: ').upper()
motion = input('Action word for a type of movement: ').upper()
decoration = input('Halloween decoration: ').upper()
last_name = input('Last name: ').upper()

print('\n')

print('Once upon a time, there was a young {} who lived with his parents.'.format(animal))

print('One day, when the {}, whose name was {}, was walking home from {}, the weather suddenly changed!'.format(animal, name, activity))

print('The sky turned dark.')

print("'Where did this {} weather come from?'  wondered {}.".format(weather, name))

print('As he approached his house, it started to seem farther and farther away. The sidewalk felt like it was pulling him back to school!')

print('He turned around to see what was happening, and he saw a {} trying to catch up with him.'.format(monster))

print('He began to {}, but no matter how much he did, he could feel the {} getting closer!'.format(motion, monster))

print("The {} at the house he was passing suddenly stood up and pushed him into the {}'s arms.".format(decoration, monster))

print('He yelled and cried. This was no {}! It was much, much worse! It was Mrs. {}, his teacher, who had come to tell him that his homework was late!'.format(monster, last_name))

print('{} wished he had never left {}...'.format(name, activity))
