#ex 12

def nul_ou_pas(a):
    if a >= 16 :
        return("Mention très bien")
    elif a >= 14:
        return("Mention bien")
    elif a >= 12:
        return("Mention assez bien")
    else:
        return("Faux")

print(nul_ou_pas(15))