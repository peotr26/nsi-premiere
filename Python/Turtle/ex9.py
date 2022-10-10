from turtle import *

def filled_square(c, color_b):
    down()
    color(color_b)
    begin_fill()
    for i in range(0, 4):
        forward(c*2)
        left(90)
    end_fill()
    up()
    
def bold_cross(c, b, color_b):
    color(color_b)
    width(b)
    left(90)
    forward(c)
    right(180)
    down()
    forward(c*2)
    up()
    left(90)
    forward(-c)
    left(90)
    forward(c)
    right(90)
    down()
    forward(c*2)
    up()

def quarter_circle(r):
    down()
    circle(r, 270)
    up()
    circle(r, 90)

def disk(a, b, color_b):
    down()
    color(color_b)
    begin_fill()
    circle(a, b)
    end_fill()
    up()

def bottom_sign(c):
    down()
    right(90)
    forward(c)
    up()
    forward(c/9)
    right(90)
    disk(1, 360, "black")
    
def figure1(x, y, c):
    up()
    goto(x-c, y-c)
    filled_square(c, "black")
    goto(x, y)
    bold_cross(c/1.5, c/6, "white")

def figure2(x, y, c):
    up()
    goto(x, y)
    width(3)
    quarter_circle(c)
    bottom_sign(c)
    ht()

def affichage():
    figure1(-100, 0, 50)
    color("black")
    figure2(100, 0, 40)

affichage()

mainloop()

