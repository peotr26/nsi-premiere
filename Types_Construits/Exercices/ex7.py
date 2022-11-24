def separation(ch):
    n = len(ch)
    final = ''
    for i in range(0, n-1):
        final += ch[i] + '*'
    final += ch[n-1]
    return final

print(separation('hello'))
