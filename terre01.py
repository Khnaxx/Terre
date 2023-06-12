"""Créez un programme qui affiche son nom de fichier.

Exemples d’utilisation :
$> node exo.js
exo.js

$> node crevette.js
crevette.js
"""
import sys 
import os 
print(os.path.basename(sys.argv[0]))
