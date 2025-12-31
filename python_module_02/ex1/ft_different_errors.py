"""
Fichier : ft_different_errors.py
Auteur  : alebaron
Date    : 2025/12/17
"""

"""
Fonction de vérification des paramètres
"""
def garden_operations(n: int, div=None, file=None, key=None) -> None:
    # Initialisation of usefull variables

    dico = {'plant': 'Amaryllis', 'temperature': '20°C'}
    value = int(n)

	# Test who will trigger an error (maybe)

	# Test 1 : Division
    if (div != None):
        useless1 = value / div
	
	# Test 2 : Open file
    if (file != None):
        useless2 = open(file, "r")
        useless2.close()
	
    # Test 3 : Dictionnary 
    if (key != None):
        useless3 = dico[key]

"""
Fonction de test
"""
def test_error_types():

    # ====== Begin & Initialisation ======

    print("=== Garden Error Types Demo ===")

    # === Test 1 : Division error ===

    print("\nTesting ValueError...")

    try:
        garden_operations(n="Wiwiwi")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    else:
        print("No error detected!")

    # === Test 2 : Zero Division Error ===
	
    print("\nTesting ZeroDivisionError...")

    try:
        garden_operations(n=42, div=0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    else:
        print("No error detected!")

    # === Test 3 : File error ===

    print("\nTesting FileNotFoundError...")

    name = "Coin.txt"
    try:
        garden_operations(n=42, div=6, file=name)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{name}'")
    else:
        print("No error detected!")

    # === Test 4 : Key error ===

    print("\nTesting KeyError...")

    word = "coin"
    try:
        garden_operations(n=42, div=6, key=word)
    except KeyError:
        print(f"Caught KeyError: 'missing\\{word}'")
    else:
        print("No error detected!")

    # === Test 5 : Multiple error ===

    print("\nTesting multiple errors together...")

    try:
        garden_operations(n=42, div=0, key=word)
    except (ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")
    else:
        print("No error detected!")

    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()