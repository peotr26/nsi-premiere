def max_dico(dico: dict) -> tuple:
    keys = list(dico.keys())
    values = list(dico.values())
    maxi = 0
    for i in range(1, len(dico)):
        if values[i] > values[maxi]:
            maxi = i
    return keys[maxi], values[maxi]


dico = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
print(max_dico(dico))

dico = {'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}
print(max_dico(dico))
