from tkinter import *

# Variables

W = 400
H = 400

colour = [
    '#0081C8',  # Bleu
    '#FCB131',  # Jaune
    '#000000',  # Noir
    '#00A651',  # Vert
    '#EE334E',  # Rouge
    '#FFFFFF'   # Blanc
]

# Fonctions

def olympic():
    d = 70
    can.create_oval(85, 150, 85+d, 150+d, width=4, outline=colour[0])
    can.create_oval(125, 185, 125+d, 185+d, width=4, outline=colour[1])
    can.create_oval(165, 150, 165+d, 150+d, width=4, outline=colour[2])
    can.create_oval(205, 185, 205+d, 185+d, width=4, outline=colour[3])
    can.create_oval(245, 150, 245+d, 150+d, width=4, outline=colour[4])
        
def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Olympoic flag')

can = Canvas(win, width=W, height=H, bg=colour[5])
can.grid(rowspan=14, column=1)

but1 = Button(win, text='Draw the Olympic flag', fg=colour[2], bg=colour[5], command=olympic)
but1.grid(row=0, column=0, padx=7)

but2 = Button(win, text='Reset', fg=colour[2], bg=colour[5], command=reset)
but2.grid(row=3, column=0)

but3 = Button(win, text='Quit', fg=colour[2], bg=colour[5], command=win.quit)
but3.grid(row=13, column=0)

win.mainloop()