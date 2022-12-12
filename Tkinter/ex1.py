from tkinter import *

# Variables

W = 600
H = 600

# Fonctions

def draw():
    can.create_oval(100, 100, 500, 500, fill='black')
    can.create_line(150, 150, 450, 450, width=20, fill='white')
    can.create_oval(350, 200, 400, 250, fill='white')
    can.create_oval(200, 350, 250, 400, fill='white')

def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Drawing')

can = Canvas(win, width = W, height = H, bg = 'white')
can.pack(side = RIGHT)

but1 = Button(win, text='Reset', fg='black', bg='white', command=reset)
but1.pack(padx=10, pady=5)

but2 = Button(win, text='Quit', fg='black', bg='white', command=win.quit)
but2.pack(pady=10)

draw()

win.mainloop()