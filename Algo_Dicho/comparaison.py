import time
import matplotlib.pyplot as plt

import algo_dicho as dicho
import algo_naif as naif

temps_dicho = []
temps_naif = []
nb_valeurs = []

for v in range(0, 100001, 1000):
    nb_valeurs.append(v)

for v in range(0, 100001, 1000):
    L = [e**2 for e in range(v)]
    start = time.time()
    dicho.recherche(L, v**2)
    end = time.time()
    elapse = end-start
    temps_dicho.append(elapse)

for v in range(0, 100001, 1000):
    L = [e**2 for e in range(v)]
    start = time.time()
    naif.recherche(L, v**2)
    end = time.time()
    elapse = end-start
    temps_naif.append(elapse)

plt.scatter(nb_valeurs, temps_dicho, s=1)
plt.scatter(nb_valeurs, temps_naif, s=1)
plt.ylabel("Temps d'exécution (en secondes)")
plt.xlabel("Nombre de valeurs dans la liste")
plt.title(
    "Temps d'exécution des fonctions recherche naïf et de recherche \n"
    "dichotomique en fonction du nombre de valeurs dans la liste"
    )
plt.show()
