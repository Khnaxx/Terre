"""Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.

Exemples d’utilisation :
$> ruby exo.rb 11 40 34
34

$> ruby exo.rb 2 1 3
2

$> ruby exo.rb 2 2 2
erreur.
"""

import sys

number = []

for X in sys.argv[1:]:
    number.append(int(X))    
if number[0] == number[1]== number[2]:
    print("erreur.")
    exit()
milieu = sum(number) / len(number)
delta = sum(number)
proche = sum(number)

for nbr in number:
    if abs(nbr - milieu) < delta:
        delta = abs(nbr - milieu)
proche = nbr


print(proche)
