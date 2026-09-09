# C.O.R's Tic-Tac-Toe Game

A straightforward command-line version of Tic-Tac-Toe built with Python.

You play as **X** and the computer plays as **O**. Choose a numbered space on the board, take turns, and see who gets three in a row first. When the round ends, you can start another game right away.

## Features

- Play against the computer in the terminal
- Clear numbered board layout for choosing moves
- Checks rows, columns, and diagonals for a win
- Detects draws when the board is full
- Prevents moves on already occupied spaces
- Handles invalid entries without ending the game
- Lets you quit during a round or play again after it ends

## Getting started

This project uses only Python’s standard library, so there are no packages to install.

```bash
git clone https://github.com/okwuchukwuchiedozie-stack/Tic-Tac-Toe--Game.git
cd Tic-Tac-Toe--Game
python main.py
```

On Windows, use this command if `python` is not recognised:

```bash
py main.py
```

## How to play

The board positions are numbered from 1 to 9:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

When prompted, enter the number of the space where you want to place your **X**.

```text
Player X, enter your move from 1 - 9 or 'q' to quit:
```

The computer then takes its turn as **O**.

The first player to complete a row, column, or diagonal wins. If every space is filled without a winner, the game ends in a draw.

## Example

```text
Welcome to C.O.R's Tic-Tac-Toe game!

The board positions are numbered like this

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Player X, enter your move from 1 - 9 or 'q' to quit: 5
Computer is thinking...
```

## Project structure

```text
Tic-Tac-Toe--Game/
├── main.py       # game logic and command-line interface
└── README.md
```
