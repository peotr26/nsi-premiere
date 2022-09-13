# ex 17

from math import sqrt

def pi():
	a=1
	for i in range(2,1000):
		a=a+(1/i)**2
	print(sqrt(6*a))