"""
Fichier : ft_score_analytics.py
Auteur  : alebaron
Date    : 2026/01/01
"""


import sys


def ft_score_analytics() -> None:
    """Get argument and display a scoreboard if everything is correct"""
    # === Get the argument ===

    argc = len(sys.argv)
    argv = sys.argv

    # === Check the number of argument ===

    try:
        if (argc == 1):
            raise ValueError("No scores provided. Usage: "
                             "python3 ft_score_analytics.py "
                             "<score1> <score2> ...")
    except ValueError as error:
        print(error)
        return None

    # === Check that every argument is a number (no banana allowed) ===

    lst_score = [None] * (argc - 1)

    try:
        for i in range(1, argc):
            tmp_nb = int(argv[i])
            lst_score[i-1] = tmp_nb
    except ValueError:
        print("Error : Arguments must be number.")

    # === Display all informations about the score ===

    total = sum(lst_score)
    avg = sum(lst_score) / (argc - 1)
    ran = max(lst_score) - min(lst_score)

    print("Score processed: [", end="")
    for i in range(0, len(lst_score)):
        if (i != (len(lst_score) - 1)):
            print(f"{lst_score[i]}", end=", ")
        else:
            print(f"{lst_score[i]}", end="]\n")

    print(f"Total players: {argc - 1}")
    print(f"Total score: {total}")
    print(f"Average score: {avg}")
    print(f"High score: {max(lst_score)}")
    print(f"Low score: {min(lst_score)}")
    print(f"Score range: {ran}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
