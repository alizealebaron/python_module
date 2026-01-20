# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/20 14:52:03 by alebaron        #+#    #+#               #
#  Updated: 2026/01/20 17:10:43 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from .Combatable import Combatable
from .Magical import Magical
from ex0.Card import Card, Rarity


# +----------------------------------------------------------------+
# |                          Interface                             |
# +----------------------------------------------------------------+

class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: Rarity,
                 defense: int, attack: int, health: int, mana: int):

        Card.__init__(self, name, cost, rarity)
        self.damage = attack
        self.defense = defense
        self.health = health
        self.type = "EliteCard"
        self.mana = mana

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def play(self, game_state: dict) -> dict:

        try:
            _ = game_state["mana_left"]
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        except KeyError:
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": None
            }

    def attack(self, target) -> dict:
        target.health -= self.damage
        return ({
            'attacker': self.name,
            'target': target.name,
            'damage': self.damage,
            'combat_type': 'melee'
        })

    def defend(self, incoming_damage: int) -> dict:

        damage_taken = 0
        damage_block = self.defense

        if (self.defense < incoming_damage):
            damage_taken = incoming_damage - self.defense
        else:
            damage_block = incoming_damage

        self.health -= damage_taken
        return ({
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_block,
            'still_alive': (self.health > 0)
        })

    def cast_spell(self, spell_name: str, targets: list) -> dict:

        for target in targets:
            target.health -= 500

        self.mana -= 4

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [target.name for target in targets],
            "mana_used": 4
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_combat_stats(self) -> dict:
        return {
            'health': self.health,
            'defense': self.defense,
            'attack': self.attack
        }
