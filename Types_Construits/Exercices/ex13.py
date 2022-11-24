def cinq(t):
    n = len(t)
    inferieur = []; superieur = []
    for i in range(0,n):
        if len(t[i]) < 5:
            inferieur.append(t[i])
        else:
            superieur.append(t[i])
    return inferieur, superieur

t = ['chat', 'serpent', 'souris', 'chien', 'canard', 'ours']
print(cinq(t))