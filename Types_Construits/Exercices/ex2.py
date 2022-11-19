def recherche_indice_1(ch,c):
    n = len(ch)
    place_c = -1
    for i in range(0,n):
        place_c += 1
        if ch[i] == c:
            return place_c
    return -1

print(recherche_indice_1("Bonjour",'a'))