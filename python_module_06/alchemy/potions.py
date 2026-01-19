# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 0026/01/19 11:36:31 by lebaron         #+#    #+#               #
#  Updated: 2026/01/19 11:52:24 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import alchemy.elements


def healing_potion():

    fire = alchemy.elements.create_fire()
    water = alchemy.elements.create_water()

    return (f"Healing potion brewed with {fire} and {water}")


def strength_potion():

    fire = alchemy.elements.create_fire()
    earth = alchemy.elements.create_earth()

    return (f"Strength potion brewed with {earth} and {fire}")


def invisibility_potion():

    air = alchemy.elements.create_air()
    water = alchemy.elements.create_water()

    return (f"Strength potion brewed with {air} and {water}")


def wisdom_potion():

    air = alchemy.elements.create_air()
    water = alchemy.elements.create_water()
    fire = alchemy.elements.create_fire()
    earth = alchemy.elements.create_earth()

    return (f"Wisdom potion brewed with all elements: "
            f"{fire} {water} {air} {earth}")
