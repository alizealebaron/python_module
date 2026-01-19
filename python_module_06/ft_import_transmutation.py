# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_import_transmutation.py                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/01/19 11:36:59 by lebaron         #+#    #+#               #
#  Updated: 2026/01/19 12:29:31 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def full_import() -> None:
    import alchemy.elements

    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def spec_import() -> None:
    from alchemy.elements import create_water

    print("\nMethod 2 - Specific function import:")
    print(f"alchemy.elements.create_fire(): {create_water()}")


def alias_import() -> None:
    from alchemy.potions import healing_potion as heal

    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")


def multi_import() -> None:
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion

    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")

    # === Méthode 1 : Import total ===
    full_import()

    # === Méthode 2 : Import spécifique ===
    spec_import()

    # === Méthode 3 : Import avec alias ===
    alias_import()

    # === Méthode 4 : Import multiple ===
    multi_import()

    print("\nAll import transmutation methods mastered!")
