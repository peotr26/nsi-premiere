from tkinter import *

# Variables

W = 400
H = 400
colour = [
    '#e0ac69',  # Couleur de la peau
    '#000000',  # Noir
    '#FFFFFF',  # Blanc
    '#03308a',  # Bleu pour le drapeau yougoslave
    '#d81612'   # Rouge pour le drapeau yougoslave
]

# Fonctions

def face():
    can.create_oval(50, 25, 350, 375, fill=colour[0], outline=colour[0])
    for i in range(0, 2):
        can.create_oval(100+(i*150), 100, 150+(i*150), 150, fill=colour[2], outline=colour[2])
        can.create_oval(120+(i*150), 120, 130+(i*150), 130, fill=colour[1], outline=colour[1])
    can.create_oval(180, 100, 220, 220, width=2, fill=colour[0])
    can.create_rectangle(140, 260, 260, 300, fill=colour[1])

def flag():
    can.create_rectangle(50, 233, 350, 300, outline=colour[4], fill=colour[4])
    can.create_rectangle(50, 100, 350, 166, outline=colour[3], fill=colour[3])
    can.create_rectangle(50, 100, 350, 300, outline=colour[1])
        
def reset():
    can.delete(ALL)

# Widgets

win = Tk()
win.title('Random')

can = Canvas(win, width=W, height=H, bg=colour[2])
can.pack(side=RIGHT)

but1 = Button(win, text='Draw a face', fg=colour[1], bg=colour[2], command=face)
but1.pack(pady=8, padx=10)

but2 = Button(win, text='Draw a flag', fg=colour[1], bg=colour[2], command=flag)
but2.pack(pady=8)

but3 = Button(win, text='Reset', fg=colour[1], bg=colour[2], command=reset)
but3.pack(pady=15)

but4 = Button(win, text='Quit', fg=colour[1], bg=colour[2], command=win.quit)
but4.pack(pady=15)

win.mainloop()