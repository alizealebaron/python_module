"""
Fichier : ft_command_quest.py
Auteur  : alebaron
Date    : 2025/12/31
"""


import sys

argc = len(sys.argv)
argv = sys.argv

print("=== Command Quest ===")
if (argc == 1):
    print("No arguments provided!")
else:
    print(f"Arguments received: {argc - 1}")
    for i in range(1, argc):
        print(f"Argument {i}: {argv[i]}")

print(f"Program name: {sys.argv[0]}")
print(f"Total arguments: {argc}")
