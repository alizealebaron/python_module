"""
Fichier : ft_data_stream.py
Auteur  : alebaron
Date    : 2026/01/08
"""


# +----------------------------------------------------------------+
# |                             Liste                              |
# +----------------------------------------------------------------+

def list_example(dic: dict) -> None:

    # === Parcours du dictionnaire ===

    high_score = [name for name, info in dic.items() if info['score'] > 2000]
    active_players = [name for name, info in dic.items() if info['active']]

    print(f"High scorers (>2000): {high_score}")
    print(f"Active players: {active_players}")


# +----------------------------------------------------------------+
# |                         Dictionnaire                           |
# +----------------------------------------------------------------+

def dict_example(dic: dict) -> None:

    # === Parcours du dictionnaire ===

    player_score = {name: info['score'] for (name, info) in dic.items()}
    nb_achievement = {name: len(info['achievement']) for (name, info) in dic.items()}

    print(f"Player scores: {player_score}")
    print(f"Achievement counts: {nb_achievement}")

# +----------------------------------------------------------------+
# |                              Set                               |
# +----------------------------------------------------------------+

def set_example(dic: dict) -> None:

    unique_player = set(name for name in dic)
    unique_achievement = set(success for value in dic.values() for success in value["achievement"])
    active_region = set(info["region"] for _, info in dic.items() if info["active"] is True)

    print(f"Unique players: {unique_player}")
    print(f"Unique achievements: {unique_achievement}")
    print(f"Active regions: {active_region}")


# +----------------------------------------------------------------+
# |                              All                               |
# +----------------------------------------------------------------+

def all_example(dic: dict) -> None:
    total_player = len(set(name for name in dic))
    total_succes = len(set(success for value in dic.values() for success in value["achievement"]))
    avg_score = sum(info['score'] for (_, info) in dic.items()) / total_player

    print(f"Total players: {total_player}")
    print(f"Total unique achievements: {total_succes}")
    print(f"Average score: {avg_score:.2f}")

# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    # === Initialisation des données ===

    player_data = {
        "Manu": {
            "score": 2300,
            "active": True,
            "achievement": {"Libération", "Béni", "Apprenti", "Âme de dragon"},
            "region": "north"
        },
        "Rémy": {
            "score": 800,
            "active": False,
            "achievement": {"Libération", "Béni"},
            "region": "south"
        },
        "Amélie": {
            "score": 5800,
            "active": True,
            "achievement": {"Libération", "Béni", "L'art de la Voix",
                            "Gardien", "Explorateur d'Oblivion",
                            "La chasse au dragon"},
            "region": "north"
        },
        "Romain": {
            "score": 2500,
            "active": False,
            "achievement": {"Libération", "Maître", "Gloire funèbre",
                            "Étranger", "Explorateur d'Oblivion"},
            "region": "central"
        },
        "Ana": {
            "score": 3200,
            "active": True,
            "achievement": {"Libération", "Voleur", "Au sommet d'Apocrypha",
                            "Légende", "Au-delà de la mort",
                            "Jugement d'un pair"},
            "region": "central"
        },
        "Noémie": {
            "score": 500,
            "active": True,
            "achievement": {"Libération"},
            "region": "central"
        }
    }

    print("=== List Comprehension Examples ===")

    list_example(player_data)

    print("\n=== Dict Comprehension Examples ===")

    dict_example(player_data)

    print("\n=== Set Comprehension Examples ===")

    set_example(player_data)

    print("\n=== Combined Analysis ===")

    all_example(player_data)