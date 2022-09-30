from turtle import *
from random import randrange 


def color_b(r1, r2):
    if r1 < 0 and r2 < 0:
        color('blue')
    if r1 < 0 and r2 > 0:
        color('red')
    if r1 > 0 and r2 < 0:
        color('green')
    if r1 > 0 and r2 >0:
        color('yellow')

def pantagone():
    for i in range(0,10):
        r1 = randrange(-400, 400)
        r2 = randrange(-400, 400)
        color_b(r1, r2)
        up()
        goto(r1, r2)
        down()
        for i in range(0, 6):
            forward(30)
            left(360/5)
        up()
        
pantagone()

mainloop()