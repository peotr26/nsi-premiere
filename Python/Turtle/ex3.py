from turtle import *

W = window_width()
H = window_height()


bgcolor('white')

def pair_ou_pas(n):
    if n%2 == 0:
        cible1('red')
    else:
        cible2('green')

def cible1(coul1):
    color(coul1)
    up()
    goto(0, H/2)
    down()
    goto(0, - H/2)
    up()
    goto(W/2,0)
    right(90)
    down()
    goto(- W/2, 0)

def cible2(coul2):
    color(coul2)
    up()
    goto(W,H)
    down()
    goto(-W,-H)
    up()
    goto(-W,H)
    down()
    goto(W,-H)  
    
pair_ou_pas(33)

mainloop()