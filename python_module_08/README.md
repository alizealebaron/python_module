<p align="center">
  <img src="https://github.com/alizealebaron/alizealebaron/blob/main/assets/python-module_simple.png" width="120"/>
</p>
<h3 align="center">
  <em>Welcome to the Real World of Data Engineering</em>
</h3>

---

## ⚠️ Avant propos

- **Portfolio :** Ce répertoire se concentre sur un seul sujet. Vous pouvez retrouver tous mes projets sur mon [profil](https://github.com/alizealebaron).
- **Sujet :** Conformément aux règles de 42, vous ne trouverez pas le sujet de l'exercice dans ce répertoire.
- **État du projet:** Le code est exactement le même que lorsqu'il a été validé. Il ne sera pas mis à jour même s'il contient des erreurs.
- **Aide & Licence :** Ce répertoire est principalement là pour vous aider à faire votre propre code. Évitez de copier / coller sans comprendre le code.

## 🦆 Status

**Commencé le :** 27/01/2026.

**Rendu le :** 29/01/2026.

**Note :** 100/100.

## Quelques notes sur l'utilisation des environnements

Les environnements Python sont des outils qui permettent d’isoler chaque projet avec ses propres dépendances. Par exemple, si un projet A nécessite la version 3.1 d’un package et qu’un projet B utilise la version 3.5 du même package, l’installation de la version 3.5 pourrait remplacer la 3.1. Cela risquerait de causer des conflits ou des erreurs de compatibilité, surtout sur des projets complexes.

Un environnement virtuel est un dossier qui contient une copie indépendante de Python ainsi qu’un espace réservé aux packages. Lorsqu’il est activé, toutes les installations via pip install ne concernent que cet environnement : ni votre système, ni vos autres projets ne sont modifiés.

## Créer un environnement virtuel

Pour créer un nouvel environnement, utilisez la commande suivante :

```bash
python3 -m venv nom_environnement
```

> [!NOTE]
> Le nom `.venv` est couramment utilisé, mais vous pouvez choisir un autre nom si vous le souhaitez.

## Activer l’environnement

La méthode d’activation dépend de votre système d’exploitation.

### Linux (Ubuntu)
```bash
source .venv/bin/activate
```

### Windows (PowerShell)
```powershell
.venv\Scripts\Activate.ps1
```

> [!CAUTION]
> Si vous rencontrez une erreur liée à la politique d’exécution, exécutez :
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Windows (CMD)
```cmd
.venv\Scripts\activate.bat
```

Une fois activé, votre terminal affichera le nom de l’environnement en préfixe. Pour quitter l’environnement, utilisez :

```bash
deactivate
```

## Gérer les packages

| Action                     | Commande                          |
|----------------------------|-----------------------------------|
| Installer un package       | `pip install nom_package`         |
| Mettre à jour un package   | `pip install --upgrade nom_package` |
| Lister les packages        | `pip list`                        |
| Désinstaller un package    | `pip uninstall nom_package`      |

## Exporter et importer les dépendances

Pour sauvegarder les dépendances installées :
```bash
pip freeze > requirements.txt
```

Pour installer les dépendances depuis un fichier :
```bash
pip install -r requirements.txt
```

Voilà qui conclu les base de l'utilisation des environnements python avec pip (pour poetry, je vous laisse chercher c:) !

## 💡 Inspirations && Sources

- [github.com/overtekk/python_module_08](https://github.com/Overtekk/Python-Module-00-10/tree/main/Python%20Module%2008)
- [blog.stephane-robert.info/python/environnements-virtuels](https://blog.stephane-robert.info/docs/developper/programmation/python/environnements-virtuels/)
- [betterstack.com/guides/poetry-vs-pip](https://betterstack.com/community/guides/scaling-python/poetry-vs-pip/)
- [github.com/shadox254/python_module_08](https://github.com/shadox254/Module-Python/tree/main/Module-08)

**Contact :** alebaron@student.42lehavre.fr