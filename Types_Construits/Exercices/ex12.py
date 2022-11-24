def alternance(l1, l2):
    l3 = []
    n = len(l1)
    for i in range(0,n):
        l3.append(l1[i])
        l3.append(l2[i])
    return l3

l1 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aôut', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
l2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(alternance(l1, l2))