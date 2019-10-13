#Determines whether a triangle is a Pythagorean triple, then uses turtle to draw a triangle with the same angles and proportions.
import turtle

a = int(input('Enter the length of your first side (non-hypotenuse). Please use numbers only: '))
b = int(input('Enter the length of your second side (non-hypotenuse). Please use numbers only: '))
c = int(input('Enter the length of your hypotenuse. Please use numbers only: '))


#Defines whether the user's triangle is a pythagorean triple
def is_a_pythagorean_triple(a, b, c):
    print('\n')
    if (a**2 + b**2) == c**2:
        print('Your triangle is indeed a pythagorean triple!\n')
        return True
    else:
        print('Your triangle is not a pythagorean triple.\n')
        return False


tester = is_a_pythagorean_triple(a, b, c)

if tester == True:

#Creates a turtle graphic for the triangle in question. Scales it to fit in the window if necessary.
    print('Let\'s draw your pythagorean triangle. Please note that sidelengths greater than 500 may go off screen')
    pythag = turtle.Turtle()
    pythag.pensize(4)
    pythag.color('white')
    wn = turtle.Screen()
    wn.bgcolor('yellow')

    pythag.left(180)
    pythag.forward(a)
    pythag.color('blue')
    pythag.right(90)
    pythag.forward(b)
    pythag.color('red')
    pythag.goto(0,0)


