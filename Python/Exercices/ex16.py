# ex 16

def f(a):
	for i in range(1,4):
		if a%2 == 0:
			a = a/2+4
		if a%3 == 0:
			a = a/3+2
	return a

print(f(112))