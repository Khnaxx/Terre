"""Créez un programme qui affiche l’inverse de la chaîne de caractères donnée en argument.


Exemples d’utilisation :
$> node exo.js “Hello world!”
!dlrow olleH


$> node exo.js “lehciM”
Michel

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.
"""
import sys

phrase = sys.argv[1]
retour = ""
for X in reversed(phrase):
        retour += X
print(retour)
