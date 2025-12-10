"""
Fichier : ft_plant_age.py
Auteur  : alebaron
Date    : 2025/12/10
"""


def ft_plant_age():
    day = input("Enter plant age in days: ")
    if (int(day) > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
