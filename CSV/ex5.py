import csv


def jointure(t1: list, t2: list) -> list:
    table = []
    for i in range(len(t1)):
        table.append({
            'Pays': t1[i]['Pays'],
            'Capitale': t1[i]['Capitale'],
            'Superficie en km2': t2[i]['Superficie en km2'],
            'Monnaie': t2[i]['Monnaie']
            })
    return table


def validation(table: list) -> list:
    for e in table:
        e['Superficie en km2'] = float(e['Superficie en km2'])
    return table


fichier = open("liste_pays_capitale.csv", "r")
tablePaysCap = list(csv.DictReader(fichier, delimiter=","))
fichier.close()

fichier = open("liste_pays_superficie_monnaie.csv", "r")
tablePaysSupMon = list(csv.DictReader(fichier, delimiter=","))
fichier.close()

tablePaysSupMon = validation(tablePaysSupMon)

tablePaysComplete = jointure(tablePaysCap, tablePaysSupMon)

fichier = open("liste_pays_complete.csv", 'w')
tableau = csv.DictWriter(fichier, [
    'Pays', 'Capitale', 'Superficie en km2', 'Monnaie'
    ])
tableau.writeheader()
tableau.writerows(tablePaysComplete)
fichier.close
