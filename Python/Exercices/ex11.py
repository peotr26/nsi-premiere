#ex 11

def imc(a,b):
	if a/b**2 < 18.5 :
		print("Manger plus")
	elif a/b**2 > 25 :
		print("Manger moins")
	else :
		 print("Continuer comme ça")