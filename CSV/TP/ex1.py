import csv


# Fonctions
def moyenne(table1: list) -> dict:
    """Fonction qui créer une liste avec les moyennes de chaque matière."""
    table1 = validation(table1)
    moy = {
        'Math': 0, 'Français': 0, 'Informatique': 0, 'Anglais': 0, 'Espagnol': 0
        }
    for d in tuple(moy.keys()):
        moy[d] = moyenne_matiere(d, table1)
    return moy


def moyenne_matiere(matiere: str, table1: list) -> float:
    """Fonction qui calcule la moyenne d'une matière spécifique."""
    total = 0
    for d in table1:
        total += d[matiere]
    return total/len(table1)


def validation(table1: list) -> list:
    """Fonction qui transforme les strings en entiers."""
    for d in table1:
        d['Math'] = int(d['Math'])
        d['Français'] = int(d['Français'])
        d['Informatique'] = int(d['Informatique'])
        d['Anglais'] = int(d['Anglais'])
        d['Espagnol'] = int(d['Espagnol'])
    return table1


# Ouverture du fichier CSV.
f = open("table1.csv", 'r')
table1 = list(csv.DictReader(f, delimiter=","))
f.close()

# Vérification si la fonction fonctionne
assert moyenne(table1) == {
    'Math': 12.0, 'Français': 16.0, 'Informatique': 14.25, 'Anglais': 14.0, 'Espagnol': 12.75
    }
