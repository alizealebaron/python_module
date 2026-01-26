# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 13:28:26 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 10:55:47 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")

    card1 = CreatureCard("Diapason de l'âme", 3, Rarity.RARE, 500, 200)
    card2 = CreatureCard("Dragon Ascendant Rouge", 6, Rarity.EPIC, 2100, 1600)

    print("CreatureCard Info:")
    print(card1.get_card_info())

    mana = 6
    print(f"\nPlaying {card1.name} with {mana} mana available:")
    print(f"Playable: {card1.is_playable(mana)}")
    print(f"Play result: {card1.play({'mana_left': mana})}")

    print(f"\n{card1.name} attacks {card2.name}:")
    print(f"Attack result: {card1.attack_target(card2)}")

    mana = 3
    print(f"\nTesting insufficient mana ({mana} available):")
    print(f"Playable: {card2.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")
