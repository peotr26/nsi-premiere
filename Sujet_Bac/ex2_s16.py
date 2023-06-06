def moyenne(nom: str, dico_result: dict) -> float:
    if nom in list(dico_result.keys()):
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points/total_coefficients, 1)
    else:
        return -1


resultats = {'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'DS3': [14, 4]
    },

    'Durand': {
        'DS1': [6, 4],
        'DM1': [14.5, 1],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [8, 4],
        'DS4': [15, 4]
    }
}

assert moyenne('Dupont', resultats) == 12.0
assert moyenne('Durand', resultats) == 9.2
