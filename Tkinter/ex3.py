from tkinter import *
from random import randint, randrange

# Variables

W = 400
H = 400

# Fonctions

def face():
    can.create_oval(50, 25, 350, 375, fill='#e0ac69', outline='#e0ac69')
    for i in range(0, 2):
        can.create_oval(100+(i*150), 100, 150+(i*150), 150, fill='black')
    can.create_oval(180, 225, 220, 150, fill='black')
        
def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Random')

can = Canvas(win, width=W, height=H, bg='white')
can.pack(side=RIGHT)

but1 = Button(win, text='Draw circle', fg='black', bg='white', command=face)
but1.pack(pady=8, padx=10)

but2 = Button(win, text='Reset', fg='black', bg='white', command=reset)
but2.pack(pady=15)

but3 = Button(win, text='Quit', fg='black', bg='white', command=win.quit)
but3.pack(pady=15)

win.mainloop()