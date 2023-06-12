"""Créez un programme qui détermine si une liste d’entiers est triée ou pas.


Exemples d’utilisation :
$> ruby exo.rb 9 8 3
Pas triée !

$> ruby exo.rb 3 8 9 12
Triée !

$> ruby exo.rb “Salut”
erreur.
"""

import sys

liste = []
if len(sys.argv) < 3:
    print("erreur.")
    exit()
else:
    for X in sys.argv[1:]:
        if X.isalpha():
            print("erreur.")
            exit()
    else:
        for X in sys.argv[1:]:
            liste.append(int(X))
        liste_triée = sorted(liste)

        if liste_triée == liste:
            print("Triée !")
        else: print("Pas triée !")

        
