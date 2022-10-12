import time


def tempsEnSecondes(temps):

    """Fonction qui convertit un temps en seconde"""
    return int(temps[0])*86400 + int(temps[1])*3600 + \
        int(temps[2])*60 + int(temps[-1])


def secondesEnTemps(secondes):

    """ Fonction qui convertit un temp en secondes"""

    temps = [0, 0, 0, 0]

    jours = 0
    heures = 0
    minutes = 0

    jours = int(secondes/86400)
    secondes -= jours*86400
    heures = int(secondes/3600)
    secondes -= heures*3600
    minutes = int(secondes/60)
    secondes -= minutes*60

    temps[3] = secondes
    temps[2] = minutes
    temps[1] = heures
    temps[0] = jours

    return temps


def afficheTemps(temps):

    """Fonction qui affiche le temps"""

    if temps[0] == 1:
        print(temps[0], "jour")
    if temps[0] > 1:
        print(temps[0], "jours")

    if temps[1] == 1:
        print(temps[1], "heure")
    if temps[1] > 1:
        print(temps[1], "heures")

    if temps[2] == 1:
        print(temps[2], "minute")
    if temps[2] > 1:
        print(temps[2], "minutes")

    if temps[3] == 1:
        print(temps[3], "seconde")
    if temps[3] > 1:
        print(temps[3], "secondes")


def demandeTemps():

    """Fonction qui demande à l'utilisateur de saisir un temps"""

    temps = [0, 0, 0, 0]

    temps[0] = int(input("Jours : "))

    temps[1] = 25
    while temps[1] > 23 or temps[1] < 0:
        temps[1] = int(input("Heures (0 ~ 23) : "))

    temps[2] = 61
    while temps[2] > 59 or temps[2] < 0:
        temps[2] = int(input("Minutes (0 ~ 59) : "))

    temps[3] = 61
    while temps[3] > 59 or temps[3] < 0:
        temps[3] = int(input("Secondes (0 ~ 59) : "))

    return temps


def sommeTemps(temps1, temps2):

    """Fonction qu renvoie la somme de deux temps"""

    return secondesEnTemps(tempsEnSecondes(temps1) + tempsEnSecondes(temps2))


def proportionTemps(temps, proportion):

    """Fonction qui donne la proportion souhaité d'un temps donné"""

    return secondesEnTemps(tempsEnSecondes(temps) * proportion)


def bisextile(jour):

    """Fonction qui affiche les années bisextiles depuis 1970"""

    an = 1970
    while jour >= 0:
        an += 1
        if (an % 4 == 0 and (an % 100 != 0 or an % 400 == 0)):
            print(an)
            jour -= 366
        else:
            jour -= 365


def tempsEnDate(temps):

    """Fonction qui donne la date"""

    an = (int(temps[0]) / 365) + 1970
    jour = (int(temps[0]) + 1) % 365

    return (an, jour, temps[1], temps[2], temps[3])


def afficheDate(date):

    """Fonction qui affiche la date"""

    date = time.gmtime()

    print(date[0], date[1], date[2], date[3], date[4])


def nombreBisextile(jour):

    """Fonction qui retourne le nombre de jours bisextiles depuis 1970"""

    compte = 0
    an = 1970

    while jour >= 0:
        an += 1
        compte += 1
        if (an % 4 == 0 and (an % 100 != 0 or an % 400 == 0)):
            jour -= 366
        else:
            jour -= 365

    return compte


def tempsEnDateBisextile(temps):

    """Fonction qui change le temps en date en \
        prenant en compte les années bisextiles"""

    jour = int(tempsEnSecondes(temps)) // 3600 // 24
    bi = int(nombreBisextile(jour))
    an = 1970

    jour_ = int(jour - bi)

    while jour_ >= 365:
        an += 1
        jour_ -= 365

    return (an, "an", jour_, "jour", temps[2], "minute", temps[3], "seconde")
