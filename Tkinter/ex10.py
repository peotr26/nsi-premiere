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
]

checkboard_place = [
    [[0, 0, 00], [0, W/10, 00], [0, (W/10*2), 00], [0, (W/10)*3, 00], [0, (W/10)*4, 00], [0, (W/10)*5, 00], [0, (W/10)*6, 00], [0, (W/10)*7, 00], [0, (W/10)*8, 00], [0, (W/10)*9, 00]],
    [[0, 0, 10], [0, W/10, 10], [0, (W/10*2), 10], [0, (W/10)*3, 10], [0, (W/10)*4, 10], [0, (W/10)*5, 10], [0, (W/10)*6, 10], [0, (W/10)*7, 10], [0, (W/10)*8, 10], [0, (W/10)*9, 10]],
    [[0, 0, 20], [0, W/10, 20], [0, (W/10*2), 20], [0, (W/10)*3, 20], [0, (W/10)*4, 20], [0, (W/10)*5, 20], [0, (W/10)*6, 20], [0, (W/10)*7, 20], [0, (W/10)*8, 20], [0, (W/10)*9, 20]],
    [[0, 0, 30], [0, W/10, 30], [0, (W/10*2), 30], [0, (W/10)*3, 30], [0, (W/10)*4, 30], [0, (W/10)*5, 30], [0, (W/10)*6, 30], [0, (W/10)*7, 30], [0, (W/10)*8, 30], [0, (W/10)*9, 30]],
    [[0, 0, 40], [0, W/10, 40], [0, (W/10*2), 40], [0, (W/10)*3, 40], [0, (W/10)*4, 40], [0, (W/10)*5, 40], [0, (W/10)*6, 40], [0, (W/10)*7, 40], [0, (W/10)*8, 40], [0, (W/10)*9, 40]],
    [[0, 0, 50], [0, W/10, 50], [0, (W/10*2), 50], [0, (W/10)*3, 50], [0, (W/10)*4, 50], [0, (W/10)*5, 50], [0, (W/10)*6, 50], [0, (W/10)*7, 50], [0, (W/10)*8, 50], [0, (W/10)*9, 50]],
    [[0, 0, 60], [0, W/10, 60], [0, (W/10*2), 60], [0, (W/10)*3, 60], [0, (W/10)*4, 60], [0, (W/10)*5, 60], [0, (W/10)*6, 60], [0, (W/10)*7, 60], [0, (W/10)*8, 60], [0, (W/10)*9, 60]],
    [[0, 0, 70], [0, W/10, 70], [0, (W/10*2), 70], [0, (W/10)*3, 70], [0, (W/10)*4, 70], [0, (W/10)*5, 70], [0, (W/10)*6, 70], [0, (W/10)*7, 70], [0, (W/10)*8, 70], [0, (W/10)*9, 70]],
    [[0, 0, 80], [0, W/10, 80], [0, (W/10*2), 80], [0, (W/10)*3, 80], [0, (W/10)*4, 80], [0, (W/10)*5, 80], [0, (W/10)*6, 80], [0, (W/10)*7, 80], [0, (W/10)*8, 80], [0, (W/10)*9, 80]],
    [[0, 0, 90], [0, W/10, 90], [0, (W/10*2), 90], [0, (W/10)*3, 90], [0, (W/10)*4, 90], [0, (W/10)*5, 90], [0, (W/10)*6, 90], [0, (W/10)*7, 90], [0, (W/10)*8, 90], [0, (W/10)*9, 90]],
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

def choose_spot():
    while True:
        w = randrange(0, 10) ; h = randrange(0, 10)
        if checkboard_place[h[w[0]]] == 0:
            return w,h

def pawn():
    w,h = choose_spot()
    print(w) ; print(h)
    #can.create_oval(margin+(36*i), margin, margin+(36*i), W-margin, width=2 )
        
def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Checkboard')

can = Canvas(win, width=W, height=H, bg=colour[1])
can.grid(rowspan=14, column=1)

but1 = Button(win, text='Draw the checkboard', fg=colour[0], bg=colour[1], command=checkboard)
but1.grid(row=0, column=0, padx=7)

but2 = Button(win, text='Pawn', fg=colour[0], bg=colour[1], command=pawn)
but2.grid(row=1, column=0)

but3 = Button(win, text='Reset', fg=colour[0], bg=colour[1], command=reset)
but3.grid(row=3, column=0)

but4 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but4.grid(row=13, column=0)

win.mainloop()