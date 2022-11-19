def recherche(ch,ca):
    n = len(ch)
    for i in range(0,n):
        if ch[i] == ca:
            return True
    return False

print(recherche('Bonjour','a'))
print(recherche('Abracabra','a'))