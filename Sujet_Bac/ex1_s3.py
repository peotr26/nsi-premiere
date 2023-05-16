def moyenne(table: list) -> float:
    dividande = 0
    diviseur = 0
    for e in table:
        dividande += e[0] * e[1]
        diviseur += e[1]
    if diviseur > 0:
        return dividande/diviseur
    else:
        return None


print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))
