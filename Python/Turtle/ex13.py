from turtle import *
from math import pi

speed(0)

def display(factor):
    '''
    Function that will draw the Fibonnaci spiral. Factor define the scale of the spiral.
    '''
    a = 0
    b = 1
    for i in range(20):
        forward_b = pi*b*factor/2   # Calcuating the number of pixels to go forward at each 
        forward_b /= 90             # Dividing the number of pixels to go forward by 90.
        for i in range(90):
            forward(forward_b)
            left(1)
        temp = a                    # Continuing the Fibonnaci suite.
        a = b
        b = temp + b

display(0.1)
mainloop()