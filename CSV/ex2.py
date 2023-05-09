import csv

table7Pays = [
    {"Pays": "Albanie", "Capitale": "Tirana", "Superficie(en km2)": 28748, "Monnaie": "Lek"},
    {"Pays": "Allemagne", "Capitale": "Berlin", "Superficie(en km2)": 357121, "Monnaie": "Euro"},
    {"Pays": "Andorre", "Capitale": "Andorre-La-Vieille", "Superficie(en km2)": 468, "Monnaie": "Euro"},
    {"Pays": "Arménie", "Capitale": "Erevan", "Superficie(en km2)": 29743, "Monnaie": "Dram"},
    {"Pays": "Autriche", "Capitale": "Vienne", "Superficie(en km2)": 83879, "Monnaie": "Euro"},
    {"Pays": "Azerbaïdjan", "Capitale": "Bakou", "Superficie(en km2)": 86600, "Monnaie": "Manat"},
    {"Pays": "Belgique", "Capitale": "Bruxelles", "Superficie(en km2)": 30528, "Monnaie": "Euro"}
    ]

fichier = open("table_7Pays.csv", 'w')
tableau = csv.DictWriter(fichier, ['Pays', 'Capitale', 'Superficie(en km2)', 'Monnaie'])
tableau.writeheader()
tableau.writerows(table7Pays)
fichier.close
