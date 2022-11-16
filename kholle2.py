#   Exercice 3

n = int(input("Choisissez un nombre entre 1 et 10 : "))
somme = 0

#       Il n'est pas nécessaire de vérifier pour les nombres inférieurs à n
#   car un nombre n supérieur à un nombre n' ne peut pas être un de ses
#   diviseurs.

for i in range(n, 100001):
    if i % n == 0:
        somme += i

print("La somme de tous les entiers divisibles par n entre 1 et \
100 000 est", somme)
