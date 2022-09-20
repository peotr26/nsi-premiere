def mutliplication(a,b):
    """
    This function will multiply a with b.

    Args:
        a : Multiplicator
        b : Multiplicator

    Returns:
        answer: The result of the multiplication.
    """
    answer=0
    for i in range(0,b):
        answer = answer + a
    return answer

c = mutliplication(7,11)
print(c)