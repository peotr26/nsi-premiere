from tkinter import *
from random import randint

# Variables

W = 400
H = 400

# Fonctions

def draw1():
    for i in range(0, 15):
        place_x = randint(W-397, W-23)
        place_y = randint(H-397, H-23)
        can.create_oval(place_x, place_y, place_x+20, place_y+20, width=2, outline='black')

def draw2():
    for i in range(0, 10):
        place_x = randint(W-397, W-33)
        place_y = randint(H-397, H-33)
        can.create_oval(place_x, place_y, place_x+30, place_y+30, fill='black')

def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Random circles')

can = Canvas(win, width=W, height=H, bg='white')
can.pack(side=RIGHT)

but1 = Button(win, text='Draw circle', fg='black', bg='white', command=draw1)
but1.pack(pady=8, padx=10)

but2 = Button(win, text='Draw disk', fg='black', bg='white', command=draw2)
but2.pack(pady=8)

but3 = Button(win, text='Reset', fg='black', bg='white', command=reset)
but3.pack(pady=15)

but4 = Button(win, text='Quit', fg='black', bg='white', command=win.quit)
but4.pack(pady=15)

win.mainloop()