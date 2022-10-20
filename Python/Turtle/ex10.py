from turtle import *

def filled_rectangle(x, y, color_b):
	down()
	color(color_b)
	begin_fill()
	for i in range(0,2):
		forward(x)
		left(90)
		forward(y)
		left(90)
	end_fill()
	up()

def drapeau_francais(x, y):
	up()
	goto(x-150, y-75)
	filled_rectangle(2*50, 3*50, '#0000ff')
	forward(2*50)
	filled_rectangle(2*50, 3*50, '#FFFFFF')
	forward(2*50)
	filled_rectangle(2*50, 3*50, '#FF0000')

def drapeau_danois(x, y):
	up()
	goto(x-150, y-75)
	filled_rectangle(6*37, 6*28, '#E31836')
	forward((6*37)/3)
	filled_rectangle(30, 6*28, "white")
	forward(-((6*37)/3))
	left(90)
	forward(23*3)
	right(90)
	filled_rectangle(6*37, 30, "white")

drapeau_francais(-200, 0)
drapeau_danois(200, 0)

mainloop()