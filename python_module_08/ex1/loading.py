# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  loading.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/28 11:28:34 by alebaron        #+#    #+#               #
#  Updated: 2026/01/28 15:08:58 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+


import importlib.util


# +----------------------------------------------------------------+
# |                           Méthodes                             |
# +----------------------------------------------------------------+

def check_dependency() -> bool:

    lst_package = ["pandas", "requests", "matplotlib"]
    is_okay = True

    for package in lst_package:
        
        # On essaie d'importer une à une les librairies
        try:
            name = importlib.util.find_spec(package)
            if name is None:
                print(f"[KO] {package} : Not installed.")
                is_okay = False 
            else:
                name = __import__(package)
                version = name.__version__
                print(f"[OK] {package} ({version}) - ", end="")
                if package == "pandas":
                    print("Data manipulation ready")
                elif package == "requests":
                    print("Network access ready")
                else:
                    print("Visualization ready")
        except (Exception, AttributeError):
            print(f"[KO] {package} : Not installed.")
            is_okay = False 

    return is_okay

def analyzing_data():
    import pandas
    import matplotlib.pyplot as plt
    
    print("Processing 1000 data points...")

    # On génère une matrice de données avec panda

    data = pandas.DataFrame([{'A': 3, 'B': 1, 'C': 4, 'D': 1},
                             {'A': 5, 'B': 9, 'C': 2, 'D': 6},
                             {'A': 5, 'B': 3, 'C': 5, 'D': 7}])
    print(data)
    print("Generating visualization...\n")

    # Puis on créer une image de celle-ci

    filename = "matrix_analysis.png"

    data.plot(kind='bar', title="Matrix Analysis Simulation")

    plt.xlabel("Index")
    plt.ylabel("Valeur")

    plt.savefig(filename)

    print("Analysis complete!")
    print(f"Result saved to: {filename}")

# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    result = check_dependency()

    if (result):
        print("\nAnalyzing Matrix data...")
        analyzing_data()
    else:
        print("\nImport failed. This program will stop.")
