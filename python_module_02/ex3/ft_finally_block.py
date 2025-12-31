"""
Fichier : ft_finally_block.py
Auteur  : alebaron
Date    : 2025/12/31
"""


def water_plants(plant_list: list) -> None:
    """
    Waters each plant in the given list.
    Ensures cleanup using a finally block.
    """
    result = 1
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        result = 0
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")

    if result:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Tests the watering system with valid and invalid plant lists.
    """

    # Initialization
    list1 = ["Mangue", "Pêche", "Citron"]
    list2 = ["Courgette", None, "Olive"]

    # Test 1: Normal watering
    print("\nTesting normal watering...")
    water_plants(list1)

    # Test 2: Error during watering
    print("\nTesting with error...")
    water_plants(list2)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
