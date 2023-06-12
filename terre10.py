"""Créez un programme qui affiche si un nombre est premier ou pas.


Exemples d’utilisation :
$> node exo.js 5
Oui, 5 est un nombre premier.

$> node exo.js 6
Non, 6 n’est pas un nombre premier.

Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.
"""
import sys
import math

if len(sys.argv) == 2:
    for X in range(1,len(sys.argv)):
        if sys.argv[X].isalpha():
            print("erreur.")
            break
    for X in range(1,len(sys.argv)):
        if sys.argv[X].isdigit() and sys.argv[X] != 1 or sys.argv[X] != 0:
            continue
        else:
            print("erreur.")
            break
    else:
        nbre = int(sys.argv[1])
        for i in range(2,nbre):
            if (nbre % i == 0):
                print(f"Non, {nbre} n'est pas un nombre premier.")
                break
        else: print(f"Oui, {nbre} est un nombre premier.")
else: print("erreur.")
