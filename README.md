# Memora Using Guide

## **ENGLISH**

## Presentation

Memora is a simple and engaging command-line game designed to help you train and test your memory of your 'Centium' and 'Millenium'. In this game, you will be presented with a number, and your task is to correctly input the element that corresponds to this number.

Memora consists of a main Python file and two JSON files: centium.json and millenium.json. These files store the elements of your Centium and Millenium respectively. The keys in these JSON files are numbers ranging from 00 to 99 in centium.json and from 000 to 999 in millenium.json. The values are blank by default, you'll have to fill them in with the elements of your Centium and Millenium.

## Demo

[Click here to view the video](https://gitlab.com/kitsuiwebster/memora/-/raw/assets/demo.mp4)

## Prerequisites

### Python

Ensure you have Python 3.6 or higher installed. You can download Python from the official site: [Download Python](https://www.python.org/downloads/)

### Pip

Windows:

`python get-pip.py`

Debian/Ubuntu:

`sudo apt install python3-pip`

Fedora:

`sudo dnf install python3-pip`

CentOS:

`sudo yum install python3-pip`

Arch Linux:

`sudo pacman -S python-pip`

## How to play

### Installation

`git clone https://gitlab.com/kitsuiwebster/memora.git`

`cd memora`

### Dependency

`pip install colorama`

### Setting up your Centium/Millenium

Open the centium.json and millenium.json files. You will see a list of keys (numbers) with blank values. Fill in the values with the elements of your Centium and Millenium.

e.g.

```json
{
    "00": "rari",
    "01": "rouge",
    "02": "rapace",
    "03": "rateau",
    "04": "rakan",
    "05": "ramriddlz",
    "06": "ryze",
    "07": "ruler",
    "08": "robe",
// the rest of your elements
}
```

### Launch Memora

Windows:

`python memora.py`

Linux: 

`python3 memora.py`

### Play Memora

From the main menu, to start training your Centium, press '1' and hit 'Enter'. The game will randomly pick a number from centium.json and ask you to input the corresponding element. If you want to train your Millenium, press '2' and hit 'Enter'. Similar to Centium training, the game will select a number from millenium.json and ask for the corresponding element. In case of a wrong answer during training, the menu will reappear, allowing you to choose between training again or quitting the game.

## Enjoy training ! 😁

## **FRENCH**

## Présentation

Memora est un jeu en ligne de commande simple et attrayant conçu pour vous aider à entraîner et tester votre mémoire de votre 'Centium' et 'Millenium'. Dans ce jeu, un nombre vous sera présenté, et votre tâche consiste à entrer correctement l'élément qui correspond à ce nombre.

Memora se compose d'un fichier Python principal et de deux fichiers JSON : centium.json et millenium.json. Ces fichiers stockent les éléments de votre Centium et Millenium respectivement. Les clés dans ces fichiers JSON sont des nombres allant de 00 à 99 dans centium.json et de 000 à 999 dans millenium.json. Les valeurs sont par défaut vides, vous devrez les remplir avec les éléments de votre Centium et Millenium.

## Prérequis

### Python

Assurez-vous d'avoir installé Python 3.6 ou une version ultérieure. Vous pouvez télécharger Python depuis le site officiel : [Télécharger Python](https://www.python.org/downloads/)

### Pip

Windows:

`python get-pip.py`

Debian/Ubuntu:

`sudo apt install python3-pip`

Fedora:

`sudo dnf install python3-pip`

CentOS:

`sudo yum install python3-pip`

Arch Linux:

`sudo pacman -S python-pip`

## Comment jouer

### Installation du jeu

`git clone https://gitlab.com/kitsuiwebster/memora.git`

`cd memora`

### Dépendence

`pip install colorama`

### Mettre en place votre Centium/Millenium

Ouvrez les fichiers centium.json et millenium.json. Vous verrez une liste de clés (nombres) avec des valeurs vides. Remplissez les valeurs avec les éléments de votre Centium et Millenium.

Par example:

```json
{
    "00": "rari",
    "01": "rouge",
    "02": "rapace",
    "03": "rateau",
    "04": "rakan",
    "05": "ramriddlz",
    "06": "ryze",
    "07": "ruler",
    "08": "robe",
// le reste de vos éléments
}
```

### Lancer Memora

Windows:

`python memora.py`

Linux: 

`python3 memora.py`

### Jouer à Memora

Depuis le menu principal, pour commencer l'entraînement sur votre Centium, appuyez sur '1' et appuyez sur 'Entrée'. Le jeu choisira au hasard un nombre à partir de centium.json et vous demandera de saisir l'élément correspondant. Si vous souhaitez entraîner votre Millenium, appuyez sur '2' puis sur 'Entrée'. Comme pour l'entraînement du Centium, le jeu sélectionnera un nombre de millenium.json et vous demandera de fournir l'élément correspondant. En cas de réponse incorrecte pendant l'entraînement, le menu principal réapparaîtra, vous donnant l'option de continuer l'entraînement ou de quitter le jeu.

## Amusez-vous bien ! 😁
