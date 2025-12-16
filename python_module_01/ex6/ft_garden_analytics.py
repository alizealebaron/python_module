"""
Fichier : ft_garden_analytics.py
Auteur  : alebaron
Date    : 2025/12/15
"""


# +----------------------------------------------------------------+
# |                            Classes                             |
# +----------------------------------------------------------------+

class Plant:

    # +------------------------------------------------------------+
    # |                        Constructor                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name: str, height: int):
        self.__name = name
        if (self.check_params(height)):
            self.__height = height
        else:
            self.__height = 0

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Height getter"""
    def get_height(self):
        return self.__height

    """Name getter"""
    def get_name(self):
        return self.__name

    # +------------------------------------------------------------+
    # |                          Setters                           |
    # +------------------------------------------------------------+

    """Height setter"""
    def set_height(self, height: int):
        if (self.check_params(height)):
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    """Name setter"""
    def set_name(self, name: str):
        self.__name == name

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    """Check parameters"""
    def check_params(self, height: int):
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return 0
        return 1

    def grow(self):
        self.__height += 1

    def to_string(self):
        print(f"{self.__name}: {self.__height}cm")


class FloweringPlant(Plant):

    # +------------------------------------------------------------+
    # |                        Constructor                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name: str, height: int, bloom: bool, color: str):
        super().__init__(name, height)
        self.__bloom = bloom
        self.__color = color

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Color getter"""
    def get_color(self):
        return self.__color

    """Bloom getter"""
    def get_bloom(self):
        return self.__bloom

    # +------------------------------------------------------------+
    # |                          Setters                           |
    # +------------------------------------------------------------+

    """Color setter"""
    def set_color(self, color: str):
        self.__color == color

    """Bloom setter"""
    def set_bloom(self, bloom: bool):
        self.__bloom == bloom

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    def to_string(self):
        if (self.__bloom):
            print(f"{self.get_name()}: {self.get_height()}cm, "
                  f"{self.__color} flowers (blooming)")
        else:
            print(f"{self.set_name()}: {self.get_height()}cm, "
                  f"{self.__color} flowers")


