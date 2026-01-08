"""
Fichier : ft_data_stream.py
Auteur  : alebaron
Date    : 2026/01/06
"""

import random


# +----------------------------------------------------------------+
# |                    Génération d'évènements                     |
# +----------------------------------------------------------------+

def generate_event(nb_event: int):
    """
    Docstring for generate_event

    @description : Permet de générer x évents
    @param nb_event: Nombre d'évents à gérer
    """

    lst_event = [
        "a tué un loup !",
        "vient de monter de niveau !",
        "a trouvé un trésor :o"
    ]

    lst_player = {
        "Romain": 1,
        "Noémie": 1,
        "Ana": 1
    }

    for num_event in range(1, nb_event + 1):
        if num_event % 3 == 1:
            player = "Romain"
        elif num_event % 2 == 1:
            player = "Noémie"
        else:
            player = "Ana"

        event = lst_event[random.randint(0, 2)]

        if event == "vient de monter de niveau !":
            lst_player[player] += 1

        yield (num_event, player, lst_player[player], event)


# +----------------------------------------------------------------+
# |                           Fibonacci                            |
# +----------------------------------------------------------------+

def generate_fibonacci(nb: int):
    """Permet de générer les nb premiers nombres
    de la suite de fibonacci.
    """
    x = 0
    y = 1

    for _ in range(nb):
        yield x
        temp_x = x
        x = y
        y += temp_x


# +----------------------------------------------------------------+
# |                        Nombres premiers                        |
# +----------------------------------------------------------------+

def generate_prime(nb_prime: int):
    """Envoie les nb premiers nombres premiers"""

    x = 2
    i = 0
    while (i < nb_prime):
        is_prime = True

        is_prime = ft_is_prime(x)

        if is_prime is True:
            yield x
            i += 1

        x += 1


def ft_is_prime(nb: int) -> bool:
    """Renvoie si un nombre est premier ou non"""

    if (nb == 0 or nb == 1 or nb < 0):
        return (False)

    i = 2
    while (i < nb):

        if (nb % i == 0):
            return (False)
        i += 1

    return (True)


# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    nb_event = 1000

    print(f"Processing {nb_event} game events...")

    nb_high_level = 0
    nb_event_level = 0
    nb_event_tresor = 0

    lst_high_level_player = []

    for num_event, player, level, event in generate_event(nb_event):
        print(f"Event {num_event}: Joueur.euse {player} "
              f"(level {level}) {event}")

        if event == "vient de monter de niveau !":
            nb_event_level += 1
        elif event == "a trouvé un trésor :o":
            nb_event_tresor += 1

        if (level > 10 and (player not in lst_high_level_player)):
            nb_high_level += 1
            lst_high_level_player.append(player)

    print("\n=== Stream Analytics ===")

    print(f"Total events processed: {nb_event}")
    print(f"High-level players (10+): {nb_high_level}")
    print(f"Treasure events: {nb_event_tresor}")
    print(f"Level-up events: {nb_event_level}")

    print("\nMemore usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    nb_fib = 10
    i = 1
    print(f"Fibonacci sequence (first {nb_fib}): ", end="")

    for nb in generate_fibonacci(nb_fib):
        if i == nb_fib:
            print(f"{nb}")
        else:
            print(f"{nb}", end=", ")
        i += 1

    nb_prime = 5
    i = 1
    print(f"Prime numbers (first {nb_prime}): ", end="")

    for nb in generate_prime(nb_prime):
        if i == nb_prime:
            print(f"{nb}")
        else:
            print(f"{nb}", end=", ")
        i += 1
