# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ArtifactCard.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/20 11:29:51 by alebaron        #+#    #+#               #
#  Updated: 2026/01/20 14:47:53 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from ex0.Card import Card


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class ArtifactCard(Card):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):

        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "Artifact"

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def play(self, game_state: dict) -> dict:
        try:
            _ = game_state["mana_left"]
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
            }
        except KeyError:
            return {
                "card_played": None,
                "mana_used": 0,
                "effect": None
            }

    def activate_ability(self) -> dict:
        return ({"effect": self.effect})
