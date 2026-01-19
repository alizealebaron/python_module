# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 12:46:31 by alebaron        #+#    #+#               #
#  Updated: 2026/01/19 13:06:15 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    is_valid = validate_ingredients(ingredients)

    if "INVALID" in is_valid:
        return (f"Spell rejected: {spell_name} ({is_valid})")
    else:
        return (f"Spell recorded: {spell_name} ({is_valid})")
