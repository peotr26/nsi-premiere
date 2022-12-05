def f(x:bool, y:bool)->int:
    result = not((x and not y) or (not x and y))
    return int(result)

assert f(True, True) == 1
print(f(True, True))