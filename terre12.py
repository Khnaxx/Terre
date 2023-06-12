"""Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.


Exemples d’utilisation :
$> ruby exo.rb 11:40PM
23:40

Attention : midi et minuit.

"""
import sys

if len(sys.argv[1]) == 7:
    
    heure,minute,tem = int(sys.argv[1][:2]),int(sys.argv[1][3:5]),str(sys.argv[1][5:])
    if tem == "AM":
        print(f"{heure:02d}:{minute:02d}{tem}")
    else :
        heure += 12
        print(f"{heure:02d}:{minute:02d}")

