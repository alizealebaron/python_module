"""
Fichier : ft_custom_errors.py
Auteur  : alebaron
Date    : 2025/12/17
"""


# +----------------------------------------------------------------+
# |                            Classes                             |
# +----------------------------------------------------------------+

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


# +----------------------------------------------------------------+
# |                             Test                               |
# +----------------------------------------------------------------+

def test_error():
    # ====== Begin & Initialisation ======

    print("=== Custom Garden Errors Demo ===")

    # === Test 1 : Plant error ===

    print("\nTesting PlantError...")

    status = "wilting"

    try:
        if (status == "wilting"):
            raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError : {error}")
    else:
        print(f"Tomato plant is {status}, seem's fine.")

    # === Test 2 : Water error ===

    print("\nTesting WaterError...")

    watering_tank = 4

    try:
        if (watering_tank < 20):
            raise PlantError("Not enough water in the tank!")
    except PlantError as error:
        print(f"Caught WaterError : {error}")
    else:
        print(f"Water tank have {watering_tank}L of water, seem's enough.")

    # === Test 3 : All error ===

    print("\nTesting catching all garden errors...")

    try:
        if (status == "wilting"):
            raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught a garden error : {error}")
    else:
        print(f"Tomato plant is {status}, seem's fine.")

    try:
        if (watering_tank < 20):
            raise PlantError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught a garden error : {error}")
    else:
        print(f"Water tank have {watering_tank}L of water, seem's enough.")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error()
