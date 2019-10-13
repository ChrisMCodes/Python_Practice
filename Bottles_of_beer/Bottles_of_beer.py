#Trying to create a project for each of the suggested projects from the reddit Python Projects list
#This one should be both simple and annoying. Enjoy!

def sing(bottles=99):
    for bottle in range(bottles):
        print(bottles, 'bottles of beer on the wall\n')
        print(bottles, 'bottles of beer\n')
        print('Take one down and pass it around\n')
        bottles -= 1
        print(bottles, 'bottles of beer on the wall!\n\n\n')

sing()