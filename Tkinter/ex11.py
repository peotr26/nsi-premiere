from tkinter import *

# Variables

W = 400
H = 400

colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
]

# Fonctions

def horizontal():
    w = W/2
    can.create_line(w, 0, w, H, width=2, fill=colour[1])

def click(event):
    if event.x < W/2:
        circle('red', event.x, event.y)
    elif event.x > W/2:
        circle('blue', event.x, event.y)
    can.bind('<Button-1>', click)

def circle(colour, w, h):
    size = 40
    can.create_oval(w-size/2, h-size/2, w+size/2, h+size/2, outline=colour, fill=colour)

def reset():
    can.delete(ALL)
    horizontal()

# Widgets

win = Tk()
win.title('One line')

can = Canvas(win, width=W, height=H, bg=colour[0])
can.grid(rowspan=14, column=1)

but1 = Button(win, text='Reset', fg=colour[0], bg=colour[1], command=reset)
but1.grid(row=1, column=0)

but2 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but2.grid(row=13, column=0)

horizontal()

can.bind('<Button-1>', click)

win.mainloop()