"""Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.

Exemples d’utilisation :
$> ruby exo.rb je suis solide !
je
suis
solide
!
"""
import sys

for arg in sys.argv[1:]:
    print(arg)
