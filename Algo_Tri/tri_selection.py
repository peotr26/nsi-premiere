from random import shuffle
from time import sleep

def tri_selection(t:list)->list:
    n = len(t)
    for i in range(0, n-1):
        indice_mini = i
        for j in range(i+1, n):
            if t[j] < t[indice_mini]:
                indice_mini = j
        temp = t[i]
        t[i] = t[indice_mini]
        t[i] = temp
        print(t)
        sleep(2)
    return t

t = [i for i in range(0, 10)]
print(t)
shuffle(t)
print(t)
t = tri_selection(t)
print(t)