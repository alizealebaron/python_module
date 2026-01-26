# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/26 10:58:18 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 12:43:56 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard
from ex0.Card import Rarity


def formatted_info(card: TournamentCard):
    print(f"{card.name} (ID: {card.id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {card.rating}")
    print(f"- Record: {card.wins}-{card.losses}\n")


if __name__ == "__main__":

    print("=== DataDeck Tournament Platform ===\n")

    tournament = TournamentPlatform()

    # === Initialisation des cartes et du tournoi ===

    print("Registering Tournament Cards...\n")

    card1 = TournamentCard("Dragon blanc aux yeux bleus", 7,
                           Rarity.LEGENDARY,
                           1200, 3000, 2500, 1000, "dragon_001")

    card2 = TournamentCard("Dragon noir aux yeux rouges", 7,
                           Rarity.LEGENDARY,
                           1150, 2400, 2000, 1600, "dragon_002")

    formatted_info(card1)
    formatted_info(card2)

    tournament.register_card(card1)
    tournament.register_card(card2)

    # === Création d'un match du tournoi ===

    print("Creating tournament match...")
    result = tournament.create_match(card1.id, card2.id)
    print(f"Match result: {result}")

    # === Affichage du leaderboard ===

    print("\nTournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    i = 1
    for card in leaderboard:
        print(f"{i}. {card.name} - Rating: {card.rating}"
              f"({card.wins}-{card.losses})")
        i += 1

    # === Affichage des statistiques ===

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
