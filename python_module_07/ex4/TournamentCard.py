# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/26 10:57:56 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 12:42:06 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class TournamentCard(Card, Combatable, Rankable):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, name: str, cost: int, rarity: Rarity, rating: int,
                 attack: int, health: int, defense: int, id: str):
        Card.__init__(self, name, cost, rarity)
        Rankable.__init__(self, rating)
        self.damage = attack
        self.health = health
        self.max_health = health
        self.defense = defense
        self.id = id

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

    def attack(self, target: Card) -> dict:
        target.defend(self.damage)
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

    def calculate_rating(self) -> int:
        self.rating += (self.wins - self.losses) * 15
        if (self.rating < 0):
            self.rating = 0

    def get_tournament_stats(self) -> dict:
        return {
            'wins': self.wins,
            'losses': self.losses
        }

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.damage,
            'defense': self.defense,
            'health': self.health
        }
