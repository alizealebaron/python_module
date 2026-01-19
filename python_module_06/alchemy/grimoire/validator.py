# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 12:46:25 by alebaron        #+#    #+#               #
#  Updated: 2026/01/19 12:52:34 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def validate_ingredients(ingredients: str) -> str:

    lst_valid = ["fire", "water", "earth", "air"]
    lst_ingredients = ingredients.split()

    for ingredient in lst_ingredients:
        if ingredient not in lst_valid:
            return (f"{ingredients} - INVALID")

    return (f"{ingredients} - VALID")
