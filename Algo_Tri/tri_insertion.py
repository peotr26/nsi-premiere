from random import shuffle

def tri_insertion(t:list)->list:
    n = len(t)
    for i in range(1, n):
        temp = t[i]
        j = 0
        while t[j] < t[i]:
            j += 1
        for k in range(i-1, j-1, -1):
            t[k+1] = t[k]
        t[j] = temp
    return t

t = [i for i in range(0, 1000)]
origin = list(t)
shuffle(t)
t = tri_insertion(t)
assert t == origin