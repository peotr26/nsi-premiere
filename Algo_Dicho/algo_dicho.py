def recherche(L: list, e: int) -> int:
    debut = 0
    fin = len(L)-1
    milieu = (debut+fin)//2
    while debut <= fin:
        milieu = (debut+fin)//2
        if L[milieu] == e:
            return milieu
        elif L[milieu] < e:
            debut = milieu+1
        else:
            fin = milieu-1
    return -1


L = [0, 2, 4, 7, 8, 13]
resultat = []
for i in range(-2, 15):
    resultat.append(recherche(L, i))
assert resultat == [
    -1, -1, 0, -1, 1, -1, 2, -1, -1, 3, 4, -1, -1, -1, -1, 5, -1
]
