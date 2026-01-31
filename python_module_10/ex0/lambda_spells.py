# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/31 11:34:11 by alebaron        #+#    #+#               #
#  Updated: 2026/01/31 14:30:24 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+



# +----------------------------------------------------------------+
# |                          Méthodes                              |
# +----------------------------------------------------------------+

def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:

    min_power = min(mages, key=lambda mage: mage["power"])
    max_power = max(mages, key=lambda mage: mage["power"])
    avg_power = round(sum(map(lambda x: x['power'], mages)) / 
                      len(mages), 2)
    
    return {
        "max_power": max_power["power"],
        "min_power": min_power["power"],
        "avg_power": avg_power
    }


# +----------------------------------------------------------------+
# |                            Main                                |
# +----------------------------------------------------------------+

if __name__ == "__main__":

    print("=========== Test : artifact_sorter ===========\n")

    art1 = {"name": "Griseous Orb", "power": 5, "type": "orb"}
    art2 = {"name": "Adamant Crystal", "power": 7, "type": "crystal"}
    art3 = {"name": "Lustrous Globe", "power": 2, "type": "globe"}

    lst_artifact = [art1, art2, art3]

    print(f"Artifact list before sort :\n{lst_artifact}")

    lst_artifact = artifact_sorter(lst_artifact)

    print(f"Artifact list after sort :\n{lst_artifact}")

    print("\n=========== Test : power_filter ===========\n")

    mage1 = {"name": "Tara Duncan", "power": 100, "element": "all"}
    mage2 = {"name": "Percy Jackson", "power": 70, "element": "water"}
    mage3 = {"name": "Luz", "power": 60, "element": "ice light grass fire"}

    lst_mage = [mage1, mage2, mage3]

    print(f"Mage list before filter :\n{lst_mage}")

    lst_mage = power_filter(lst_mage, 65)
    
    print(f"Mage list before filter :\n{lst_mage}")

    print("\n=========== Test : spell_transformer ===========\n")

    lst_spell = ["Enormibus", "Piège nocif", "Tir toxique"]

    print(f"Spell list before map :\n{lst_spell}")

    lst_spell = spell_transformer(lst_spell)
    
    print(f"Spell list before map :\n{lst_spell}")

    print("\n=========== Test : mage_stats ===========\n")

    lst_mage = [mage1, mage2, mage3]

    print(f"Mage list :\n{lst_mage}")

    result = mage_stats(lst_mage)
    
    print(f"Stats result:\n{result}")
