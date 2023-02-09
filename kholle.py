
def weekend(jour):
    '''Affiche si jour est un jours de week-end'''

    jour = jour.lower()

    if jour == "samedi" or jour == "dimanche":
        print("Week-end !")
    else:
        print("Pas week-end...")


weekend("Samedi")


def lieux_trop_visiter(visites):
    '''Renvoie la liste des lieux visités plus d'une fois'''

    resultat = []

    for lieu in range(len(visites)):

        if len(visites[lieu]) > 1:
            resultat.append(lieu + 1)

    return resultat


def lieux_jamais_visiter(visites):
    '''Renvoie la liste des lieux jamais visités'''

    resultat = []

    for lieu in range(len(visites)):

        if len(visites[lieu]) == 0:
            resultat.append(lieu + 1)

    return resultat


def echangeable(visites):
    '''Renvoie True si tous les lieux ont été visités ou si le nombre de lieux
    visités plus d'une fois est supérieur au nombre de lieux non visités'''
    
    all_visited = True

    if len(lieux_jamais_visiter(visites)) > 0:
        all_visited = False

    more_toomuch_visited = True

    if len(lieux_trop_visiter(visites)) <= len(lieux_jamais_visiter(visites)):
        more_toomuch_visited = False

    if all_visited or more_toomuch_visited:
        return True
    else:
        return False


planning = [[2, 4, 7], [], [2, 3], [1], [2, 4]]

print(lieux_trop_visiter(planning))
print(lieux_jamais_visiter(planning))

is_echangeable = [[1, 2], [3, 4], [5], []]
is_not_echangeable = [[3, 4], [], []]

print(echangeable(is_echangeable))
print(echangeable(is_not_echangeable))
