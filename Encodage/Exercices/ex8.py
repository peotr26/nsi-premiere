# Fonctions

def invert(binary:list, n:int)->list:
    for i in range(0, n):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0
    return binary

def addition(binary:list, n:int)->list:
    if binary[n-1] == 0:
        binary[n-1] = 1
    else:
        binary[n-1] = 0 ; ret = 1
        for i in range(n-2, -1, -1):
            if binary[i] == 0 and ret == 0:
                binary[i] = 0 ; ret = 0
            elif binary[i] == 0 and ret == 1:
                binary[i] = 1 ; ret = 0
            elif binary[i] == 1 and ret == 0:
                binary[i] = 1 ; ret = 0
            else:
                binary[i] = 0 ; ret = 1
    return binary

def addition_min(binary:list, n:int)->list:
    i = n-1
    while binary[i] == 1:
        b[i] = 0
        i -= 1
    b[i] = 1
    return binary

def complement_deux(b:list)->list:
    n = len(b)
    result = invert(b, n)
    result = addition(result, n)
    return result

# Vérification du code
 
assert complement_deux([1,1,1,1]) == [0,0,0,1]
assert complement_deux([1,1,1,0]) == [0,0,1,0]
assert complement_deux([1,1,0,1]) == [0,0,1,1]
assert complement_deux([1,0,1,1]) == [0,1,0,1]
assert complement_deux([0,1,1,1]) == [1,0,0,1]
assert complement_deux([1,1,0,0]) == [0,1,0,0]
assert complement_deux([1,0,0,1]) == [0,1,1,1]
assert complement_deux([0,0,1,1]) == [1,1,0,1]
assert complement_deux([1,0,0,0]) == [1,0,0,0]
assert complement_deux([0,0,0,1]) == [1,1,1,1]
assert complement_deux([0,0,0,0]) == [0,0,0,0]