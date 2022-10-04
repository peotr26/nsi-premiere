from turtle import *

up()
bgcolor("lightgrey")
speed(0)

def texte():
    goto(0, 350)
    write('Un bel échiquier !')

def echiquier():
    goto(-200, -200)
    down()
    color("white")
    begin_fill()
    for i in range(0,4):
        forward(400)
        left(90)
    end_fill()
    up()
    carre()

def carre():
    color("black")
    for i in range(0, 8):
        for i in range(0,4):
            begin_fill()
            for i in range(0, 4):
                forward(400/8)
                left(90)
            end_fill()
            up()
            forward(400/4)
            down()
        up()
        left(90)
        forward(400/4)
        left(90)
        
    
echiquier()
mainloop()