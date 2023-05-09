import csv
import ex1


def critere(ligne: int, matiere: str) -> int:
    return ligne[matiere]


def trier_matiere(matiere: str, tabel1: list) -> dict:
    return sorted(table1, key=critere, reverse=True)


def valeurs(matiere: str, table1: list) -> dict:
    dictionnaire = {'meilleur_note': 0, 'moyenne': 0, 'pire_note': 0}
    liste = trier_matiere(matiere, table1)
    dictionnaire['meilleur_note'] = liste[0][matiere]
    dictionnaire['moyenne'] = ex1.moyenne_matiere(matiere, liste)
    dictionnaire['pier_note'] = liste[0][matiere]
    return dictionnaire


def resultat(tabel1: list) -> list:
    liste = list()
    for d in table1[0].keys():
        liste.append(valeurs(table1[1][d]))
    return liste


f = open("table1.csv", 'r')
table1 = list(csv.DictReader(f, delimiter=","))
f.close()
