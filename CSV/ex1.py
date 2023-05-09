import csv


def moyenne(table1: list) -> dict:
    table1 = validation(table1)
    moy = {'Math': 0, 'Français': 0, 'Informatique': 0, 'Anglais': 0, 'Espagnol': 0}
    for d in tuple(moy.keys()):
        moy[d] = moyenne_matiere(d, table1)
    return moy


def moyenne_matiere(matiere: str, table1: list) -> float:
    total = 0
    for d in table1:
        total += d[matiere]
    return total/len(table1)


def validation(table1: list) -> list:
    for d in table1:
        d['Math'] = int(d['Math'])
        d['Français'] = int(d['Français'])
        d['Informatique'] = int(d['Informatique'])
        d['Anglais'] = int(d['Anglais'])
        d['Espagnol'] = int(d['Espagnol'])
    return table1


f = open("table1.csv", 'r')
table1 = list(csv.DictReader(f, delimiter=","))
f.close()
