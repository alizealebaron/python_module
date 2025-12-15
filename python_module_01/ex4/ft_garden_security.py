"""
Fichier : ft_garden_security.py
Auteur  : alebaron
Date    : 2025/12/12
"""


class SecurePlant:

    # +------------------------------------------------------------+
    # |                         Controller                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name: str, height: int, age: int):
        if (self.check_params(height, age)):
            self.__name = name
            self.__height = height
            self.__age = age
            print(f"Plant created: {self.__name}")

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

    """Object to string function"""
    def to_string(self):
        print(f"{self.__name} ({self.__height}cm, {self.__age} age)")

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


print("=== Garden Security System ===")
plant = SecurePlant("Amaryllis", 16, 56)

plant.set_height(25)
plant.set_age(30)

print("")

plant.set_height(-25)

print("\nCurrent plant:", end=" ")
plant.to_string()
