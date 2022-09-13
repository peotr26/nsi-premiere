# ex 13

def un_jour_de_trop(a):
	if a%400 == 0:
		return "Vrai"
	elif a%4 == 0 and a%100 != 0:
		return "Vrai"
	else:
		return "Faux"
        
print(un_jour_de_trop(2020))