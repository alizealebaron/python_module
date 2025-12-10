"""
Fichier : ft_count_harvest_iterative.py
Auteur  : alebaron
Date    : 2025/12/10
"""


def ft_count_harvest_iterative():
    day = input("Days until harvest: ")
    for i in range(1, int(day) + 1):
        print(f"Day {i}")
    print("Harvest time!")
