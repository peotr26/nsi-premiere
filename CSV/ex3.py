import csv


# Fonctions
def critere(ligne: int) -> int:
    """Fonction la clé pour trier le dictionnaire."""
    return ligne[matiere]


def trier_matiere() -> dict:
    """Fonction qui trie le dictionnaire dans l'ordre décroissant en fonction de la note en Anglais."""
    return sorted(table1, key=critere, reverse=True)


def moyenne_matiere(liste: list) -> float:
    """Fonction qui calcule la moyenne pour une matière spécifique."""
    total = 0
    for d in liste:
        total += int(d[matiere])
    return total/len(liste)


def valeurs() -> dict:
    """Fonction qui trouve la pire et meilleur note et calcule la moyenne pour une matière spécifique."""
    dictionnaire = {'matiere': matiere}
    liste = trier_matiere()
    dictionnaire['meilleur_note'] = liste[0][matiere]
    dictionnaire['moyenne'] = moyenne_matiere(liste)
    dictionnaire['pire_note'] = liste[0][matiere]
    return dictionnaire


def resultat() -> list:
    """Fonction qui créer une liste avec qui donne les différentes valeurs demandés."""
    global matiere
    liste = list()
    for i in range(1, len(table1[0])):
        matiere = list(table1[0].keys())[i]
        liste.append(valeurs())
    return liste


# Ouverture du fichier CSV.
f = open("table1.csv", 'r')
table1 = list(csv.DictReader(f, delimiter=","))
f.close()

# Vérification de la fonction resultat().
assert resultat() == [
    {'matiere': 'Math', 'meilleur_note': '8', 'moyenne': 12.0, 'pire_note': '8'},
    {'matiere': 'Français', 'meilleur_note': '19', 'moyenne': 16.0, 'pire_note': '19'},
    {'matiere': 'Informatique', 'meilleur_note': '17', 'moyenne': 14.25, 'pire_note': '17'},
    {'matiere': 'Anglais', 'meilleur_note': '7', 'moyenne': 14.0, 'pire_note': '7'},
    gh{'matiere': 'Espagnol', 'meilleur_note': '9', 'moyenne': 12.75, 'pire_note': '9'}
    ]
