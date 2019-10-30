read_story = open('Green_Eggs.txt', 'r')
write_story = open('And_Ham.txt', 'w')

story = read_story.readlines()

for line in story:
    line = line.split()
    idx = 0
    for word in line:
        if word == 'i':
            line[idx] = 'I'
        elif word == 'Sam-i-am!':
            line[idx] = 'Sam-I-Am!'
        elif word == 'Sam-i-am.':
            line[idx] = 'Sam-I-am.'
        idx += 1
    line = " ".join(line)
    line = line + '\n'
    write_story.write(line)


read_story.close()
write_story.close()
