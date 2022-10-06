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
    
def figure1(x, y, c):
    up()
    goto(x-c, y-c)
    filled_square(c, "black")
    goto(x, y)
    bold_cross(c/1.5, c/6, "white")
    
figure1(0, 0, 50)

mainloop()

