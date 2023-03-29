def rendu_monnaie_centimes(s_due: int, s_versee: int) -> list:
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    a_rendre = s_versee-s_due
    rendu = []
    i = len(pieces)-1
    while a_rendre > 0:
        if pieces[i] <= a_rendre:
            rendu.append(pieces[i])
            a_rendre = a_rendre-pieces[i]
        else:
            i = i-1
    return rendu
