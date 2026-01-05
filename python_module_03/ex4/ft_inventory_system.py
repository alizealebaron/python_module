"""
Fichier : ft_score_analytics.py
Auteur  : alebaron
Date    : 2026/01/05
"""

def afficher_inventaire(inv: dict, nom: str):
    """Permet d'afficher l'inventaire d'un joueur précis"""

    # Récupération des données du joueur s'il existe

    data = inv[nom];

    if data is None:
        print(f"Erreur: Le joueur {nom} n'existe pas.")
        return None;

    print(f"=== {nom}'s Inventory ===")

    # Affichage de l'inventaire

    inv_total = 0
    inv_nb_item = 0
    ens_categ = {}

    for key, value in data.items():

        # Récupération des données
        item_type = value.get("type")
        item_rarete = value.get("rareté")
        item_prix = value.get("prix")
        item_quantite = value.get("quantité")
        item_total = item_prix * item_quantite

        # Affichage
        print(f"{key} ({item_type}, {item_rarete}): "
              f"{item_quantite}x @ {item_prix} P each = {item_total} P")
        
        # Mise à jour des informations
        inv_total += item_total
        inv_nb_item += 1

        # Calcul des catégories
        if item_type not in ens_categ:
            ens_categ[item_type] = item_quantite
        else:
            ens_categ[item_type] += item_quantite


    print(f"\nInventory value: {inv_total} P")
    print(f"Item count: {inv_nb_item} items")
    print("Categories: " +", ".join(f"{categorie}({value})" for categorie, value in ens_categ.items()))


if __name__ == "__main__":

    # === Initialisation des dictionnaires ===

    player_inventaire = {
        "Manu": {
            "Potion": {
                "type" : "soin",
                "rareté": "common",
                "prix": 300,
                "quantité": 2
            },
            "Pierre plante": {
                "type" : "pierre",
                "rareté": "uncommon",
                "prix": 500,
                "quantité": 1
            },
            "Pokeball": {
                "type" : "ball",
                "rareté": "common",
                "prix": 200,
                "quantité": 15
            }
        },
        "Amélie": {
            "Pierre feu": {
                "type" : "pierre",
                "rareté": "uncommon",
                "prix": 500,
                "quantité": 2
            },
            "Multi Exp.": {
                "type" : "objet",
                "rareté": "rare",
                "prix": 5000,
                "quantité": 1
            },
            "Superball": {
                "type" : "ball",
                "rareté": "uncommon",
                "prix": 600,
                "quantité": 10
            },
            "Pokeball": {
                "type" : "ball",
                "rareté": "uncommon",
                "prix": 200,
                "quantité": 5
            },
        }
    }

    print("=== Player Inventory System ===\n")

    # === Affichage d'un inventaire ===

    afficher_inventaire(player_inventaire, "Manu")


