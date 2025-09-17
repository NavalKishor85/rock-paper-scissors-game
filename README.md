# Rock Paper Scissors Game

Welcome to the Rock Paper Scissors Game! This is a simple command-line game built with Python where you can play the classic game of Rock, Paper, Scissors against the computer.

## Project Overview

This project is designed to help beginners learn Python programming by building a fun and interactive game. The computer randomly selects Rock, Paper, or Scissors, and you try to beat it by making your own choice. The game keeps track of your wins and winning streaks, and you can exit the game at any time.

## Features

- Play Rock, Paper, Scissors against the computer
- Accepts both full words and shortcuts for input:
  - `Rock` or `R`
  - `Paper` or `P`
  - `Scissors` or `S`
  - `Exit` or `E` (to quit)
  - `Help` or `H` (to view instructions)
  - `Leaderboard` or `L` (to view scoreboard)
- Tracks total user wins, computer wins, and your best win streak
- Scoreboard and help available at any time
- Input is case-insensitive and ignores extra spaces

## How to Play

1. Run the script:
   ```
   python main.py
   ```
2. Enter your choice each round (`Rock`, `Paper`, or `Scissors`).
3. Use shortcuts for quick commands:
   - `[R]` Rock
   - `[P]` Paper
   - `[S]` Scissors
   - `[E]` Exit
   - `[H]` Help
   - `[L]` Leaderboard
4. To exit, type `Exit` or `E` and confirm by entering [Y].

## Rules

- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper

## Example

```
Enter your choice: r
You chose: Rock
Computer chose: Paper
You lost! 😥
Your score is: 0
```

## Requirements

- Python 3.x

## Getting Started

To start the game, open a terminal in this directory and run:
```powershell
python main.py
```

Enjoy playing and improving your Python skills!