def mystere(n):
    k = 2
    while k%n == 0:
        k = k+1
    if k == n:
        reponse = True
    else:
        reponse = False
    return reponse

c = mystere(6)
print(c)