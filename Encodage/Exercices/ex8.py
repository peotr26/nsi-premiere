def invert(binary:list)->list:
    n = len(binary)
    for i in range(0, n):
        temp = binary[i]
        if temp == 0:
            binary[i] = 1
        else:
            binary[i] = 0
    return binary

assert invert([1,0,0,0]) == [0,1,1,1]

def add1(binary:list, n:int, ret:int)->list:
    for i in range(0, n-1):
        if binary[i] == 0 and ret == 0:
            binary[i] = 0
            ret = 0
        elif binary[i] == 0 and ret == 1:
            binary[i] = 1
            ret = 0
        elif binary[i] == 1 and ret == 0:
            binary[i] = 1
            ret = 0
        else:
            binary[i] = 1
            ret = 1
    return binary

def addition(binary:list)->list:
    n = len(binary)
    ret = 0
    if binary[n-1] == 0:
        binary[n-1] = 1
    else:
        binary[n-1] = 0
        ret = 1
        add1(binary, n, ret)
    return binary

assert addition([0,1,1,1]) == [1,1,1,0]

def complement_deux(b):
    result = invert(b)
    result = addition(result)
    return result

print(complement_deux([1,1,1,0]))