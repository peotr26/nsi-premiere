def syra(a):
    temps_vol = 0
    alt_max = a
    nb_start = a
    temps_vol_alt = -1
    while a != 1 and a >= nb_start:
        if a%2 == 0:
            a = a/2
        else:
            a = 3*a+1
        temps_vol = temps_vol + 1
        if a > alt_max:
            alt_max = a
        temps_vol_alt = temps_vol_alt + 1
    while a != 1:
        if a%2 == 0:
            a = a/2
        else:
            a = 3*a+1
        temps_vol = temps_vol + 1
        if a > alt_max:
            alt_max = a
    return a, temps_vol, alt_max, temps_vol_alt

print(syra(127))

