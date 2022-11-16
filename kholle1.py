#   Exercice 1 :

#       Ce programme génére une erreur liée à l'indentation à la troisième
#   ligne car après un if, il faut indenter le bloc qui s'execute si la
#   condition est vérifiée.

#   Exercice 2 :

x = 3
y = 4
z = 5

#   Théorème de Pythagore : c**2 = a**2 + b**2, où a, b et c sont les
#   longueurs des côtés du triangle rectangle T dont c est l'hypothénuse

if x**2 + y**2 == z**2 or y**2 + z**2 == x**2 or x**2 + z**2 == y**2:
    print("Le triangle T est rectangle. (Il vérifie le théorème de Pythagore)")
else:
    print("Le triangle T n'est pas rectangle. (Le théorème de Pythagore n'est \
pas vérifié)")