class PrizeFlower(FloweringPlant):

    # +------------------------------------------------------------+
    # |                        Constructor                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name: str, height: int, bloom: bool, color: str, prize: int):
        super().__init__(name, height, bloom, color)
        if (prize >= 0):
            self.__prize = prize
        else:
            self.__prize = 0

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Prize getter"""
    def get_prize(self):
        return self.__prize

    # +------------------------------------------------------------+
    # |                          Setters                           |
    # +------------------------------------------------------------+

    """Prize setter"""
    def set_color(self, prize: int):
        if (prize >= 0):
            self.__prize = prize
            print(f"Prize updated: {prize}cm [OK]")
        else:
            print(f"Invalid operation attempted: prize {prize} [REJECTED]")
            print("Security: Negative prize rejected")

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    def to_string(self):
        if (self.get_bloom()):
            print(f"{self.get_name()}: {self.get_height()}cm, "
                  f"{self.get_color()} flowers (blooming), "
                  f"Prize points: {self.__prize}")
        else:
            print(f"{self.get_name()}: {self.get_height()}cm, "
                  f"{self.get_color()} flowers, "
                  f"Prize points: {self.__prize}")
            
class Garden:

    # +------------------------------------------------------------+
    # |                        Constructor                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self, name : str):
        self.__name = name
        self.__tab_plants = [None] * 100
        self.__nb_plant = 0
        self.__total = 0
        self.__nb_plants = 0
        self.__nb_flower = 0
        self.__nb_flowerprize = 0

    # +------------------------------------------------------------+
    # |                          Getters                           |
    # +------------------------------------------------------------+

    """Name getter"""
    def get_name(self):
        return self.__name

    def get_nb_plant(self):
        return self.__nb_plant
    
    def get_nb_plants(self):
        return self.__nb_plants
    
    def get_nb_flower(self):
        return self.__nb_flower
    
    def get_nb_flowerprize(self):
        return self.__nb_flowerprize
    
    # +------------------------------------------------------------+
    # |                   Gestion of the Garden                    |
    # +------------------------------------------------------------+

    def add_plant(self, plant: Plant):
        self.__tab_plants[self.__nb_plant] = plant
        self.__nb_plant += 1
        print(f"Added {plant.get_name()} to {self.__name}'s garden")
        if (plant.__class__.__name__ == "Plant"):
            self.__nb_plants += 1
        if (plant.__class__.__name__ == "FloweringPlant"):
            self.__nb_flower += 1
        if (plant.__class__.__name__ == "PrizeFlower"):
            self.__nb_flowerprize += 1
    
    def water_plant(self):
        print(f"{self.__name} is helping all plants grow...")
        for i in range (0, self.__nb_plant):
            self.__tab_plants[i].grow()
            self.__total += 1
            print(f"{self.__tab_plants[i].get_name()} grew 1cm")
    
    def calcul_score(self):
        score = 0
        for i in range (0, self.__nb_plant):
            score += self.__tab_plants[i].get_height()
            class_name = self.__tab_plants[i].__class__.__name__
            if (class_name == "PrizeFlower"):
                score += self.__tab_plants[i].get_prize()
            if (class_name == "FloweringPlant" or class_name
                == "PrizeFlower"):
                    if (self.__tab_plants[i].get_bloom()):
                        score += 15
        return score

    def test_height(self):
        for i in range (0, self.__nb_plant):
            if (self.__tab_plants[i].get_height() < 0):
                return 0
        return 1

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    def to_string(self):
        print(f"=== {self.__name}'s Garden Report ===")
        print("Plants in garden:")

        for i in range (0, self.__nb_plant):
            print("- ", end="")
            self.__tab_plants[i].to_string()

        print(f"\nPlants added: {self.__nb_plant}, "
              f"Total growth: {self.__total}cm")

        print(f"Plant types: {self.__nb_plants} regular, "
              f"{self.__nb_flower} flowering, "
              f"{self.__nb_flowerprize} prize flowers")

class GardenStats:
    # +--------------------------------------------------------+
    # |                      Constructor                       |
    # +--------------------------------------------------------+

    """Constructor function"""
    def __init__(self):
        self.nb_plant = 0
        self.nb_flower = 0
        self.nb_flowerprize = 0     
        
class GardenManager:

    # +------------------------------------------------------------+
    # |                        Constructor                         |
    # +------------------------------------------------------------+

    """Constructor function"""
    def __init__(self):
        self.tab_garden = [None] * 10
        self.nb_garden = 0
        self.stats = GardenStats()

    # +------------------------------------------------------------+
    # |                          Others                            |
    # +------------------------------------------------------------+

    def test_height(self):
        for i in range (0, self.nb_garden):
            if (self.tab_garden[i].test_height() == 0):
                print("Height validation test: False")
                return 0;
        print("Height validation test: True")

    def to_string(self):
        print("Garden scores - ", end="")
        for i in range (0, self.nb_garden):
            print(f"{self.tab_garden[i].get_name()}: "
                  f"{self.tab_garden[i].calcul_score()}", end= "")
            if (i != (self.nb_garden - 1)):
                print(",", end= " ")
            else:
                print(".")
        print(f"Total gardens managed: {self.nb_garden}")

    def add_garden(self, garden: Garden):
        self.tab_garden[self.nb_garden] = garden
        self.nb_garden += 1

    def get_stats(self):
        self.stats.nb_flower = 0
        self.stats.nb_plant = 0
        self.stats.nb_flowerprize = 0
        for i in range (0, self.nb_garden):
            garden = self.tab_garden[i]
            self.stats.nb_flower += garden.get_nb_flower()
            self.stats.nb_flowerprize += garden.get_nb_flowerprize()
            self.stats.nb_plant += garden.get_nb_plants()

# +----------------------------------------------------------------+
# |                              Main                              |
# +----------------------------------------------------------------+

print("=== Garden Management System Demo ===\n")

network = GardenManager()

garden1 = Garden("Summer")
garden2 = Garden("Stella")

network.add_garden(garden1)
network.add_garden(garden2)

plant1 = Plant("Oak tree", 100)
plant2 = FloweringPlant("Amaryllis", 25, True, "blanche")
plant3 = PrizeFlower("Tournesol", 50, True, "jone", 10)
plant4 = Plant("Rose", 15)

garden1.add_plant(plant1)
garden1.add_plant(plant2)
garden1.add_plant(plant3)

garden2.add_plant(plant4)

print("")

garden1.water_plant()

print("")

garden1.to_string()

print("")

network.to_string()
