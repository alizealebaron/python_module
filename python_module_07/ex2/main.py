# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/20 14:51:57 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 10:56:31 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard

if __name__ == "__main__":

    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    # === Initialisation des cartes ===

    elite = EliteCard("Dragon rouge Archdémon Meurtri", 8,
                      Rarity.LEGENDARY, 2500, 3000, 3000, 8)
    target = CreatureCard("Clayman", 4, Rarity.RARE, 850, 3000)
    target2 = CreatureCard("Neos", 7, Rarity.COMMON, 2500, 2000)

    # === Phase de combat ===

    print(f"Playing {elite.name} ({elite.type}):\n")

    game_state = {
        "mana_left": 15,
        "target": target,
    }

    print("Combat phase:")
    print(f"Attack result: {elite.attack(target)}")
    print(f"Defense result: {elite.defend(target.attack)}")

    # === Phase de magie ===

    print("\nMagic phase:")

    print(f"Spell cast: "
          f"{elite.cast_spell('Oblitération suprême', [target, target2])}")
    print(f"Mana channel: {elite.channel_mana(4)}")

    print("\nMultiple interface implementation successful!")
