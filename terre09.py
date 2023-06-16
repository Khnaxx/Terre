"""Créez un programme qui affiche la racine carrée d’un entier positif.


Exemples d’utilisation :
$> node exo.js 9
3

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.
"""
import sys
import math
if len(sys.argv) == 2:
    for X in range(1,len(sys.argv)):
        if sys.argv[X].isalpha():
            print("erreur.")
            exit()
    for X in range(1,len(sys.argv)):
        if sys.argv[X].isdigit():
            continue
        else:
            print("erreur.")
            exit()
    else: print(int(math.sqrt(int(sys.argv[1]))))
else: print("erreur.")
