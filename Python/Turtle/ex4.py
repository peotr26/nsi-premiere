from turtle import *

w = - window_width()
h = 0

def triangle(c,w,h):
    up()
    goto(w, h)
    right(360/3)
    down()
    for i in range(0, 3):
        forward(c)
        left(360/3)
    up()

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