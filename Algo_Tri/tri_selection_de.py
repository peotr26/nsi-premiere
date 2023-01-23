from random import shuffle

def tri_selection(t:list)->list:
    n = len(t)
    for i in range(0, n-1):
        indice_maxi = i
        for j in range(i+1, n):
            if t[j] > t[indice_maxi]:
                indice_maxi = j
        temp = t[i]
        t[i] = t[indice_maxi]
        t[indice_maxi] = temp
    return t

t = [i for i in range(999, -1, -1)]
origin = list(t)
shuffle(t)
t = tri_selection(t)
assert t == origin
