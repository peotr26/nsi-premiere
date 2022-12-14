def complement_deux(b):
    n = len(b)
    result = 0
    a = 0
    for i in range(n-1, -1, -1):
        var = b.pop(i)
        if var == 1:
            result += 2**a
        a += 1
    return result

b1 = [0,1,1,1]
assert complement_deux(b1) == 7

b2 = [1,1,1,0,0,1,0]
assert complement_deux(b2) == 114