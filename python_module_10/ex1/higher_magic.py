# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 15:32:57 by alebaron        #+#    #+#               #
#  Updated: 2026/01/31 17:05:25 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from typing import Callable


# +----------------------------------------------------------------+
# |                          Méthodes                              |
# +----------------------------------------------------------------+

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda x: (base_spell(x) * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(target: str) -> str:
        if condition():
            return spell(target)
        else:
            return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def make_a_list(target: str) -> list[str]:
        liste = []
        for spell in spells:
            liste.append(spell(target))
        return liste

    return make_a_list


# +----------------------------------------------------------------+
# |                            Main                                |
# +----------------------------------------------------------------+

if __name__ == "__main__":

    print("=========== Test : spell_combiner ===========\n")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    target = "canard"
    combined = spell_combiner(fireball, heal)
    print(f"{combined(target)[0]}, {combined(target)[1]}.")

    print("\n=========== Test : power_amplifier ===========\n")

    def magic_missile(power: int) -> int:
        return power

    mega_magic_missile = power_amplifier(magic_missile, 3)
    print(f"Original: {magic_missile(5)}, Amplified: {mega_magic_missile(5)}")

    print("\n=========== Test : conditional_caster ===========\n")

    def ret_true() -> bool:
        return True

    conditional_caste = conditional_caster(ret_true, fireball)
    print(conditional_caste(target))

    print("\n=========== Test : spell_sequence ===========\n")

    liste = [fireball, heal, fireball]

    spell_sequenc = spell_sequence(liste)
    print(spell_sequenc(target))
