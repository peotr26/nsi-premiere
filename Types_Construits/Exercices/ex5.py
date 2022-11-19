def reverse(ch):
    n = len(ch)
    reversed = ''
    for i in range(n-1,-1,-1):
        ri = i + 1
        reversed += ch[ri-1]
    return reversed

print(reverse('moto'))