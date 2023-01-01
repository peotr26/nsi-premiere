from tkinter import *
from random import randrange, randint

# Variables

W = 400
H = 400
colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
    '#003153',  # Bleu de Prusse
]
colour_target = [
    'white',
    'black',
    'blue',
    'red',
    'yellow',
]

# Fonctions

def circles():
    w = W/2 ; h = H/2
    for i in range(0, 3):
        col = colour[2] ; size = randrange(50, 376)
        can.create_oval(w-(size/2), h-(size/2), w+(size/2), h+(size/2), width=3, outline=col)

def target():
    w = W/2 ; h = H/2
    for i in range(1, 11):
        col = colour_target[int(i/2)] ; size = 350-i*35
        can.create_oval(w-(size/2), h-(size/2), w+(size/2), h+(size/2), fill=col, outline=colour[0])
        
def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Circles on target')

can = Canvas(win, width=W, height=H, bg=colour[1])
can.grid(rowspan=14, column=1)

but1 = Button(win, text='Draw a few circles', fg=colour[0], bg=colour[1], command=circles)
but1.grid(row=0, column=0, padx=7)

but2 = Button(win, text='Draw a target', fg=colour[0], bg=colour[1], command=target)
but2.grid(row=1, column=0)

but3 = Button(win, text='Reset', fg=colour[0], bg=colour[1], command=reset)
but3.grid(row=3, column=0)

but4 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but4.grid(row=13, column=0)

win.mainloop()