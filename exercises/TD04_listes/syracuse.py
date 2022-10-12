def syracuse(n):
    '''Retourne la suite de syracuse correspondante à n'''

    to_return = [n]

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1

        to_return.append(int(n))

    return to_return


def testeConjecture(n_max):
    '''Test les n_max premiers entiers à la conjecture de Collatz'''

    contre_exemple = False
    for i in range(1, n_max+1):
        values = syracuse(i)

        if values[len(values) - 1] != 1:
            contre_exemple = True
            break
    return not contre_exemple


def tempsVol(n):
    '''Retourne le temps de vol de n'''

    return len(syracuse(n)) - 1


def tempsVolListe(n_max):
    '''Retourne la liste de tous les temps de vol des n premiers entiers'''

    to_return = []
    for k in range(1, n_max + 1):
        to_return.append(tempsVol(k))

    return to_return


def altitude(n):
    '''Retourne l'altitude d'un n donné'''

    a = syracuse(n)
    a.sort()

    return a[len(a)-1]


def altitudeMax(n_max):
    '''Retourne un tuple de l'altitude max des n_max premiers entiers \
        et son n coreespondant'''

    max = 0
    n = 0

    for k in range(1, n_max):
        if altitude(k) > max:
            max = altitude(k)
            n = k

    return (max, n)


r = altitudeMax(10000)
print("L'altitude maximale trouvée est", r[0], " pour n =", r[1])
