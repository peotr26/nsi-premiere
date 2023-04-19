from random import randint


def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours+x) % 12
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n+1
    for k in cases_vues:
        assert k <= 12
    return n


print(nbre_coups())
