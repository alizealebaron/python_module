# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Card.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 13:32:21 by alebaron        #+#    #+#               #
#  Updated: 2026/01/19 15:31:36 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+

from typing import Dict
from abc import ABC, abstractmethod
from enum import Enum

# +----------------------------------------------------------------+
# |                           Type Enum                            |
# +----------------------------------------------------------------+

class Rarity(Enum):
    """"Enum class for rarity type."""
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    UNIQUE = "Unique"

# +----------------------------------------------------------------+
# |                       Classe abstraite                         |
# +----------------------------------------------------------------+

class Card(ABC):
    
    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, name: str, cost: int, rarity: Rarity):
        super().__init__()

        self.name = name
        self.cost = cost
        self.rarity = rarity

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value
        }

    def is_playable(self, available_mana: int) -> bool:
        return (available_mana >= self.cost)
