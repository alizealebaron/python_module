"""
Fichier : ft_stream_management.py
Auteur  : alebaron
Date    : 2026/01/09
"""


import sys


if __name__ == "__main__":
	print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

	# Récupération des variables sur l'entrée standart
	arch_id = input("Input Stream active. Enter archivist ID: ")
	sys_nom = input("Input Stream active. Enter status report: ")

	try:
		# Affichage sur la sortie standart et la sortie erreur
		sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {sys_nom}\n")
		sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
		sys.stdout.write("[STANDARD] Data transmission complete\n")

		print("\nThree-channel communication test successful.")
	except:
		print("\nError : Three-channel communication test unsuccessful.")
