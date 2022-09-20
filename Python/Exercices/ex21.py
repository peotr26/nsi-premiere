def mystere(n):
    k = 2
    while n%k != 0:
        k = k+1
    if k == n:
        reponse = True
    else:
        reponse = False
    return reponse, k

c = mystere(8)
print(c)

def mystere_ame(n):
    if n ==2: return True