def pair_ou_impair(t):
    n = len(t)
    pair = []
    impair = []
    for i in range(0, n):
        a = t[i]
        if a%2 == 0:
            pair.append(a)
        else:
            impair.append(a)
    return pair, impair

print(pair_ou_impair([11, 15, 14, 6, 7, 44, 3, 5, 62, 73]))