from random import shuffle

def tri_selection(t:list)->list:
    n = len(t)
    for i in range(0, n-1):
        indice_mini = i
        for j in range(i+1, n):
            if t[j] < t[indice_mini]:
                indice_mini = j
        temp = t[i]
        t[i] = t[indice_mini]
        t[indice_mini] = temp
    return t

t = [i for i in range(0, 1000)]
origin = t
shuffle(t)
t = tri_selection(t)
assert t == origin
