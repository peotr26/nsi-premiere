def double_voyelle(ch):
    voyelles = ['a','e','u','o','i','y']
    n = len(ch)
    final = ''
    for i in range(0,n):
        final += ch[i]
        if any(voyelle in ch[i] for voyelle in voyelles):   # Vérifie si le charactère correspond à un charactère dans la liste voyelles.
            final += ch[i]
    return final

print(double_voyelle('hello'))