<p align="center">
  <img src="https://github.com/alizealebaron/alizealebaron/blob/main/assets/python-module_simple.png" width="120"/>
</p>
<h3 align="center">
  <em>Python Fundamentals Through Garden Data</em>
</h3>

---

> [!CAUTION]  
> Les sujets des modules python ont été modifiés et changés pendant la réalisation des exercices. Certains exercices seront peut-être déjà dépassé et différent de ceux que vous aurez à programmer.

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

### Le langage Python

Comme python est un langage de barbare non raffiné. Ici, plus besoin d'utiliser de `{}` ou de `;`. Python se base surtout sur l'**indentation**.

### L'identation

Là où l'indentation est peu importe pour le fonctionnement du code en C (elle est surtout utilisée pour apporté de la lisibilité), en python, l'indentation fait partie de la syntax. **Un code mal indenté pourra ne pas fonctionner comme souhaité**.

- Les blocs de code (comme à l'intérieur d'un `if`) commencent avec un `:`.
- Tout à l'intérieur du bloc être indenté avec des tabulations.
- Lorsque l'on arrête d'indenter, nous sommes à l'extérieur du bloc.

Par exemple :
```c
// En ✨ C ✨
if (a > b)
{
	printf("Coin !");
}
printf("Quack !");
```
```python
# En ☠️ Python ☠️
if a > b:
    print("Coin !") # A l'intérieur du if
print("Quack !")    # A l'extérieur du if
```

### Déclaration des variables

En python, il n'y a pas besoin de déclarer les types des variables, oublions donc les `char *` et autre `int` python s'occupera d'attribuer un type à la variable selon ce qu'elle contient. Ainsi, les variables se déclarent de cette façon (moi j'appelle ça de la magie noire mais apparemment il s'agit de [Dynamic Typing](https://simple.wikipedia.org/wiki/Dynamic_typing)) :
```python
a = 3
b = "Quack"
```
> [!CAUTION]  
> CEPENDANT ! Ce n'est pas parceque vous ne définissez pas les types de variables que ça ne vous posera pas problème. Il se peut que cela pose des problèmes plus tard car là où vous pensez avoir un int, vous avez une chaîne de caractère. Le programme ne fonctionnera pas comme voulu ainsi. 

### Déclarations de fonctions

Les fonctions ont toujours besoin d'être déclarées, mais la synthaxe est différente. Voici comment déclarer une fonction en python :
```python
def add(a, b):
    return a + b
```

### Afficher du texte

Python possède aussi une fonction `printf` qui se nomme `print`. Son fonctionnement est cependant différent, ici plus besoin d'utiliser de `%s` ou `%d` puisque les variables sont typées par python lui-même. Ainsi, il est possible d'afficher le contenus des variables de cette façon :
```python
name = "Sir Quack the third"
level = 10

# Première façon avec print(f"")
print(f"Player {name} is level {level}") # Le f est important, il permet d'afficher les variables entre {}

# Deuxième façon sans le f (moins pratique)
print("Player " + name + " is level " + str(level))
```

### Compilation et exécution du programme

En python pas besoin de compiler, oubliez donc les `make` ou les `cc -Wall -Werror -Wextra`. Le langage python s'exécute directement de haut en bas. Ainsi la commande et la suivante :
```bash
python3 my_script.py
```

### Plus qu'à continuer..

Maintenant que vous avez les rudiments de base pour utiliser python, vous allez pouvoir commencer les modules python. Bon courage à vous !

## Inspirations && Sources

- [github.com/overtekk/python_module](https://github.com/Overtekk/Python-Module-00-10/tree/main/Python%20Module%2000)

**Contact :** alebaron@student.42lehavre.fr
