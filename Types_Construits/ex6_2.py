notes_premiere_2 = {'Emma' : ('Math', 12), 'Charles' : ('Math', 15), 'Rodolphe' : ('Math', 8), 'Berthe' : ('NSI', 7), 'Léon' : ('NSI', 11), 'Hyppolite' : ('NSI', 10)}

def notes_par_matieres(notes_premiere_2):
    n = len(notes_premiere_2)
    notes_matiere = {'Math' : [], 'NSI': []}
    for k in notes_premiere_2:
        if notes_premiere_2[k][0] == 'NSI':
            notes_matiere['NSI'].append(notes_premiere_2[k][1])
        if notes_premiere_2[k][0] == 'Math':
            notes_matiere['Math'].append(notes_premiere_2[k][1])
    return notes_matiere

print(notes_par_matieres(notes_premiere_2))
