""" Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..


Exemples d’utilisation :
$> ruby exo.rb 2
pair

$> ruby exo.rb 5
impair


$> ruby exo.rb Bonjour
Tu ne me la mettras pas à l’envers.

$> ruby exo.rb
Tu ne me la mettras pas à l’envers.


Attention : gérez aussi les entiers négatifs.
"""

import sys
if len(sys.argv)<2:
     print("Tu ne me la mettras pas à l'envers")  
elif not sys.argv[1].lstrip("-").isdigit() :
    print("Tu ne me la mettras pas à l'envers")
else: 
    number = abs(int(sys.argv[1]))
    if number % 2 ==0:
        print("pair")
    else: print("impair")
