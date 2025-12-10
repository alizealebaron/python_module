"""
Fichier : ft_harvest_total.py
Auteur  : alebaron
Date    : 2025/12/10
"""


def ft_harvest_total():
    day1 = input("Day 1 harvest:")
    day2 = input("Day 2 harvest:")
    day3 = input("Day 3 harvest:")
    area = int(day1) + int(day2) + int(day3)
    print(f"Total harvest: {area}")
