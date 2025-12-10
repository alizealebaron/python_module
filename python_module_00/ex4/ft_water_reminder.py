"""
Fichier : ft_water_reminder.py
Auteur  : alebaron
Date    : 2025/12/10
"""


def ft_water_reminder():
    day = input("Days since last watering: ")
    if (int(day) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
