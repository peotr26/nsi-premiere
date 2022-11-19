def recherche_indice_2(ch,c):
    n = len(ch)
    place_c = n
    for i in range(n-1,0,-1):
        place_c -= 1
        if ch[i] == c:
            return place_c
    return -1

print(recherche_indice_2("Bonjour",'o'))