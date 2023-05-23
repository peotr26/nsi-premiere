mendeleiev = [
    ['H', '.', '.', '.', '.', '.', '.', 'He'],
    ['Li', 'Be', 'B', 'C', 'O', 'Fl', 'Ne']
    ]

gaz_rares = []

for ligne in mendeleiev:
    gaz_rares.append(ligne[len(ligne)-1])

print(gaz_rares)
