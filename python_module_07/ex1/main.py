# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/20 11:29:48 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 10:56:03 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, Effect_Type
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

if __name__ == "__main__":

    print("=== DataDeck Deck Builder ===\n")

    # === Création des cartes et ajout au deck ===

    print("Building deck with different card types...")

    card1 = CreatureCard("Diapason de la vision", 2, Rarity.COMMON, 400, 400)
    card2 = SpellCard("Appel de diapason", 2, Rarity.COMMON,
                      Effect_Type.DAMAGE)
    card3 = ArtifactCard("Appel par la tombe", 3, Rarity.EPIC, 1,
                         "Revive one ally this turn")

    deck = Deck()
    deck.add_card(card1)
    deck.add_card(card2)
    deck.add_card(card3)

    # === Affichage des statistiques du deck ===

    print(f"Deck Stats: {deck.get_deck_stats()}")

    # === Piocher et jouer des cartes ===

    print("\nDrawing and playing cards:\n")

    game_state = {'mana_left': 15}

    card = deck.draw_card()

    print(f"Drew: {card.name} ({card.type})")
    print(f"Play result: {card.play(game_state)}\n")

    card = deck.draw_card()

    print(f"Drew: {card.name} ({card.type})")
    print(f"Play result: {card.play(game_state)}\n")

    card = deck.draw_card()

    print(f"Drew: {card.name} ({card.type})")
    print(f"Play result: {card.play(game_state)}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")
