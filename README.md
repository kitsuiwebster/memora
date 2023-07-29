# Memora Using Guide

## Presentation

Memora is a simple and engaging command-line game designed to help you train and test your memory of your 'Centium' and 'Millenium'. In this game, you will be presented with a number, and your task is to correctly input the element that corresponds to this number.

## Game Files

Memora consists of a main Python file and two JSON files: centium.json and millenium.json. These files store the elements of your Centium and Millenium respectively. The keys in these JSON files are numbers ranging from 00 to 99 in centium.json and from 000 to 999 in millenium.json. The values are blank by default, you'll have to fill them in with the elements of your Centium and Millenium.

## How to play

### Installation

`git clone https://gitlab.com/kitsuiwebster/memora.git`

`cd memora`

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

`python memora.py` or `python3 memora.py`

### Play Memora

From the menu, to start training your Centium, press '1' and hit 'Enter'. The game will randomly pick a number from centium.json and ask you to input the corresponding element. If you want to train your Millenium, press '2' and hit 'Enter'. Similar to Centium training, the game will select a number from millenium.json and ask for the corresponding element. In case of a wrong answer during training, the menu will reappear, allowing you to choose between training again or quitting the game.

## Dependencies

### Install Colorama

`pip install colorama`

## Enjoy training 😁
