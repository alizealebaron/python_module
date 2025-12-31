"""
Fichier : ft_garden_management.py
Auteur  : alebaron
Date    : 2025/12/31
"""


# +----------------------------------------------------------------+
# |                         Errors Class                           |
# +----------------------------------------------------------------+

class GardenError(Exception):
    """Base exception for garden-related errors."""
    pass


class PlantError(GardenError):
    """Error related to plants."""
    pass


class WaterError(GardenError):
    """Error related to watering."""
    pass


# +----------------------------------------------------------------+
# |                        Garden Class                            |
# +----------------------------------------------------------------+

class Plant:
    # +------------------------------------------------------------+
    # |                        Constructor                         |
    # +------------------------------------------------------------+

    """init function"""
    def __init__(self, name: str, water: int, sun: int):
        self.__name = name
        self.__water = water
        self.__sun = sun

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Sun getter"""
    def get_sun(self) -> int:
        return self.__sun

    """Water getter"""
    def get_water(self) -> int:
        return self.__water

    """Name getter"""
    def get_name(self) -> str:
        return self.__name

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    """Function who convert plant to string"""
    def to_string(self):
        print(f"{self.__name}: healthy (water: {self.__water}, "
              f"sun: {self.__sun})")

    def water_plant(self):
        self.__water += 1


class GardenManager:
    # +------------------------------------------------------------+
    # |                        Constructor                         |
    # +------------------------------------------------------------+

    """init function"""
    def __init__(self):
        self.__lst_plant = [None] * 15
        self.__water_tank = 3
        self.__nb_plant = 0

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    """Function for adding a plant to our garden"""
    def add_plant(self, name: str, water: int, sun: int) -> None:
        try:
            if (name is None):
                raise PlantError("Plant name cannot be empty!")
                return
        except PlantError as error:
            print(f"Error adding plant: {error}")
        else:
            plant = Plant(name, water, sun)
            self.__lst_plant[self.__nb_plant] = plant
            self.__nb_plant += 1
            print(f"Added {name} successfully")

    """Function for watering all the plant"""
    def water_plants(self) -> None:
        result = 1
        print("Opening watering system")
        try:
            for i in range(0, self.__nb_plant):
                plant = self.__lst_plant[i]
                if (self.__water_tank == 0):
                    raise WaterError("Not enough water")
                else:
                    print(f"Watering {plant.get_name()}")
                    self.__water_tank -= 1
                    plant.water_plant()

        except WaterError as error:
            result = 0
            print(f"Error: Cannot water {plant.get_name()} - {error}")
        finally:
            print("Closing watering system (cleanup)")
        if result:
            print("Watering completed successfully!")

    """Check the plant health"""
    def check_plant_health(self) -> None:
        for i in range(0, self.__nb_plant):
            is_health = 1
            plant = self.__lst_plant[i]
            try:
                water_level = plant.get_water()
                sunlight_hours = plant.get_sun()
                if (water_level < 1):
                    raise WaterError(f"Water level {water_level} "
                                     f"is too low (min 1)")
                if (water_level > 10):
                    raise WaterError(f"Water level {water_level} "
                                     f"is too high (max 10)")
                if (sunlight_hours < 2):
                    raise PlantError(f"Sunlight hours {sunlight_hours} "
                                     f"is too low (min 2)")
                if (sunlight_hours > 12):
                    raise PlantError(f"Sunlight hours {sunlight_hours} "
                                     f"is too high (max 12)")
            except GardenError as error:
                is_health = 0
                print(f"Error checking {plant.get_name()}: {error}")

            if (is_health):
                plant.to_string()

    """Testing error recovery"""
    def error_recovery(self) -> None:
        is_error = False
        try:
            if (self.__water_tank < self.__nb_plant):
                raise GardenError("Not enough water in tank")
        except GardenError as error:
            is_error = True
            print(f"Caught {error.__class__.__name__}: {error}")
        else:
            print("Tank have enough water :D")
        finally:
            if is_error is True:
                print("System recovered and continuing...")
            else:
                print("System all good...")


# +----------------------------------------------------------------+
# |                            Main                                |
# +----------------------------------------------------------------+

def main() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager()

    # Test 1 : Ajout de plantes
    print("\nAdding plants to garden...")
    garden.add_plant("avocado", 5, 3)
    garden.add_plant("lettuce", 14, 3)
    garden.add_plant(None, 1, 3)

    # Test 2 : Arrosage des plantes
    print("\nWatering plants...")
    garden.water_plants()

    # Test 2 : Check les plantes
    print("\nChecking plant health...")
    garden.check_plant_health()

    # Test 3 : Check error recovery
    print("\nTesting error recovery...")
    garden.error_recovery()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
