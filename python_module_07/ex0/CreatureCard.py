# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  CreatureCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 13:28:14 by alebaron        #+#    #+#               #
#  Updated: 2026/01/20 11:54:37 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from .Card import Card, Rarity


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class CreatureCard(Card):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, name: str, cost: int, rarity: Rarity,
                 attack: int, health: int) -> None:

        try:
            if attack <= 0:
                attack = 100
                raise ValueError("Attack must be a positive number.")
            if health <= 0:
                health = 100
                raise ValueError("Health must be a positive number.")
        except ValueError as e:
            print(f"Error: {e}")

        super().__init__(name, cost, rarity)

        self.attack = attack
        self.health = health

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def get_card_info(self):
        return ({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })

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

    def attack_target(self, target: Card) -> dict:

        try:
            if (target.health <= 0 or self.health <= 0):
                return {
                    "attacker": self.name,
                    "target": target.name,
                    "damage_dealt": 0,
                    "combat_resolved": False
                }
        except (AttributeError, KeyError):
            return {
                "attacker": self.name,
                "target": "Target invalid",
                "damage_dealt": 0,
                "combat_resolved": False
            }
        else:
            target.health -= self.attack
            return {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": True
            }
