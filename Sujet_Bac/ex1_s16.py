def recherche_indices_classement(elt: int, tab: list) -> tuple:
    inferieur = []
    egale = []
    superieur = []
    for i in range(0, len(tab)):
        if tab[i] == elt:
            egale.append(i)
        elif tab[i] < elt:
            inferieur.append(i)
        else:
            superieur.append(i)
    return inferieur, egale, superieur

