# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 11:02:34 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 10:56:51 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex1.SpellCard import SpellCard, Effect_Type
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
import random


# +----------------------------------------------------------------+
# |                            Classe                              |
# +----------------------------------------------------------------+

class FantasyCardFactory(CardFactory):

    # +------------------------------------------------------------+
    # |                        Constructeur                        |
    # +------------------------------------------------------------+

    def __init__(self):

        self.data = {
            "creature": {
                "Chevalier du flamboiement des ténébres":
                [6, Rarity.LEGENDARY, 2200, 800],
                "Sentinelle au grand bouclier": [4, Rarity.COMMON, 100, 2600],
                "Gardien Celte": [4, Rarity.COMMON, 1400, 1200],
                "Chevalier de la reine": [4, Rarity.RARE, 1500, 1600],
                "Chevalier du roi": [4, Rarity.COMMON, 1600, 1400],
                "Chevalier du valet": [5, Rarity.RARE, 1900, 1000],
                "Crane Invoqué": [6, Rarity.EPIC, 2500, 1200],
                "Dragon Crane noir": [9, Rarity.LEGENDARY, 3200, 2500],
                "Dragon blanc aux yeux bleus": [8, Rarity.UNIQUE, 3000, 2500],
                "Bébé dragon aux yeux rouges": [3, Rarity.RARE, 1200, 700],
                "Poussin B. aux yeux rouges": [1, Rarity.COMMON, 800, 500],
                "Ultime dragon noir aux yeux rouges":
                [11, Rarity.UNIQUE, 4000, 3000],
                "Bébébcérasaure": [2, Rarity.COMMON, 500, 500],
                "Destrier des chevaliers floraux":
                [3, Rarity.COMMON, 400, 800],
                "Kuribeille": [1, Rarity.COMMON, 300, 200],
                "Gilasaure": [3, Rarity.COMMON, 1400, 400],
                "Protecteur Mortuaire": [3, Rarity.RARE, 600, 1300]
            },
            "spell":
            {
                "Epée de lumière révélatrice":
                [3, Rarity.COMMON, Effect_Type.BUFF],
                "Gaia cramoisie": [4, Rarity.RARE, Effect_Type.HEAL],
                "Polymérisation": [3, Rarity.COMMON, Effect_Type.BUFF],
                "Rituel de magie noire": [5, Rarity.EPIC, Effect_Type.DEBUFF],
                "Transfomine": [1, Rarity.COMMON, Effect_Type.DEBUFF],
                "Invitation des ténèbres":
                [2, Rarity.RARE, Effect_Type.DAMAGE],
                "Bénédiction Naturia": [2, Rarity.COMMON, Effect_Type.HEAL],
                "Offrande aux damnés":
                [6, Rarity.LEGENDARY, Effect_Type.DAMAGE],
                "Rituel du dragon blanc":
                [3, Rarity.LEGENDARY, Effect_Type.HEAL],
                "Hommage torrentiel": [2, Rarity.UNIQUE, Effect_Type.BUFF]
            },
            "artifact":
            {
                "Protection Espillon": [6, Rarity.RARE, 2, "BUFF ALY PV 500"],
                "Rage suprême": [8, Rarity.EPIC, 2, "BUFF ALY ATK 500"],
                "Epée de la force de la lumière":
                [9, Rarity.LEGENDARY, 3, "DEBUFF ENMY ATK 500"]
            }
        }

        self.lst_creature = [name for name in self.data["creature"]]
        self.lst_spell = [name for name in self.data["spell"]]
        self.lst_artifact = [name for name in self.data["artifact"]]

        self.deck_size = 0

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def create_creature(self, name_or_power: str | int | None = None) -> Card:

        values = self.data["creature"][name_or_power]
        return CreatureCard(name_or_power, *values)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:

        values = self.data["spell"][name_or_power]
        return SpellCard(name_or_power, *values)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:

        values = self.data["artifact"][name_or_power]
        return ArtifactCard(name_or_power, *values)

    def create_themed_deck(self, size: int) -> dict:

        deck = {
            "creature": [],
            "spell": [],
            "artifact": []
        }

        try:
            self.deck_size = int(size)
            if (self.deck_size <= 0):
                raise ValueError("A deck requires a minimum number of cards.")
        except ValueError as e:
            print(f"Error: {e}")
            return None

        if self.deck_size < 3:
            # Si on a moins de trois cartes, on ajoute que des créatures
            for i in range(0, self.deck_size):
                deck["creature"].append(self.create_creature(
                    random.choice(self.lst_creature)))
        else:
            lst_type_card = [name for name in self.data]
            lst_random_type = random.choices(lst_type_card,
                                             weights=[14, 6, 1],
                                             k=self.deck_size)

            for card_type in lst_random_type:
                if card_type == "creature":
                    deck["creature"].append(self.create_creature(
                        random.choice(self.lst_creature)))
                elif card_type == "spell":
                    deck["spell"].append(self.create_spell(
                        random.choice(self.lst_spell)))
                else:
                    deck["artifact"].append(self.create_artifact(
                        random.choice(self.lst_artifact)))

        return (deck)

    def get_supported_types(self) -> dict:
        return {
            "creature": self.lst_creature,
            "spell": self.lst_spell,
            "artifact": self.lst_artifact
        }
