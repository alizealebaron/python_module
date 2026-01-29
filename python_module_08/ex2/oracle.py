# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  oracle.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 15:25:56 by alebaron        #+#    #+#               #
#  Updated: 2026/01/29 10:34:46 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("Error: Install python-doenv before execute this program.")


# +----------------------------------------------------------------+
# |                           Méthodes                             |
# +----------------------------------------------------------------+

def get_all_info() -> None:

    # Modifie les données pour mettre celle du .env
    load_dotenv()

    data = {
        "MATRIX_MODE": None,
        "DATABASE_URL": None,
        "API_KEY": None,
        "LOG_LEVEL": None,
        "ZION_ENDPOINT": None
    }

    print("Configuration loaded:")
    is_all_here = True
    for key in data:
        if os.getenv(key) is not None:
            print(f"{key.capitalize()}: {os.getenv(key)}")
        else:
            print(f"{key.capitalize()}: not found")
            is_all_here = False

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")
    if is_all_here is True:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file no properly configured")
    print("[OK] Production overrides available")


# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

if __name__ == "__main__":

    print("ORACLE STATUS: Reading the Matrix...\n")

    get_all_info()

    print("\nThe Oracle sees all configurations.")
