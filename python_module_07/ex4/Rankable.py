# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Rankable.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/26 10:57:45 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 11:24:54 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from abc import ABC, abstractmethod


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class Rankable(ABC):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self, rating: int):
        self.wins = 0
        self.losses = 0
        self.rating = rating

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
