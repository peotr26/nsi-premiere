from turtle import *

w = - window_width()
h = 0
color('orange')
speed()

def polynome(c,n,w,h):
    up()
    goto(w+25, h)
    down()
    for i in range(0, n):
        forward(c)
        left(360/n)
    up()
    
def affichage():
    w = 0 - 550
    h = 0
    c = 40
    n=2
    for i in range(1,7):
        w = w + c + 100
        n=n+1
        polynome(c, n, w, h)
        
affichage()

mainloop()