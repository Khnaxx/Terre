"""Créez un programme qui affiche le résultat d’une puissance.


L’exposant ne pourra pas être négatif.


Exemples d’utilisation :
$> node exo.js 2 3
8

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.
"""
import sys
if len(sys.argv) == 3:
    for X in range(1,len(sys.argv)):
        if sys.argv[X].isalpha():
            print("erreur.")
            break
    for X in range(1,len(sys.argv)):
        if sys.argv[X].isdigit():
            continue
        else:
            print("erreur.")
            break
    else: print(int(sys.argv[1]) ** int(sys.argv[2]))
else: print("erreur.")
