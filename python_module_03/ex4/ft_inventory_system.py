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

def transaction_inventaire(inv: dict, objet: str, quantite: int,
                           donneur: str, receveur: str) -> dict:
    """Permet d'effectuer une transaction d'une quantité d'objet d'un jouer à un autre"""
    quantite_inv = inv[donneur].get(objet).get("quantité")

    # Vérification de la présence de l'objet dans l'inventaire
    if inv[donneur].get(objet) is None:
        print(f"Erreur : L'objet {objet} n'existe pas dans l'inventaire de {donneur}")
    elif quantite_inv < quantite:
        print(f"Erreur : Il n'y a pas assez de {objet}.")
    else:
        print(f"\n=== Transaction: {donneur} gives {receveur} {quantite} {objet} ===")
        inv[donneur].get(objet)["quantité"] -= quantite
        inv[receveur].get(objet)["quantité"] += quantite
        print("Transaction successful!\n")
        print("=== Updated Inventories ===")
        quantite_don = inv[donneur].get(objet).get("quantité")
        quantite_rec = inv[receveur].get(objet).get("quantité")
        print(f"{donneur} {objet}: {quantite_don}")
        print(f"{receveur} {objet}: {quantite_rec}")
        return inv

def analyse_inventaire(inv: dict):
    """Affiche une analyse des inventaires des joueurs"""
    print(f"\n=== Inventory Analytics ===")

    if inv is None:
        print("Il n'y a pas encore de joueur.")
        return None

    max_money = {
        "propriétaire": None,
        "quantité": 0
    }
    max_items = {
        "propriétaire": None,
        "quantité": 0
    }
    rarete_list = []

    for player, objet in inv.items():
        count_items = 0
        count_money = 0
        for name, items in objet.items():
            count_items += 1
            count_money += items.get("prix") * items.get("quantité")
            if items.get('rareté') == "rare":
                rarete_list.append(name)

        if count_money > max_money.get("quantité"):
            max_money["quantité"] = count_money
            max_money["propriétaire"] = player
        if count_items > max_items.get("quantité"):
            max_items["quantité"] = count_items
            max_items["propriétaire"] = player
    
    print(f"Most valuable player: {max_money.get('propriétaire')} ({max_money.get('quantité')} P)")
    print(f"Most items: {max_items.get('propriétaire')} ({max_items.get('quantité')} item(s))")
    print(f"Rarest items : {rarete_list}")

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
                "quantité": 10
            },
        }
    }

    print("=== Player Inventory System ===\n")

    # === Affichage d'un inventaire ===

    afficher_inventaire(player_inventaire, "Manu")

    # Transaction d'un inventaire à un autre

    player_inventaire = transaction_inventaire(player_inventaire, "Pokeball",
                                               5, "Amélie", "Manu")

    # Afficher total inventaire

    analyse_inventaire(player_inventaire)
