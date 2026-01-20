# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  SpellCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/20 11:29:58 by alebaron        #+#    #+#               #
#  Updated: 2026/01/20 14:49:13 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from ex0.CreatureCard import CreatureCard
from ex0.Card import Card, Rarity
from enum import Enum


# +----------------------------------------------------------------+
# |                           Type Enum                            |
# +----------------------------------------------------------------+

class Effect_Type(Enum):
    """"Enum class for rarity type."""
    DAMAGE = "Deal 300 damage to target"
    HEAL = "Heal 300 health to target"
    BUFF = "Target gains 300 attack"
    DEBUFF = "Target loose 300 attack"


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class SpellCard(Card):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, name: str, cost: int, rarity: Rarity,
                 effect_type: Effect_Type):

        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def play(self, game_state: dict) -> dict:
        try:
            _ = game_state["mana_left"]
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type.value
            }
        except KeyError:
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": None
            }

    def resolve_effect(self, targets: list[CreatureCard]) -> dict:
        for target in targets:
            if self.effect_type == Effect_Type.HEAL:
                target.health += 300
            elif self.effect_type == Effect_Type.DAMAGE:
                target.health -= 300
            elif self.effect_type == Effect_Type.BUFF:
                target.attack += 300
            else:
                target.attack -= 300

        return ({"effect": self.effect_type.value})
