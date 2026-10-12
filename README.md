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

## Getting Started

Open a terminal and run the commands below based on your operating system.

---

### Windows

```powershell
git clone https://github.com/your-username/rock-paper-scissors-game.git
cd rock-paper-scissors-game
winget install Python.Python.3
python main.py
```

---

### macOS

```bash
git clone https://github.com/your-username/rock-paper-scissors-game.git
cd rock-paper-scissors-game
brew install python
python3 main.py
```

---

### Linux (Debian/Ubuntu)

```bash
git clone https://github.com/your-username/rock-paper-scissors-game.git
cd rock-paper-scissors-game
sudo apt update && sudo apt install python3
python3 main.py
```

---

## How to Play

Once the game starts, enter your choice each round using the following commands:

| Input | Action |
|---|---|
| `R` or `Rock` | Play Rock ✊ |
| `P` or `Paper` | Play Paper 🖐️ |
| `S` or `Scissors` | Play Scissors ✌️ |
| `H` or `Help` | View in-game instructions |
| `L` or `Leaderboard` | View the scoreboard |
| `E` or `Exit` | Quit the game |

> **Note:** Input is **case-insensitive** — `r`, `R`, and `rock` are all accepted. When exiting, confirm with `Y` or `N`.

### Rules

- **Rock** beats Scissors
- **Paper** beats Rock
- **Scissors** beats Paper

### Example Round

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

> **Tip:** If you interrupt the game at any time with `Ctrl+C`, your progress and scores will be saved automatically.

Enjoy the game and happy coding!