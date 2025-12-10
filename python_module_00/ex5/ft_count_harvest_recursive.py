"""
Fichier : ft_count_harvest_recursive.py
Auteur  : alebaron
Date    : 2025/12/10
"""


def ft_count_harvest_recursive(quack=-1):
    if (quack == -1):
        day = input("Days until harvest: ")
    else:
        day = quack
    if (int(day) > 0):
        ft_count_harvest_recursive(int(day) - 1)
        print(f"Day {day}")
    if (quack == -1):
        print("Harvest time!")
