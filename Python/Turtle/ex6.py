from turtle import *
from random import randrange 


def color_b(x, y):
    if x%2 !=0 and y%2 != 0:
        color('blue')
    if x%2 != 0 and y%2 == 0:
        color('red')
    if x%2 == 0 and y%2 != 0:
        color('green')
    if x%2 == 0 and y%2 == 0:
        color('yellow')

def pantagone():
    for i in range(0,10):
        x = randrange(-400, 400)
        y = randrange(-400, 400)
        color_b(x, y)
        up()
        goto(x, y)
        down()
        for i in range(0, 6):
            forward(30)
            left(360/5)
        up()
        
pantagone()

mainloop()