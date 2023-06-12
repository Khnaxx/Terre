""" L'alphabet
Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.

Exemples d’utilisation :
$> python exo.py
abcdefghijklmnopqrstuvwxyz
$>

Attention : votre programme devra utiliser une boucle.
"""
alphabet = ""
asc = ord("a")
for X in range(asc,asc+26):
    alphabet += (str(chr(X)))

print(alphabet)