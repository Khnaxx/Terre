""" Créez un programme qui affiche le nombre de caractères d’une chaîne de caractères passée en argument.


Exemples d’utilisation :
$> python exo.py “Hello world!”
12


$> python exo.py
erreur.


$> python exo.py “Bonjour” “Aurevoir”
erreur.

$> python exo.py 10
erreur.
"""

import sys

if len(sys.argv) <1 or len(sys.argv) > 2:
    print("erreur.")
elif sys.argv[1].isdigit():
    print("erreur.")
else:
    phrase = sys.argv[1]
    print(len(phrase))
