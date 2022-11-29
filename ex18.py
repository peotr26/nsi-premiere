def xor(x:bool,y:bool)->bool:
    result = (x and not y) or (not x and y)
    return result

print(xor(True,False))