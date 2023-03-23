def recherche_di(L, e):
    debut = 0
    fin = len(L)
    milieu = (debut+fin)//2
    pre = fin-debut
    while L[milieu] != e:
        if L[milieu] < e:
            debut = milieu
        elif L[milieu] > e:
            fin = milieu
        milieu = (debut+fin)//2
        if pre == fin-debut:
            return -1
        pre = fin-debut
    return milieu


L = [0, 2, 4, 7, 8, 13]
resultat = []
for i in range(-2, 15):
    resultat.append(recherche_di(L, i))
assert resultat == [
    -1, -1, 0, -1, 1, -1, 2, -1, -1, 3, 4, -1, -1, -1, -1, 5, -1
]
