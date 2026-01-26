# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 11:02:18 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 10:48:36 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from .GameStrategy import GameStrategy
from ex0.Card import Card


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list[Card], battlefield: list[Card]) -> dict:

        res_round = {
            'cards_played': None,
            'mana_used': 0,
            'targets_attacked': [],
            'damage_dealt': 0
        }

        creature_hand = self.prioritize_targets(hand)
        total_mana_round = sum(card.cost for card in creature_hand)
        targets = self.prioritize_targets(battlefield)

        if (len(hand) == 0 or len(battlefield) == 0) or len(targets) == 0:
            return res_round

        res_round['cards_played'] = hand
        res_round['mana_used'] = total_mana_round
        res_round['cards_played'] = [card.name for card in creature_hand]

        for card in creature_hand:
            if not targets:
                break

            if targets[0].name not in res_round['targets_attacked']:
                res_round['targets_attacked'].append(targets[0].name)

            if card.attack >= targets[0].health:
                res_round["damage_dealt"] += targets[0].health
                targets.pop(0)
            else:
                targets[0].health -= card.attack
                res_round["damage_dealt"] += card.attack

        return res_round

    def get_strategy_name(self) -> str:
        return ("Aggressive")

    def prioritize_targets(self, available_targets: list) -> list:
        valid_targets = [target for target
                         in available_targets if hasattr(target, "health")]

        return sorted(valid_targets, key=lambda target: target.health)
