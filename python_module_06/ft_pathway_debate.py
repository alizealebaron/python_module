# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: alebaron <alebaron@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/19 12:20:51 by alebaron        #+#    #+#               #
#  Updated: 2026/01/19 12:44:45 by alebaron        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def absolute_import() -> None:
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem

    print("Testing Absolute Imports (from basic.py):")

    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")


def relative_imports() -> None:
    from alchemy.transmutation.advanced import philosophers_stone
    from alchemy.transmutation.advanced import elixir_of_life

    print("\nTesting Relative Imports (from advanced.py):")

    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")


def package_access() -> None:
    import alchemy.transmutation

    print("\nTesting Package Access:")

    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")

    # === Test 1 : Imports absolus ===
    absolute_import()

    # === Test 2 : Imports relatifs ===
    relative_imports()

    # === Test 3 : Package Access ===
    package_access()

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
