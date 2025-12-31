"""
Fichier : ft_plant_types.py
Auteur  : alebaron
Date    : 2025/12/15
"""


# +----------------------------------------------------------------+
# |                            Classes                             |
# +----------------------------------------------------------------+

class Plant:

    # +------------------------------------------------------------+
    # |                         Controller                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name: str, height: int, age: int):
        if (self.check_params(height, age)):
            self.__name = name
            self.__height = height
            self.__age = age

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Height getter"""
    def get_height(self):
        return self.__height

    """Age getter"""
    def get_age(self):
        return self.__age

    """Name getter"""
    def get_name(self):
        return self.__name

    # +------------------------------------------------------------+
    # |                          Setters                           |
    # +------------------------------------------------------------+

    """Height setter"""
    def set_height(self, height: int):
        if (self.check_params(height, self.get_age())):
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    """Age setter"""
    def set_age(self, age: int):
        if (self.check_params(self.get_height(), age)):
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    """Name setter"""
    def set_name(self, name: str):
        self.__name == name

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    """Check parameters"""
    def check_params(self, height: int, age: int):
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return 0
        if (age < 0):
            print(f"Invalid operation attempted: age {age} age [REJECTED]")
            print("Security: Negative age rejected")
            return 0
        return 1


class Tree(Plant):

    # +------------------------------------------------------------+
    # |                         Controller                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Trunk_diameter getter"""
    def get_trunk_diameter(self):
        return self.__trunk_diameter

    # +------------------------------------------------------------+
    # |                          Setters                           |
    # +------------------------------------------------------------+

    """Trunk_diameter setter"""
    def set_trunk_diameter(self, trunk_diameter: int):
        self.__trunk_diameter = trunk_diameter
        print(f"Trunk_diameter updated: {trunk_diameter}cm [OK]")

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    """Object to string function"""
    def to_string(self):
        print(f"{self.get_name()} (Tree): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.__trunk_diameter}cm diameter")

    def produce_shade(self):
        radius = self.get_height() / 100
        area = 3.14 * (radius ** 2)
        print(f"{self.get_name()} provides {int(area)} "
              f"square meters of shade")


class Flower(Plant):

    # +------------------------------------------------------------+
    # |                         Controller                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.__color = color

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Color getter"""
    def get_color(self):
        return self.__color

    # +------------------------------------------------------------+
    # |                          Setters                           |
    # +------------------------------------------------------------+

    """Color setter"""
    def set_color(self, color: str):
        self.__color = color
        print(f"Color updated: {color} [OK]")

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    """Object to string function"""
    def to_string(self):
        print(f"{self.get_name()} (Flower): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.__color} color")

    def bloom(self):
        print(f"{self.get_name()} is blooming beautifully!")


class Vegetable(Plant):

    # +------------------------------------------------------------+
    # |                         Controller                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self.__harvest_season = harvest_season
        self.__nutritional_value = nutritional_value

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Harvest_season getter"""
    def get_harvest_season(self):
        return self.__harvest_season

    """Nutritional_value getter"""
    def get_nutritional_value(self):
        return self.__nutritional_value

    # +------------------------------------------------------------+
    # |                          Setters                           |
    # +------------------------------------------------------------+

    """Harvest_season setter"""
    def set_harvest_season(self, harvest_season: str):
        self.__harvest_season = harvest_season
        print(f"Harvest_season updated: {harvest_season} [OK]")

    """Nutritional_value  setter"""
    def set_nutritional_value(self, nutritional_value: str):
        self.__nutritional_value = nutritional_value
        print(f"Nutritional_value  updated: {nutritional_value} [OK]")

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    """Object to string function"""
    def to_string(self):
        print(f"{self.get_name()} (Vegetable): {self.get_height()}cm, "
              f"{self.get_age()} days, {self.__harvest_season} harvest")
        print(f"{self.get_name()} is rich in {self.__nutritional_value}")


# +----------------------------------------------------------------+
# |                              Main                              |
# +----------------------------------------------------------------+

print("=== Garden Plant Types ===\n")

tree = Tree("Oak", 500, 1825, 50)
flower = Flower("Rose", 25, 30, "red")
vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

flower.to_string()
flower.bloom()

print("")

tree.to_string()
tree.produce_shade()

print("")

vegetable.to_string()
