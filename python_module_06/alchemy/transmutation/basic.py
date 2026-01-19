# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  basic.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 12:21:33 by alebaron        #+#    #+#               #
#  Updated: 2026/01/19 12:38:49 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return (f"Lead transmuted to gold using {create_fire()}")


def stone_to_gem() -> str:
    return (f"Stone transmuted to gem using {create_earth()}")
