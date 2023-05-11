import csv

# Ouverture des 2 fichiers CSV.
f = open("table1.csv", 'r')
table1 = list(csv.DictReader(f, delimiter=","))
f.close()

f = open("table2.csv", 'r')
table2 = list(csv.DictReader(f, delimiter=","))
f.close()

# Fusion des 2 listes.
table3 = table1 + table2

# Écriture de la liste dans un nouveau fichier CSV.
fichier = open("table3.csv", 'w')
tableau = csv.DictWriter(fichier, [
    'Prénom', 'Math', 'Français', 'Informatique', 'Anglais', 'Espagnol'
    ])
tableau.writeheader()
tableau.writerows(table3)
fichier.close
