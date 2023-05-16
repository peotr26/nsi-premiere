def verifie(table: list) -> bool:
    n = len(table)
    for i in range(1, n):
        if table[i-1] >= table[i]:
            return False
    return True


assert verifie([1, 2, 3, 4]) == True
assert verifie([1, 5, 4, 6]) == False
