# Rock Paper Scissors Game

Welcome to the Rock Paper Scissors Game! This is a simple command-line game built with Python, where you can play the classic game of Rock, Paper, Scissors against the computer.

## Project Overview

This project is designed to help beginners learn Python programming by building an interactive and fun game. The computer randomly selects Rock, Paper, or Scissors, and you try to beat it by making your own choice. The game keeps track of your wins, computer wins, and your best win streak. You can exit the game at any time, and your scores are saved between sessions.

## Features

- Play Rock, Paper, Scissors against the computer
- Accepts both full words and shortcuts for input:
   - `Rock` or `R`
   - `Paper` or `P`
   - `Scissors` or `S`
   - `Exit` or `E` (to quit)
   - `Help` or `H` (to view instructions)
   - `Leaderboard` or `L` (to view scoreboard)
- Tracks your total wins, computer wins, and your best win streak
- Scoreboard and help are available at any time
- Input is case-insensitive and ignores extra spaces
- Scores and streaks are saved in text files (`highscore.txt` and `rounds.txt`) and persist between sessions
- Graceful error handling for file operations and user input

## How to Play

1. Run the script:
   ```powershell
   python main.py
   ```
2. Enter your choice each round (`Rock`, `Paper`, or `Scissors`).
3. Use shortcuts for quick commands:
   - `[R]` Rock
   - `[P]` Paper
   - `[S]` Scissors
   - `[E]` Exit (confirm with Y or N)
   - `[H]` Help
   - `[L]` Leaderboard
4. To exit, type `Exit` or `E`, and confirm by entering `Y` or `Yes`.

## Rules

- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper

## Example

```
Enter your choice: r

----- Round 1 -----
   ✊ Vs ✌️
You chose: Rock
Computer chose: Scissors
You won! 🥳
Your score is: 1
-------------------
```

## Requirements

- Python 3.x

## Getting Started

To start the game, open a terminal in this directory, and run:
```powershell
python main.py
```

If you interrupt the game (Ctrl+C), your progress will be saved automatically.

Enjoy playing and improving your Python skills!