"""Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.


Exemples d’utilisation :
$> ruby exo.rb 23:40
11:40PM

Attention : midi et minuit.
"""
import sys

heure,minute = int(sys.argv[1][:2]),int(sys.argv[1][3:])

if heure > 12:
    heure -= 12
    print(f"{heure:02d}:{minute:02d}PM")
elif heure == 0 and minute == 0:
    print(f"{heure:02d}:{minute:02d}")
else: print(f"{heure:02d}:{minute:02d}")
