def recherche(elt: int, tab: list) -> int:
    '''
    Fonction qui cherche la 1ere occurence d'un entier, elt, dans une liste, tab.
    '''
    n = len(tab)
    for i in range(0, n):
        if tab[i] == elt:
            return i
    return -1


assert recherche(1, [9, 3, 1]) == 2
assert recherche(9, [8, -5, 40, 26]) == -1
assert recherche(15, [-15, 26, -26, 15]) == 3
