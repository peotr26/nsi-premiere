def reverse(ch):
    n = len(ch)
    reversed = ''
    for i in range(0, n):
        ri = i + 1
        reversed = ch[ri-1] + reversed
    return reversed

print(reverse('moto'))