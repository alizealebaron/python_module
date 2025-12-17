"""
Fichier : ft_first_exception.py
Auteur  : alebaron
Date    : 2025/12/17
"""


def check_temperature(temp_str : str):
    try:
        int(temp_str)
    except:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        temp = int(temp_str)
        if (temp > 40):
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif (temp < 0):
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")

def test_temperature_input():
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")

# test_temperature_input()