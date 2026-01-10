"""
Fichier :  ft_crisis_response.py
Auteur  : alebaron
Date    : 2026/01/10
"""


def access_archive(nom_fichier: str) -> None:

    # Tentative de l'ouverture du fichier
    try:
        with open(nom_fichier, "r") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{nom_fichier}'...")
            print(f"SUCCESS: Archive recovered - '{file.read()}'")
            print(f"STATUS: Normal operations resumed")
    except FileNotFoundError:
        alert_message(nom_fichier, "Archive not found in storage matrix")
    except PermissionError:
        alert_message(nom_fichier, "Security protocols deny access")
    except IsADirectoryError:
        alert_message(nom_fichier, "Cannot open a folder")


def alert_message(nom: str, text: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{nom}'...")
    print(f"RESPONSE: {text}")
    print(f"STATUS: Crisis handled, system stable")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    # === Test 1 : Fichier inexistant ===
    access_archive("lost_archive.txt")
    print("") # Saut de ligne

    # === Test 2 : Permission refusée ===
    access_archive("classified_vault.txt")
    print("") # Saut de ligne

    # === Test 3 : Accéder à un dossier ===
    access_archive("folder")
    print("") # Saut de ligne

    # === Test 4 : Fichier valide ===
    access_archive("standard_archive.txt")
    print("") # Saut de ligne
