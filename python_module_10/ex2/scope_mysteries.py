# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 17:06:01 by alebaron        #+#    #+#               #
#  Updated: 2026/02/02 11:30:11 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from typing import Callable, Any
from random import randint


# +----------------------------------------------------------------+
# |                          Méthodes                              |
# +----------------------------------------------------------------+


def mage_counter() -> Callable:
    cpt = 0

    def counting_stars() -> int:
        nonlocal cpt
        cpt += 1
        return cpt

    return counting_stars


def spell_accumulator(initial_power: int) -> Callable:
    cpt = initial_power

    def counting_power(power: int) -> int:
        nonlocal cpt
        cpt += power
        return cpt

    return counting_power


def enchantment_factory(enchantment_type: str) -> Callable:
    tmp = enchantment_type

    def enchant_item(item: str) -> str:
        return (f"{tmp} {item}")

    return enchant_item


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any | str:
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


# +----------------------------------------------------------------+
# |                            Main                                |
# +----------------------------------------------------------------+

if __name__ == "__main__":

    print("=========== Test : mage_counter ===========\n")

    count = mage_counter()
    for i in range(0, 10):
        print(f"Call {i + 1}: {count()}")

    print("\n=========== Test : spell_accumulator ===========\n")

    initial_power = 0
    final_power = spell_accumulator(initial_power)
    print(f"Start power: {final_power(initial_power)}")
    for i in range(0, 3):
        power_to_add = randint(0, 100)
        print(f"Current power: {final_power(power_to_add)}"
              f"({power_to_add} added)")

    print(f"Final power : {final_power(0)}")

    print("\n=========== Test : enchantment_factory ===========\n")

    enchantments = {
        "Fire aspect": "Sword",
        "Power": "Bow",
        "Respiration": "Helmet",
        "Thorns": "Chestplate",
        "Swift Sneak": "Leggings",
        "Frost Walker": "Boots",
        "Lure": "Fishing Rod",
        "Efficiency": "Pickaxe"
    }
    for enchantment, item in enchantments.items():
        enchant = enchantment_factory(enchantment)
        print(enchant(item))

    print("\n=========== Test : memory_vault ===========\n")

    vault = memory_vault()
    vault["store"]("canard", 50)
    print("Recalling stored memory...")
    print(f"Canard: {vault['recall']('canard')}\n")
    print("Recalling no stored memory...")
    print(f"Ornithorynque: {vault['recall']('ornithorynque')}")
