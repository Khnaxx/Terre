"""Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.


Exemples d’utilisation :
$> python exo.py 5 2
résultat: 2
reste: 1


$> python exo.py 10 0
erreur.


$> python exo.py 3 5
erreur.
"""
import sys

pre = int(sys.argv[1])
deu = int(sys.argv[2])
if (pre == 0 or deu == 0) or (pre < deu):
    print("erreur.")
else:     
    print("resultat: ",pre // deu)
    print("reste : ", pre % deu)
