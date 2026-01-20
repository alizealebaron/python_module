# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Deck.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/20 11:29:55 by alebaron        #+#    #+#               #
#  Updated: 2026/01/20 14:48:34 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


import random
from ex0.Card import Card


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class Deck():

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self):

        self.deck = []

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:

        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if (len(self.deck) == 0):
            print("Error: Your deck is empty :c")
            return None
        card = self.deck.pop(0)
        return card

    def get_deck_stats(self) -> dict:

        nb_creature = len([card for card in self.deck
                           if card.type == "Creature"])
        nb_spell = len([card for card in self.deck
                        if card.type == "Spell"])
        nb_artifact = len([card for card in self.deck
                           if card.type == "Artifact"])
        total_cost = sum([card.cost for card in self.deck])

        try:
            avg = round(total_cost / len(self.deck), 1)
        except ZeroDivisionError:
            avg = 0

        return {
            'total_card': len(self.deck),
            'creatures': nb_creature,
            'spells': nb_spell,
            'artifacts': nb_artifact,
            'avg_cost': avg
        }
