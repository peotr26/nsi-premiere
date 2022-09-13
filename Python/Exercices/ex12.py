#ex 12

def bac(a):
	if a >= 16 :
		return("Mention très bien")
	elif a >= 14:
		return("Mention bien")
	elif a >= 12:
		return("Mention assez bien")
	else:
		return("Faux")

print(bac(15))