from tkinter import *

# Variables

W = 400
H = 400

# Fonctions

# Widgets

win = Tk()
win.title('Random circles')

can = Canvas(win, width=W, height=H, bg='white')
can.pack(side=RIGHT)

but1

but2

but3

but4 = Button(win, text='Quit', fg='black', bg='white', command=win.quit)
but4.pack(pady=15)