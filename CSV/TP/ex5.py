import csv


# Fonctions
def jointure(l1: dict, l2: dict) -> dict:
    """Fonction qui joint 2 listes."""
    return {
        'Prénom': l1['Prénom'], 'Math': l1['Math'], 'Français': l1['Français'], 'Informatique': l1['Informatique'], 'Anglais': l1['Anglais'], 'Espagnol': l1['Espagnol'], 'Age': l2['Age'], 'Numéro de téléphone': l2['Numéro de téléphone']
        }


# Ouverture des 2 fichiers CSV.
f = open("table3.csv", 'r')
table3 = list(csv.DictReader(f, delimiter=","))
f.close()

f = open("table4.csv", 'r')
table4 = list(csv.DictReader(f, delimiter=","))
f.close()

# Jointure des 2 listes.
table5 = [
    jointure(l1, l2) for l1 in table3 for l2 in table4 if l1['Prénom'] == l2['Prénom']
    ]

# Écriture de la liste dans un nouveau fichier CSV.
fichier = open("table5.csv", 'w')
tableau = csv.DictWriter(fichier, [
    'Prénom', 'Math', 'Français', 'Informatique', 'Anglais', 'Espagnol', 'Age', 'Numéro de téléphone'
    ])
tableau.writeheader()
tableau.writerows(table5)
fichier.close
