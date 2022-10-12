carre_mag = [[4, 14, 15, 1],
             [9, 7, 6, 12],
             [5, 11, 10, 8],
             [16, 2, 3, 13]]

carre_pas_mag = [carre_mag[k].copy() for k in range(len(carre_mag))]
carre_pas_mag[3][2] = 7


def afficheCarre(carre):
    '''Affiche la liste à deux dimensions carre comme un carré'''

    for line in carre:
        for element in line:
            print(element, end=" ")
        print()


def testLignesEgales(carre):
    '''Renvoie la somme des éléments d'une ligne si toutes les lignes ont \
        une somme égale'''

    to_return = 0
    for line in carre:
        if sum(line) == sum(carre[0]):
            to_return = sum(line)
        else:
            to_return = -1
            break

    return to_return


def testColonnesEgales(carre):
    '''Revoie la somme des colonnes'''

    to_return = 0
    somme_de_verif = 0

    for x in range(len(carre[0])):

        somme = 0

        for y in range(len(carre)):
            if x == 0:
                somme_de_verif += carre[y][x]
            else:
                somme += carre[y][x]
        if x == 0:
            to_return = somme_de_verif
            continue

        if somme != somme_de_verif:
            to_return = -1
            break

    return to_return


def testDiagonalesEgales(carre):

    diag1 = 0
    diag2 = 0

    for i in range(len(carre)):
        diag1 += carre[i][i]
        diag2 += carre[i][len(carre) - 1 - i]

    if diag1 == diag2:
        return diag1
    else:
        return -1


def estCarreMagique(carre):
    '''Renvoie True si le carre est magique, False sinon'''

    tests = (testLignesEgales(carre), testColonnesEgales(carre),
             testDiagonalesEgales(carre))

    to_return = True
    for k in range(len(tests)):
        if tests[k] == -1 or tests[k] != tests[0]:
            to_return = False

    return to_return


def estNormal(carre):
    '''Retourne True si contient toutes les valeurs de 1 à n^2, False sinon'''

    manque = [k for k in range(len(carre)**2)]

    for y in range(len(carre)):
        for x in range(len(carre[y])):
            if carre[y][x] in manque:
                manque.pop(manque.index(carre[y][x]))

    if len(manque) == 0:
        return True
    else:
        return False


print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
