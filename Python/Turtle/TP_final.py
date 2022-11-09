from turtle import *
from random import randrange

bgcolor('white')
speed(0)

def goto_am(x,y):
    up()
    goto(x,y)
    down()

def move(s,o):
    up()
    setheading(o)
    forward(s)
    down()

def go_back(s,o):
    up()
    move(s,o+180)
    move(s/20,o+90)
    down()
    
def line(s,o,colour):
    down()
    color(colour)
    setheading(o)
    forward(s)    

def main_structure(x,y,s):
    goto_am(x, y)
    color('black')
    for i in range(0,4):
        forward(s)
        left(90)

def opening(x,y,s,o):
    goto_am(x,y)
    line(s/20,o,'white')
    
def choose_colour():
    if randrange(0,4) == 0:
        return 'white'
    else:
        return 'black'
    
def serie_line(s,o):
    for i in range(0,int(s/20)):
        line(20, o, choose_colour())
        
def draw_series(s):
    a = 19
    while a != 0:
        serie_line(s,0)
        go_back(s,0)
        a -= 1
    move(s/20,0)
    for i in range(1,20):
        serie_line(s,180+90)
        go_back(s,180+90)

def display():
    up()
    goto(-200,-180)
    draw_series(400)
    main_structure(-200,-200,400)
    opening(-200,-200,400,0)
    opening(200,200,400,180)
   
display()
mainloop()