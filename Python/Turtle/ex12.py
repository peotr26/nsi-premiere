from turtle import *

# Note : n and m to not be creating any problem have been mdofified into n_n and n_m.

speed(0)

def line(s, colour):
    '''
    Function that will draw the line.
    '''
    down()
    color(colour)           # Apply the choosen colour.
    left(90)
    forward(s)              # Draw the line.
    up()
    right(180)
    forward(s)              # Go back to the starting point.
    left(90)

def n_side(n_n, n_m, sb):
    '''
    Function that will draw the lines vertically.
    '''
    for i in range(0, n_n):
        line(25*n_m, 'black')
        forward(sb)
    line(25*n_m, 'black')   # Draw the last line to make it cleaner.

def m_side(n_n, n_m, sb):
    '''
    Function that will draw the lines horizontally.
    '''
    for i in range(0, n_m):
        line(25*n_n, 'black')   
        forward(sb)
    line(25*n_n, 'black')   # Draw the last line to make it cleaner.

def display(n_n, n_m, sb):
    '''
    Function that will display the final result depending on n_n and n_m.
    '''
    n_side(n_n, n_m, sb)
    left(90)
    m_side(n_n, n_m, sb)
    
display(10, 10, 25)
mainloop()