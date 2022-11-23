def cinq(t):
    n = len(t)
    inferieur = []
    superieur = []
    for i in range(0,n):
        animal = t[i]
        if len(animal) < 5:
            inferieur.append(animal)
        else:
            superieur.append(animal)
    return inferieur, superieur

t = ['chat', 'serpent', 'souris', 'chien', 'canard', 'ours']
print(cinq(t))