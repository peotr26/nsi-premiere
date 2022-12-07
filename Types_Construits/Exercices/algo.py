# Soit t1 et t2 deux listes contenant uniquement des entiers:
t1 = [15, 0, 8, 9, 25]
t2 = [15, 5, 89, 45, 17, 3]

# Algorithme pour vérifier l'occurence d'un entier dans une liste.
def recherche_occ(t:list, a:int)->bool:
    '''Fonction qui renvoie le booléen True si l'entier a se trouve dans la liste t.
    Sinon elle renvoie le booléen False.
    '''
    n = len(t)
    for i in range(0, n):
        if t[i] == a:
            return True
    return False

assert recherche_occ(t1, 17) == False
assert recherche_occ(t2, 17) == True

# Algorithme pour calculer la moyenne d'une liste:
def moyenne(t:list)->float:
    '''Fonction qui renvoie la moyenne des éléments de la liste t.
    '''
    n = len(t)
    moy = 0
    for i in range(0, n):
        moy += t[i]
    # moy est égale à la somme des entiers de la liste t.
    moy = moy/n
    return moy

assert moyenne(t1) == 11.4
assert moyenne(t2) == 29.0

# Algorythmes pour trouver un extremum d'une liste:
def recherche_max(t:list)->int:
    '''Fonction qui renvoie le plus grand entier de la liste t.
    '''
    n = len(t)
    maxi = t[0]
    for i in range(1, n):
        if t[i] > maxi:
            maxi = t[i]
    return maxi

assert recherche_max(t1) == 25
assert recherche_max(t2) == 89

def recherche_min(t:list)->int:
    '''Fonction qui renvoie le plus petit entier de la liste t.
    '''
    n = len(t)
    mini = t[0]
    for i in range(1, n):
        if t[i] < mini:
            mini = t[i]
    return mini

assert recherche_min(t1) == 0
assert recherche_min(t2) == 3