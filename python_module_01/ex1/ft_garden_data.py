"""
Fichier : ft_garden_data.py
Auteur  : alebaron
Date    : 2025/12/12
"""


class Plant:
    def __init__(self, plant, height, days):
        self.plant = plant
        self.height = height
        self.days = days

    def to_string(self):
        print(f"{self.plant}: {self.height}cm, {self.days} days old")


def main():
    plant1 = Plant("Amaryllis", 35, 89)
    plant2 = Plant("Coquelicot", 41, 10)
    plant3 = Plant("Rose", 30, 17)
    print("=== Garden Plant Registry ===")
    plant1.to_string()
    plant2.to_string()
    plant3.to_string()


main()
