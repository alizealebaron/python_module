# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 11:02:45 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 10:53:20 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from .CardFactory import CardFactory
from .GameStrategy import GameStrategy
import random


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class GameEngine():

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self):

        self.factory = None
        self.strat = None
        self.nb_turn = 0
        self.nb_damage = 0
        self.deck = None

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:

        self.factory = factory
        self.strat = strategy
        self.deck = factory.create_themed_deck(15)

    def simulate_turn(self) -> None:

        all_card = [card for card in self.deck["creature"]]

        hand = random.choices(all_card, k=3)
        battlefield = random.choices(self.deck["creature"], k=2)

        turn = self.strat.execute_turn(hand, battlefield)

        self.nb_turn += 1
        self.nb_damage += turn["damage_dealt"]

        print(f"Actions: {turn}")

    def get_engine_status(self) -> dict:
        return {
            "factory": self.factory.__class__.__name__,
            "strategy": self.strat.__class__.__name__,
            "turns_simulated": self.nb_turn,
            "total_damage": self.nb_damage,
            "cards_created": self.factory.deck_size
        }
