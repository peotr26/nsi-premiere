from turtle import *
from math import sqrt

speed(0)

def triangle(c):
    down()
    begin_fill()
    for i in range(0, 3):
        forward(c)
        left(360/3)
    end_fill()
    up()

def pythagore1(c):
    b = sqrt(c**2-(c/2)**2)
    return b

def nuclear(w, h, c):
    up()
    goto(w, h)
    triangle(c)
    goto(w-c/2, h-pythagore1(c))
    triangle(c)
    goto(w -c, h)
    triangle(c)

def pyramide(w, h, c):
    up()
    goto(w-c, h-pythagore1(c))
    triangle(c*2)
    forward(c)
    left(360/6)
    color("white")
    triangle(c)
    right(360/6)

def initiate():
    down()
    begin_fill()

def terminate():
    end_fill()
    up()

def move(s):
    left(90)
    forward(s)
    right(90)
    
def disk(a, b, color_b):
    down()
    color(color_b)
    begin_fill()
    circle(a, b)
    end_fill()
    up()

def symbol(w, h, c):
    goto(w, h+c*2)
    left(180)
    disk(c*2, 180, "black")
    disk(c, 360, 'white')
    color("black")
    move(c/2)
    disk(c/3, 360, "black")
    move(c+c/2)
    disk(c, 360, "black")
    move(c/2)
    disk(c/3, 360, "white")
    color("black")
    goto(w, h-c*2)
    down()
    circle(c*2)

def screen():
    nuclear(-200, 0, 50)
    up()
    pyramide(0, 0, 50)
    up()
    symbol(200, 0, 25)

screen()
mainloop()
