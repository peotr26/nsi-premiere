from tkinter import *
from random import randrange

# Variables

W = 400
H = 400

assert H/W == 1

colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
    '#FF0000',  # Rouge
    '#0000FF',  # Bleu
]

checkboard_place = [
    [[0, W/10*0, H/10*0], [0, W/10*1, W/10*0], [0, (W/10*2), W/10*0], [0, (W/10)*3, W/10*0], [0, (W/10)*4, W/10*0], [0, (W/10)*5, W/10*0], [0, (W/10)*6, W/10*0], [0, (W/10)*7, W/10*0], [0, (W/10)*8, W/10*0], [0, (W/10)*9, W/10*0]],
    [[0, W/10*0, H/10*1], [0, W/10*1, W/10*1], [0, (W/10*2), W/10*1], [0, (W/10)*3, W/10*1], [0, (W/10)*4, W/10*1], [0, (W/10)*5, W/10*1], [0, (W/10)*6, W/10*1], [0, (W/10)*7, W/10*1], [0, (W/10)*8, W/10*1], [0, (W/10)*9, W/10*1]],
    [[0, W/10*0, H/10*2], [0, W/10*1, W/10*2], [0, (W/10*2), W/10*2], [0, (W/10)*3, W/10*2], [0, (W/10)*4, W/10*2], [0, (W/10)*5, W/10*2], [0, (W/10)*6, W/10*2], [0, (W/10)*7, W/10*2], [0, (W/10)*8, W/10*2], [0, (W/10)*9, W/10*2]],
    [[0, W/10*0, H/10*3], [0, W/10*1, W/10*3], [0, (W/10*2), W/10*3], [0, (W/10)*3, W/10*3], [0, (W/10)*4, W/10*3], [0, (W/10)*5, W/10*3], [0, (W/10)*6, W/10*3], [0, (W/10)*7, W/10*3], [0, (W/10)*8, W/10*3], [0, (W/10)*9, W/10*3]],
    [[0, W/10*0, H/10*4], [0, W/10*1, W/10*4], [0, (W/10*2), W/10*4], [0, (W/10)*3, W/10*4], [0, (W/10)*4, W/10*4], [0, (W/10)*5, W/10*4], [0, (W/10)*6, W/10*4], [0, (W/10)*7, W/10*4], [0, (W/10)*8, W/10*4], [0, (W/10)*9, W/10*4]],
    [[0, W/10*0, H/10*5], [0, W/10*1, W/10*5], [0, (W/10*2), W/10*5], [0, (W/10)*3, W/10*5], [0, (W/10)*4, W/10*5], [0, (W/10)*5, W/10*5], [0, (W/10)*6, W/10*5], [0, (W/10)*7, W/10*5], [0, (W/10)*8, W/10*5], [0, (W/10)*9, W/10*5]],
    [[0, W/10*0, H/10*6], [0, W/10*1, W/10*6], [0, (W/10*2), W/10*6], [0, (W/10)*3, W/10*6], [0, (W/10)*4, W/10*6], [0, (W/10)*5, W/10*6], [0, (W/10)*6, W/10*6], [0, (W/10)*7, W/10*6], [0, (W/10)*8, W/10*6], [0, (W/10)*9, W/10*6]],
    [[0, W/10*0, H/10*7], [0, W/10*1, W/10*7], [0, (W/10*2), W/10*7], [0, (W/10)*3, W/10*7], [0, (W/10)*4, W/10*7], [0, (W/10)*5, W/10*7], [0, (W/10)*6, W/10*7], [0, (W/10)*7, W/10*7], [0, (W/10)*8, W/10*7], [0, (W/10)*9, W/10*7]],
    [[0, W/10*0, H/10*8], [0, W/10*1, W/10*8], [0, (W/10*2), W/10*8], [0, (W/10)*3, W/10*8], [0, (W/10)*4, W/10*8], [0, (W/10)*5, W/10*8], [0, (W/10)*6, W/10*8], [0, (W/10)*7, W/10*8], [0, (W/10)*8, W/10*8], [0, (W/10)*9, W/10*8]],
    [[0, W/10*0, H/10*9], [0, W/10*1, W/10*9], [0, (W/10*2), W/10*9], [0, (W/10)*3, W/10*9], [0, (W/10)*4, W/10*9], [0, (W/10)*5, W/10*9], [0, (W/10)*6, W/10*9], [0, (W/10)*7, W/10*9], [0, (W/10)*8, W/10*9], [0, (W/10)*9, W/10*9]],
]

# Fonctions

def choose_colour(i:int, k:int)->str:
    if k%2 == 0:
        if i%2 == 0:
            result = colour[0]
        else:
            result = colour[1]
    else:
        if i%2 == 0:
            result = colour[1]
        else:
            result = colour[0]
    return result

def checkboard():
    for k in range(0, 10):
        w = 0 ; h = (H/10)*k ; size = W/10
        for i in range(0, 10):
            can.create_rectangle(w+(size*i), h, w+(size*i)+size, h+size, fill=choose_colour(i, k), outline=choose_colour(i, k))

def choose_spot()->tuple:
    for i in range(0, 100):
        w = randrange(0, 10) ; h = randrange(0, 10)
        if checkboard_place[h][w][0] == 0:
            checkboard_place[h][w][0] = 1
            return checkboard_place[h][w][1], checkboard_place[h][w][2]

def pawn(colour_pawn:str):
    w,h = choose_spot() ; size = W/10 ; margin = W/100
    can.create_oval(w+margin, h+margin, w+size-margin, h+size-margin, fill=colour_pawn, outline=colour_pawn)

def pawn_red():
    pawn(colour[2])

def pawn_blue():
    pawn(colour[3])

def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Checkboard')

can = Canvas(win, width=W, height=H, bg=colour[1])
can.grid(rowspan=14, column=1)

but1 = Button(win, text='Draw the checkboard', fg=colour[0], bg=colour[1], command=checkboard)
but1.grid(row=0, column=0, padx=7)

but2 = Button(win, text='Red pawn', fg=colour[0], bg=colour[1], command=pawn_red)
but2.grid(row=1, column=0)

but3 = Button(win, text='Blue pawn', fg=colour[0], bg=colour[1], command=pawn_blue)
but3.grid(row=2, column=0)

but4 = Button(win, text='Reset', fg=colour[0], bg=colour[1], command=reset)
but4.grid(row=4, column=0)

but5 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but5.grid(row=13, column=0)

win.mainloop()