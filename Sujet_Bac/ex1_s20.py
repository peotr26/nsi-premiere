def ajoute_dictionnaires(d1: dict, d2: dict) -> dict:
    resultat = {}
    d_cles = liste_cles(d1, d2)
    for k in d_cles:
        if k in list(d1.keys()) and k in list(d2.keys()):
            resultat[k] = d1[k]+d2[k]
        elif k in list(d1.keys()):
            resultat[k] = d1[k]
        else:
            resultat[k] = d2[k]
    return resultat


def liste_cles(d1: dict, d2: dict) -> list:
    d_cles = []
    for k in list(d1.keys()):
        d_cles.append(k)
    for k in list(d2.keys()):
        test = True
        for e in d_cles:
            if k == e:
                test is False
        if test is True:
            d_cles.append(k)
    return d_cles


d1 = {1: 5, 2: 7}
d2 = {2: 9, 3: 11}
print(ajoute_dictionnaires(d1, d2))
