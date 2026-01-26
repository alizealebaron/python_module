# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/26 10:58:07 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 12:43:13 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from ex4.TournamentCard import TournamentCard


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class TournamentPlatform():

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self):
        self.lst_card = []
        self.nb_match = 0

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def register_card(self, card: TournamentCard) -> str:
        self.lst_card.append(card)

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        if (card1_id == card2_id):
            raise Exception("Error: A card can't battle itself.")

        player1 = [card for card in self.lst_card if card.id == card1_id]
        if (len(player1) == 0):
            raise Exception("Error: Card1 is'nt registered yet.")

        player2 = [card for card in self.lst_card if card.id == card2_id]
        if (len(player2) == 0):
            raise Exception("Error: Card2 is'nt registered yet.")

        player1 = player1[0]
        player2 = player2[0]

        player1.max_health = player1.health
        player2.max_health = player2.health

        while player1.health > 0 and player2.health > 0:
            player1.attack(player2)
            if (player2.health <= 0):
                break
            player2.attack(player1)

        if (player1.health <= 0):
            winner = player2
            looser = player1
        else:
            winner = player1
            looser = player2

        winner.update_wins(1)
        looser.update_losses(1)

        self.nb_match += 1
        return ({
            "winner": winner.id,
            "loser": looser.id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": looser.calculate_rating(),
        })

    def get_leaderboard(self) -> list:
        return sorted(self.lst_card, key=lambda card: card.rating,
                      reverse=True)

    def generate_tournament_report(self) -> dict:
        return {'total_cards': len(self.lst_card),
                'matches_played': self.nb_match,
                'avg_rating': sum(card.rating for card in self.lst_card) /
                len(self.lst_card),
                'platform_status': 'active'}
