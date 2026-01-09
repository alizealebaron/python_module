"""
Fichier : ft_data_stream.py
Auteur  : alebaron
Date    : 2026/01/09
"""

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    filename = "ancient_fragment.txt"

    try:
        # Tentative de récupération du fichier
        print(f"Accessing Storage Vault: {filename}")
        file = open(filename, "r", encoding='utf-8')

        # Lecture du contenu du fichier
        print("Connection established...\n")
        content = file.read()

        # Affichage du contenu du fichier
        print("RECOVERED DATA:")
        print(content)

        # Fermeture du fichier
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("Error: File 'ancient_fragment.txt' not found.")
        print("\nData recovery incomplete. Storage unit disconnected.")
