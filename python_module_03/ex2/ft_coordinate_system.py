"""
Fichier : ft_score_analytics.py
Auteur  : alebaron
Date    : 2026/01/01
"""


import math


def create_coord(coord: str) -> tuple:
    """Get a string and parse it for return a tuple"""

    try:
        new_coord = tuple(int(x) for x in coord.split(","))
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{coord}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None

    print(f"Parsing coordinates: {coord}")
    print(f"Parsed position: {new_coord}")

    return new_coord


def main():
    """Main function of the program"""
    # === Testing with some coordinates ===

    coord_spawn = (0, 0, 0)
    coord_test = (5, 18, 3)

    x1, y1, z1 = coord_spawn
    x2, y2, z2 = coord_test

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

    print(f"Position created: ({x2}, {y2}, {z2})")
    print(f"Distance between {coord_spawn} and {coord_test}: {distance:.2f}\n")

    # === Parsing some coordinates ===

    coord_pars = create_coord("3,4,0")

    x3, y3, z3 = coord_pars
    distance = math.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2)
    print(f"Distance between {coord_spawn} and {coord_pars}: {distance:.2f}\n")

    # === Parsing wrong coordinates ===

    create_coord("abc,def,ghi")

    # === Unpacking coordinates ===

    print("\nUnpacking demonstration:")
    print(f"Player at x={x3}, y={y3}, z={z3}")
    print(f"Coordinates at X={x3}, Y={y3}, Z={z3}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    main()
