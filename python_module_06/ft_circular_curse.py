# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_circular_curse.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 12:45:50 by alebaron        #+#    #+#               #
#  Updated: 2026/01/19 13:06:48 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.grimoire import validate_ingredients, record_spell

if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")

    # === Test 1 : Validation d'ingrédients ===

    print("Testing ingredient validation:")
    print(f"validate_ingredients(\"fire air\"): "
          f"{validate_ingredients('fire air')}")
    print(f"validate_ingredients(\"dragon scales\"): "
          f"{validate_ingredients('dragon scales')}")

    # === Test 2 : Enregistrement de sorts ===

    print("\nTesting spell recording with validation:")
    print(f"record_spell(\"Fireball\", \"fire air\"): "
          f"{record_spell('Fireball', 'fire air')}")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): "
          f"{record_spell('Dark Magic', 'shadow')}")

    # === Test 3 : Test d'import ===

    print("\nTesting late import technique:")
    print(f"record_spell(\"Lightning\", \"air\"): "
          f"{record_spell('Lightning', 'air')}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
