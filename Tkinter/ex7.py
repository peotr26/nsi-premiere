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
    margin = W/10
    for i in range(0, 10):
        can.create_line(margin, margin+(36*i), W-margin, margin+(36*i), width=2 )

def vertical():
    margin = H/10
    for i in range(0, 10):
        can.create_line(margin+(36*i), margin, margin+(36*i), W-margin, width=2 )
        
def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Horizontal or vertical')

can = Canvas(win, width=W, height=H, bg=colour[1])
can.grid(rowspan=14, column=1)

but1 = Button(win, text='Horizontal', fg=colour[0], bg=colour[1], command=horizontal)
but1.grid(row=0, column=0, padx=7)

but2 = Button(win, text='Vertical', fg=colour[0], bg=colour[1], command=vertical)
but2.grid(row=1, column=0)

but3 = Button(win, text='Reset', fg=colour[0], bg=colour[1], command=reset)
but3.grid(row=3, column=0)

but4 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but4.grid(row=13, column=0)

win.mainloop()