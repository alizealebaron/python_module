"""
Fichier : ft_plant_factory.py
Auteur  : alebaron
Date    : 2025/12/12
"""


class Plant:
    def __init__(self, plant, height, days):
        self.plant = plant
        self.height = height
        self.days = days

    def to_string(self):
        print(f"{self.plant} ({self.height}cm, {self.days} days)")


tab_plant = [
    ("Amaryllis", 12, 45),
    ("Coquelicot", 4, 21),
    ("Rose", 78, 12),
    ("Tulipe", 45, 95),
    ("Paquerette", 6, 4)
]

nb_plant = 0

print("=== Plant Factory Output ===")
for element in tab_plant:
    plant = Plant(element[0], element[1], element[2])
    print("Created:", end=" ")
    plant.to_string()
    nb_plant += 1
print(f"\nTotal plants created: {nb_plant}")
