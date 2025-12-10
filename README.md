# python_module
Vous trouverez tous les modules pythons du tronc commun de 42.

## Introduction à python

Depuis la piscine et le début du tronc commun nous avons été habitué à utiliser le langage C. Bien que celui-ci soit très intéressant, il est temps d'apprendre à utiliser du python.
Python est un langage bien plus simple à prendre en main que le C. Mais il y a tout de même deux trois petites choses à savoir pour bien commencer avec.

### La Norme flake8

Les sujets de 42 nous demande d'utiliser la norme pyhton **flake8**. Cependant, il n'y a pas de norminette pour vérifier cette fois. Vous pouvez tout de même installer la norme pour l'ajouter au python déjà téléchargé sur votre machine. Pour cela vous n'aurez qu'à utiliser la commande suivante :
```bash
pip install flake8
```
Et pour l'utiliser, vous n'avez qu'à faire la commande suivante :
```bash
python3 -m flake8
```
Comme pour la compilation avec les flags, il est possible de créer un alias pour se simplifier la vie. Pour cela, ouvrez le fichier `~/.zshrc` :
```bash
nano ~/.zshrc
```
Et ajoutez la ligne suivante (vous pouvez mettre n'importe quel nom autre pour votre alias) :
```bash
alias flake8="python3 -m flake8"
```

### Le langage python

Comme python est un langage de barbare non raffiné. Ici, plus besoin d'utiliser de `{}` ou de `;`. Python se base surtout sur l'**indentation**.

#### Test header 4


## Inspirations && Sources

- [github.com/overtekk/python_module](https://github.com/Overtekk/Python-Module-00-10/tree/main/Python%20Module%2000)

**Contact :** alebaron@student.42lehavre.fr
