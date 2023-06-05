def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
        result = caractere + result
    return result


def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine


def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)


assert inverse_chaine('bac') == 'cab'
assert est_palindrome('NSI') is False
assert est_palindrome('ISN-NSI') is True
assert est_nbre_palindrome(214312) is False
assert est_nbre_palindrome(213312) is True
