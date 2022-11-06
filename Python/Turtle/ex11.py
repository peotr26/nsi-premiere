from turtle import *

def coloured_circle(r, dg, b, colour):
    '''
    Function that will draw a circle depending on the radius, degree, boldness and colour.
    '''
    down()
    width(b)            # Choose the width of the line.
    color(colour)       # Apply the colour choosen.
    circle(r, dg)       # Draw the circle.
    up()

def draw(r, dg, b, colour):
    '''
    Function that will draw and move to the right place to create the rainbow.
    '''
    coloured_circle(r, dg, b, colour)
    up()
    left(90)
    forward(r*2-b)      # Move to the right possition to do the next line.
    left(90)
    down()

def display(s):
    '''
    Function that will draw the whole rainbow.
    '''
    b = s/10
    up()
    forward(s)          # Move to the right place to start the drawing.
    left(90)
    draw(s, 180, b, 'red')
    draw(s-b, 180, b, 'orange')
    draw(s-b*2, 180, b, 'yellow')
    draw(s-b*3, 180, b, 'green')
    draw(s-b*4, 180, b, 'blue')
    draw(s-b*5, 180, b, 'indigo')
    draw(s-b*6, 180, b, 'purple')

display(300)
mainloop()

# End note : this program will be way better if I could make use of list function.