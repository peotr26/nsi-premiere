from tkinter import *

# Variables

W = 400
H = 400

colour = [
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
]

colour_column = [
    '#FCB131',  # Jaune
    '#00A651',  # Vert
]

# Fonctions

def column():
    w = W/2-8 ; h = H/2-80
    for i in range(0, 10):
        can.create_rectangle(w, h+(16*i), w+16, h+(16*i)+16, fill=colour_column[i%2], outline=colour_column[i%2])
        
def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Yellow or green')

can = Canvas(win, width=W, height=H, bg=colour[1])
can.grid(rowspan=14, column=1)

but1 = Button(win, text='Draw the column', fg=colour[0], bg=colour[1], command=column)
but1.grid(row=0, column=0, padx=7)

but2 = Button(win, text='Reset', fg=colour[0], bg=colour[1], command=reset)
but2.grid(row=3, column=0)

but3 = Button(win, text='Quit', fg=colour[0], bg=colour[1], command=win.quit)
but3.grid(row=13, column=0)

win.mainloop()