# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/27 13:24:20 by alebaron        #+#    #+#               #
#  Updated: 2026/01/29 10:36:45 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


import os
import sys
import site


# +----------------------------------------------------------------+
# |                           Méthodes                             |
# +----------------------------------------------------------------+

def env():

    path = sys.executable

    print("\nMATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {path}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")

    # Pour récupéré le chemin d'installation de package
    # On récupère tous et on affiche uniquement le 1er
    # C'est celui qui sera utilisé par défaut

    print("Package installation path:")
    print(f"{site.getsitepackages()[0]}")


def not_env():

    path = sys.executable
    version = sys.version_info.minor

    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {path}.{version}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows\n")

    print("Then run this program again.")


# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

if __name__ == "__main__":

    # Si base_prefix est différent de prefix :
    # On est dans un environnement
    if (sys.base_prefix == sys.prefix):
        not_env()
    else:
        env()
