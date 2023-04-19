def insere(a, tab):
    l = list(tab)
    l.append(a)
    i = len(tab)-1
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i-1
    return l
