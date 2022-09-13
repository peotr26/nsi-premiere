def est_en_cours(heure):
	lycee_est_ouvert = False
	if 8 <= heure < 17.5:
		lycee_est_ouvert = True
	return lycee_est_ouvert

reponse = est_en_cours(6)

print(reponse)