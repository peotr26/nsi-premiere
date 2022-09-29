from turtle import *

w = - window_width()
h = 0
color('orange')

def triangle(c,w,h):
    up()
    goto(w+50, h)
    right(360/3*2)
    down()
    for i in range(0, 3):
        forward(c)
        left(360/3)
    up()
    right(360/3)
    

def affichage():
    w = 0 - 500
    h = 0
    c = 20
    for i in range(1,8):
        c = c + 10
        w = w + c + 30
        triangle(c,w,h)

affichage()

mainloop()