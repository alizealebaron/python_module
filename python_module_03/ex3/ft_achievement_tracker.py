"""
Fichier : ft_score_analytics.py
Auteur  : alebaron
Date    : 2026/01/05
"""


if __name__ == "__main__":
    # === Initialisation des Achievement ===

    achievement = ["Taking Inventory",
                   "Getting Wood",
                   "Getting Wood",
                   "Benchmaking",
                   "Time to Mine!",
                   "Hot Topic",
                   "Acquire Hardware",
                   "The Lie",
                   "Awarded All Trophies",
                   "Music to my Ears",
                   "Super Sonic",
                   "Bee our guest"]

    # === Attribution des achievements ===

    remy_achievement = [achievement[0], achievement[1], achievement[6],
                        achievement[7], achievement[10]]
    noem_achievement = [achievement[0], achievement[1], achievement[3],
                        achievement[4]]
    coin_achievement = [achievement[0], achievement[1], achievement[3],
                        achievement[11], achievement[10]]

    set_remy = set(remy_achievement)
    set_noem = set(noem_achievement)
    set_coin = set(coin_achievement)

    # === Mise en route du programme ===

    print("=== Achievement Tracker System ===\n")

    # Affichage des achievements

    print(f"Player Rémy achievements: {set_remy}")
    print(f"Player Noémie achievements: {set_noem}")
    print(f"Player Coin coin achievements: {set_coin}")

    # Affichage de la partie analyse

    print("\n=== Achievement Analytics ===")

    set_achievement = set(achievement)

    # Afficher tous les achievements

    print(f"All unique achievements: {set_achievement}")
    print(f"Total unique achievements: {len(set_achievement)}\n")

    # Afficher les succès communs

    common_succes = set_coin & set_remy & set_noem
    common_succes = set_coin.intersection(set_noem, set_remy)

    print(f"Common to all players: {common_succes}")

    # Afficher les succès rare (1 seule personne)

    remy_unique = set_remy - set_noem - set_coin
    noem_unique = set_noem - set_remy - set_coin
    coin_unique = set_coin - set_remy - set_noem

    remy_unique = set_remy.difference(set_coin.union(set_noem))
    noem_unique = set_noem.difference(set_coin.union(set_remy))
    coin_unique = set_coin.difference(set_remy.union(set_noem))

    rare_succes = remy_unique | noem_unique | coin_unique

    print(f"Rare achievements (1 player): {rare_succes}\n")

    # Rémy VS Noémie

    common_fight = set_remy & set_noem

    print(f"Noémie vs Rémy common: {common_fight}")
    print(f"Noémie unique: {noem_unique}")
    print(f"Rémy unique: {remy_unique}")
