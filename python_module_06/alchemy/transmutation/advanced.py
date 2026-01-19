# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  advanced.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 12:21:31 by alebaron        #+#    #+#               #
#  Updated: 2026/01/19 12:38:53 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return (f"Philosopher's stone created using {lead_to_gold()} "
            f"and {healing_potion()}")


def elixir_of_life() -> str:
    return ("Elixir of life: eternal youth achieved!")
