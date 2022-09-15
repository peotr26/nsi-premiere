# ex 17

from math import sqrt

def pi(n):
	a=1
	for i in range(2,n):
		a=a+(1/i)**2
	return sqrt(6*a)
 
print(pi(1000))