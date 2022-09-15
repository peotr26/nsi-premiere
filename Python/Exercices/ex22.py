def syra(a):
    temps_vol = 0
    alt_max = a
    nb_start = a
    temps_vol_alt = -1
    while a != 1:
        if a%2 == 0:
            a = a/2
        else:
            a = 3*a+1
        temps_vol = temps_vol + 1
        if a > alt_max:
            alt_max = a
        if a >= nb_start:
            temps_vol_alt = temps_vol_alt + 1
    print('\n Temps de vol : \n', temps_vol, '\n Altitude maximale : \n', alt_max, '\n Temps de vol en altitude : \n', temps_vol_alt )

syra(127)