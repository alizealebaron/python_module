"""
Fichier : ft_plant_growth.py
Auteur  : alebaron
Date    : 2025/12/12
"""


class Plant:
    def __init__(self, plant, height, days):
        self.plant = plant
        self.height = height
        self.days = days

    def get_info(self):
        print(f"{self.plant}: {self.height}cm, {self.days} days old")

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1


def main():
    days = 1
    plant1 = Plant("Amaryllis", 25, 30)
    height = plant1.height
    print(f"=== Day {days} ===")
    plant1.get_info()
    for days in range(2, 8):
        plant1.age()
        plant1.grow()
    print(f"=== Day {days} ===")
    plant1.get_info()
    height = plant1.height - height
    print(f"Growth this week: +{height}cm")


main()
