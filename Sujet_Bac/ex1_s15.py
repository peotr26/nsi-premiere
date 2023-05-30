def mini(releve: list, date: list) -> tuple:
    n = len(releve)
    tmp = releve[0]
    tmp_date = date[0]
    for i in range(1, n):
        if releve[i] < tmp:
            tmp = releve[i]
            tmp_date = date[i]
    return tmp, tmp_date


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(mini(t_moy, annees))
