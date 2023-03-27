def recherche(L: list, e: int) -> int:
    n = len(L)
    for i in range(n):
        if e == L[i]:
            return i
    return -1


L = [0, 2, 4, 7, 8, 13]
resultat = []
for i in range(-2, 15):
    resultat.append(recherche(L, i))
assert resultat == [
    -1, -1, 0, -1, 1, -1, 2, -1, -1, 3, 4, -1, -1, -1, -1, 5, -1
]
