from turtle import *

W = window_width()
H = window_height()


bgcolor('blue')

def decouverte(coul):
    color(coul)
    up()
    goto(0, H/2)
    down()
    goto(0, - H/2)
    up()
    goto(W/2,0)
    right(90)
    down()
    goto(- W/2, 0)
    
    
    
decouverte('red')

mainloop()