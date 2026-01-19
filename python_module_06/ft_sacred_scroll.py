# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
# ft_sacred_scroll.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
# By: alebaron <alebaron@student.42.fr>          +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
# Created: 2026/01/19 10:47:26 by alebaron         #+#    #+#               #
# Updated: 2026/01/19 11:35:13 by alebaron         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


import alchemy


if __name__ == "__main__":

    print("=== Sacred Scroll Mastery ===\n")

    # === Test 1 : Accès direct au éléments ===
    print("Testing direct module access:")

    print(f"alchemy.elements.create_fire():{alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water():{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth():{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air():{alchemy.elements.create_air()}")

    # === Test 2 : Accès par __init__.py ===
    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire():{alchemy.create_fire()}")
    print(f"alchemy.create_water():{alchemy.create_water()}")

    try:
        print(f"alchemy.create_earth():{alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_air():{alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    # === Affichage des méta-datas ===
    print("\nPackage metadata:")

    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")