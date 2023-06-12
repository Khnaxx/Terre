""" Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.


Exemples d’utilisation :
$> python exo.py n
nopqrstuvwxyz
$>


Attention : votre programme devra utiliser une boucle.
"""


import sys

dep = ord(sys.argv[1])
fin = ord("z")
alpha = ""
for X in range(dep,fin+1):
    alpha += str(chr(X))
print(alpha)
