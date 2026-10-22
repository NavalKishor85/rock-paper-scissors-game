# Rock Paper Scissors

![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

A simple Rock Paper Scissors game that runs in your terminal. You play against the computer, and your total score is saved even after you close the game.

The whole game is in one file (`main.py`) and uses only built-in Python, so there is nothing extra to install.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Example](#example)
- [How Scoring Works](#how-scoring-works)
- [Saved Data](#saved-data)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

## Features

- **Play against the computer**, which picks Rock, Paper or Scissors at random each round
- **ASCII-art hands** shown for you and the computer in every round
- **Full words or one-letter shortcuts** for every command (for example `rock` or `r`); input is not case-sensitive, and extra spaces are ignored
- **Win-streak banner** whenever you win 2 or more rounds in a row
- **Leaderboard** with your all-time rounds played, wins, computer wins and best streak
- **Persistent stats**: scores are saved automatically after every round
- **Reset and Exit with confirmation**, asks for confirmation before you exit or reset the game

## Getting Started

### Prerequisites

- **Python 3.8 or newer** (tested on Python 3.12)

Check your Python version:

```bash
python3 --version
```

If Python is not installed:

| OS | Command |
|---|---|
| Windows | `winget install Python.Python.3` |
| macOS | `brew install python` |
| Debian / Ubuntu | `sudo apt update && sudo apt install python3 git` |

Or you can download Python from [python.org](https://www.python.org/downloads/).

## How to Run

Download or clone this project, then open a terminal in the project folder.

```bash
git clone https://github.com/NavalKishor85/rock-paper-scissors-game.git
cd rock-paper-scissors-game
```

Start the game:

```bash
python3 main.py
```

On Windows, use `python main.py`.

## How to Play

1. Start the game. The rules and commands are shown on screen.
2. At the `Enter your choice:` prompt, type `R`, `P` or `S` and press Enter.
3. The game shows both choices and tells you who won the round.
4. Keep playing, or use any command from the table below.

### Game Rules

- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper
- Same choice from both players is a tie

### Commands

| Command | Shortcut | What it does |
|---|---|---|
| `Rock` | `R` | Play Rock |
| `Paper` | `P` | Play Paper |
| `Scissors` | `S` | Play Scissors |
| `Leaderboard` | `L` | Show your all-time scoreboard |
| `Help` | `H` | Show the rules and commands |
| `Reset` | none | Clear all saved scores (asks to confirm) |
| `Exit` | `E` | Quit the game (asks to confirm) |

When the game asks for confirmation, type `y`, `yes` or `1` to confirm, and `n`, `no` or `0` to cancel.

You can also press `Ctrl+C` at any time to quit. Your scores are already saved.

## Example

Winning a round (`Rock` beats Scissors):

```text
+--------------------------------------------------------------------------------+
|                                    Round 1                                     |
+--------------------------------------------------------------------------------+
|                   _______                            _______                   |
|               ---'  ____ )                       ---'  ____ )____              |
|                    (_____)                                 ______)             |
|                    (_____)                              __________)            |
|                    (____)                              (____)                  |
|               ---.__(___)                        ---.__(___)                   |
|                                       VS                                       |
|                   ROCK                               SCISSORS                  |
|                                                                                |
|                              YOU WON! Great move!                              |
|                                                                                |
|               Your score is : 1        Computer score is : 0                   |
+--------------------------------------------------------------------------------+
```

Then typing `L` to open the leaderboard:

```text
+--------------------------------------------------------------------------------+
|        ____   ____ ___  ____  _____     ____   ___    _    ____  ____          |
|       / ___/ / ___/ _ \|  _ \| ____|   | __ ) / _ \  / \  |  _ \|  _ \         |
|       \___ \| |  | | | | |_) |  _|     |  _ \| | | |/ _ \ | |_) | | | |        |
|        ___) | |__| |_| |  _ <| |___    | |_) | |_| / ___ \|  _ <| |_| |        |
|       \____/ \____\___/|_| \_\_____|   |____/ \___/_/   \_\_| \_\____/         |
+--------------------------------------------------------------------------------+
|                       You have played a total of 1 round                       |
|               You won                  : 1  round                              |
|               The Computer won         : 0  rounds                             |
|               Your best streak         : 1  round in a row                     |
+--------------------------------------------------------------------------------+
```

## How Scoring Works

| Screen | What it shows |
|---|---|
| Round screen | The round number and scores for the **current session** only. These start from 0 each time you open the game. |
| Leaderboard | **All-time** totals saved from every session: rounds played (ties included), your wins, computer wins and your best streak. |

- A **streak** is the number of rounds you win in a row.
- A loss or a tie ends your streak.
- Your streak starts again from 0 each time you open the game. Only your best streak is saved.

## Saved Data

Your scores are saved in a text file called `user_states.txt`. It is created automatically in the same folder as `main.py` after your first round.

| Line | What it stores |
|---|---|
| 1 | Total rounds played |
| 2 | Your total wins |
| 3 | Computer's total wins |
| 4 | Your best streak |

- To start fresh, use the `Reset` command in the game, or delete the file.
- If the file is missing or has wrong values, the game starts from 0.

## Project Structure

```text
rock-paper-scissors-game/
├── main.py            # the complete game
├── README.md          # this file
└── user_states.txt    # created after your first round
```

## Troubleshooting

| Problem | Solution |
|---|---|
| `python` is not recognised (Windows) | Restart the terminal after installing Python, or try `py main.py` |
| The game does not start and shows a syntax message | Your Python version is too old. Install Python 3.12 or newer |
| The game screen looks broken | Make your terminal window at least 82 characters wide |
| `Error writing to ...user_states.txt` | The folder is read-only. The game still runs, but scores are not saved |

## Author

**Naval Kishor** - [@NavalKishor85](https://github.com/NavalKishor85)

Enjoy the game and happy coding!
