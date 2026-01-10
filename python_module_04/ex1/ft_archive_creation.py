"""
Fichier : ft_archive_creation.py
Auteur  : alebaron
Date    : 2026/01/09
"""


if __name__ == "__main__":
	print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

	filename = "new_discovery.txt"
	text = (
        "[ENTRY 001] New species of duck discovered 🦆\n"
        "[ENTRY 002] This new species is named 'Mighty Duck' 🦆\n"
        "[ENTRY 003] Mighty Ducks have conquered the world 🦆\n"
        ""
    )

	try:
		# Initialisation du document
		print(f"Initializing new storage unit: {filename}")
		file =  open(filename, "w+", encoding='utf-8')
		print(f"Storage unit created successfully...\n")

		# Ecriture du text dans le document
		file.write(text)

		#Fermeture propre du fichier
		file.close()

		# Ouverture en mode lecture du fichier
		file = open(filename, "r")

		# Lecture du document pour vérifier les données inscrites
		print("Inscribing preservation data...")
		content = file.read()
		print(content)

		#Fermeture propre du fichier
		file.close()

		print("Data inscription complete. Storage unit sealed.")
		print(f"Archive '{filename}' ready for long-term preservation.")


	except:
		print(f"Error : The creation of the '{filename}' file was unsuccessful.")
		print("Data inscription incomplete.")
