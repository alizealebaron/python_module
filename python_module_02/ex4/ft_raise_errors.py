"""
Fichier : ft_raise_errors.py
Auteur  : alebaron
Date    : 2025/12/31
"""


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Check the plant health"""
    is_health = 1

    try:
        if (plant_name is None):
            raise ValueError("Plant name cannot be empty!")
        if (water_level < 1):
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if (water_level > 10):
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if (sunlight_hours < 2):
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        if (sunlight_hours > 12):
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
    except ValueError as error:
        is_health = 0
        print(f"Error: {error}")

    if (is_health):
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:

    # Test 1 : Bonne valeurs
    print("\nTesting good values...")
    check_plant_health("avocado plant", 3, 5)

    # Test 2 : Nom vide
    print("\nTesting empty plant name...")
    check_plant_health(None, 3, 5)

    # Test 3 : Mauvais niveau d'eau
    print("\nTesting bad water level...")
    check_plant_health("avocado plant", 15, 5)

    # Test 4 : Mauvais niveau d'ensoleillement
    print("\nTesting bad sunlight hours...")
    check_plant_health("avocado plant", 5, 1)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
    print("\nAll error raising tests completed!")
