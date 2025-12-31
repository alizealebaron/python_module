"""
Fichier : ft_different_errors.py
Auteur  : alebaron
Date    : 2025/12/17
"""


def garden_operations(n: int, div=None, file=None, key=None) -> None:
    """
    Performs several operations that may raise different types of errors.
    Used to demonstrate exception handling.
    """

    # Initialize variables
    dico = {'plant': 'Amaryllis', 'temperature': '20°C'}
    value = int(n)

    # Test 1: Division (may raise ZeroDivisionError)
    if div is not None:
        _ = value / div

    # Test 2: File opening (may raise FileNotFoundError)
    if file is not None:
        f = open(file, "r")
        f.close()

    # Test 3: Dictionary access (may raise KeyError)
    if key is not None:
        _ = dico[key]


def test_error_types():
    """
    Tests different Python error types using garden_operations.
    """

    # ===== Initialization =====
    print("=== Garden Error Types Demo ===")

    # Test 1: ValueError
    print("\nTesting ValueError...")
    try:
        garden_operations(n="Wiwiwi")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    else:
        print("No error detected!")

    # Test 2: ZeroDivisionError
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations(n=42, div=0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    else:
        print("No error detected!")

    # Test 3: FileNotFoundError
    print("\nTesting FileNotFoundError...")
    name = "Coin.txt"
    try:
        garden_operations(n=42, div=6, file=name)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{name}'")
    else:
        print("No error detected!")

    # Test 4: KeyError
    print("\nTesting KeyError...")
    word = "coin"
    try:
        garden_operations(n=42, div=6, key=word)
    except KeyError:
        print(f"Caught KeyError: 'missing\\{word}'")
    else:
        print("No error detected!")

    # Test 5: Multiple errors
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
