"""
Fichier : stream_processor.py
Auteur  : alebaron
Date    : 2026/01/10
"""


# +----------------------------------------------------------------+
# |                         Importations                           |
# +----------------------------------------------------------------+

from typing import Any, List
from abc import ABC, abstractmethod


# +----------------------------------------------------------------+
# |                       Classe abstraite                         |
# +----------------------------------------------------------------+

class DataProcessor(ABC):
    """Classe abstraite DataProcessor"""

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"Result: {result}")


# +----------------------------------------------------------------+
# |                       Classe Héritaire                         |
# +----------------------------------------------------------------+

class NumericProcessor(DataProcessor):
    """Permet de gérer les paramètres numériques"""

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def process(self, data: List[int]) -> str:
        """Renvoie la chaîne de statistiques de la liste de nombres"""
        try:
            lon = len(data)
            som = sum(data)
            avg = som / lon
            return (f"Processed {lon} numeric values, sum={som}, avg={avg}")
        except TypeError:
            return ("Error: data must be a list[int].")
        except ZeroDivisionError:
            return ("Error: list musn't be empty")

    def validate(self, data: List[int]) -> bool:
        try:
            lon = len(data)
            _ = sum(data)
            return (lon > 0)
        except Exception:
            return (False)

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class TextProcessor(DataProcessor):
    """Permet de gérer les paramètres textuels"""

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def process(self, data: str) -> str:
        """Renvoie la chaîne de statistiques d'une chaîne de caractères'"""
        if (type(data) is str):
            lon = len(data)
            nb_word = len(data.split(" "))
            return (f"Processed text: {lon} characters, {nb_word} words")
        else:
            return ("Error: data must be a str.")

    def validate(self, data: str) -> bool:
        return (type(data) is str)

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class LogProcessor(DataProcessor):
    """Permet de gérer les paramètres de logs"""

    # +------------------------------------------------------------+
    # |                          Méthodes                          |
    # +------------------------------------------------------------+

    def process(self, data: str) -> str:
        """Renvoie la chaîne de statistiques d'un log"""

        # === Initialisation du tableau de level ===
        log_level = {
            "ERROR": "ALERT",
            "INFO": "INFO",
            "WARN": "WARNING",
            "NOTE": "NOTICE",
            "DEBUG": "DEBUG"
        }

        # === Vérification de la validité ===
        if type(data) is not str:
            return ("Error: data must be a str.")

        alert = data.split(":")

        if (len(alert) != 2):
            return ("Error: The string must be in a similar format: "
                    "“Alert_type: description”")

        # Renvoie de la phrase nécessaire
        try:
            level = log_level[alert[0]]
            return (f"[{level}] {alert[0]} level detected:{alert[1]}")
        except Exception:
            return ("Error: Level alert incorrect.")

    def validate(self, data: str) -> bool:
        log_level = {
            "ERROR": "ALERT",
            "INFO": "INFO",
            "WARN": "WARNING",
            "NOTE": "NOTICE",
            "DEBUG": "DEBUG"
        }

        # === Vérification de la validité ===
        if type(data) is not str:
            return (False)

        alert = data.split(":")

        if (len(alert) != 2):
            return (False)

        # Renvoie de la phrase nécessaire
        try:
            _ = log_level[alert[0]]
            return (True)
        except Exception:
            return (False)

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


# +----------------------------------------------------------------+
# |                             Main                               |
# +----------------------------------------------------------------+

def test_processor(data: Any, proc: DataProcessor, type: str):
    """Permet de tester un processeur comme dans le sujet"""

    print(f"Processing data: \"{data}\"")

    if (proc.validate(data)):
        print(f"Validation: {type} data verified")
    else:
        print(f"Validation: {type} data not verified")

    print(proc.format_output(proc.process(data)))


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # === Test 1 : NumericProcessor ===
    print("Initializing Numeric Processor...")

    data = [1, 2, 3, 4, 5]
    # data = [1, 2, 3, 4, "abc"] # False Test
    proc = NumericProcessor()

    test_processor(data, proc, "Numeric")

    # === Test 2 : TextProcessor ===
    print("\nInitializing Text Processor...")

    data = "Hello Nexus World"
    proc = TextProcessor()

    test_processor(data, proc, "Text")

    # === Test 3 : LogProcessor ===
    print("\nInitializing Log Processor...")

    data = "ERROR: Connection timeout"
    proc = LogProcessor()

    test_processor(data, proc, "Log")

    # === Test 4 : Multi test ===
    print("\nProcessing multiple data types through same interface...")

    print("Result 1:", NumericProcessor().process([2, 2, 2]))
    print("Result 2:", TextProcessor().process("Hello World"))
    print("Result 3:", LogProcessor().process("INFO: System ready"))

    print("\nFoundation systems online. Nexus ready for advanced streams.")
