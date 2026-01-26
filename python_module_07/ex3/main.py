# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 11:02:55 by alebaron        #+#    #+#               #
#  Updated: 2026/01/26 10:53:53 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .GameEngine import GameEngine
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory

if __name__ == "__main__":

    print("=== DataDeck Game Engine ===\n")

    # === Initialisation du deck de carte ===

    print("Configuring Fantasy Card Game...")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strat = AggressiveStrategy()
    engine.configure_engine(factory, strat)

    status = engine.get_engine_status()

    # === Affichage des paramètres de l'engine ===

    print(f"Factory: {status['factory']}")
    print(f"Strategy: {status['strategy']}")
    print(f"Available types: {factory.get_supported_types()}")

    # === Simulation d'un tour aggressif ===

    print("\nSimulating aggressive turn...")
    engine.simulate_turn()

    # === Rapport des tours joués ===

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")
