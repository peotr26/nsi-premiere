def recherche(tab: list, n: int) -> int:
    for i in range(len(tab)-1, -1, -1):
        if tab[i] == n:
            return i
    return n


print(recherche([2, 3, 5, 2, 4], 2))
