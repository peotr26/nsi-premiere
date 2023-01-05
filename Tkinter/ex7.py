from tkinter import *
from random import randrange, randint

# Variables

W = 400
H = 400
colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
]

# Fonctions

def horizontal():
    for i in range(0, 10):

def vertical():
    
        
def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('3 or 5')

can = Canvas(win, width=W, height=H, bg=colour[1])
can.grid(rowspan=14, column=1)

but1 = Button(win, text='Draw 3', fg=colour[0], bg=colour[1], command=three)
but1.grid(row=0, column=0, padx=7)

but2 = Button(win, text='Draw 5', fg=colour[0], bg=colour[1], command=five)
but2.grid(row=1, column=0)

but3 = Button(win, text='Reset', fg=colour[0], bg=colour[1], command=reset)
but3.grid(row=3, column=0)

but4 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but4.grid(row=13, column=0)

win.mainloop()