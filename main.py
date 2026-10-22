"""
----Rock Paper Scissors Game----
Command-line game: user vs computer. 
The computer randomly picks Rock, Paper, or Scissors. The user enters their choice. 
The winner is decided by classic rules. Tracks total wins and win streaks. 
"""
import random
import os

CHOICES = ['Rock', 'Paper', 'Scissors']
STATS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_states.txt")
STATS_LINE_NUM = {
    "rounds_played": 0,
    "user_wins": 1,
    "computer_wins": 2,
    "high_score": 3
}
WIDTH = 80


def display_rules():
    print(r"""
+--------------------------------------------------------------------------------+
|            ____   ___   ____ _  __    ____   _    ____  _____ ____             |    
|           |  _ \ / _ \ / ___| |/ /   |  _ \ / \  |  _ \| ____|  _ \            |    
|           | |_) | | | | |   | ' /    | |_) / _ \ | |_) |  _| | |_) |           |    
|           |  _ <| |_| | |___| . \    |  __/ ___ \|  __/| |___|  _ <            |    
|           |_| \_\\___/ \____|_|\_\   |_| /_/   \_\_|   |_____|_| \_\           |    
|                ____   ____  ___  ____  ____   ___  ____   ____                 |
|               / ___| / ___||_ _|/ ___|/ ___| / _ \|  _ \ / ___|                |
|               \___ \| |     | | \___ \\___ \| | | | |_) |\___ \                |
|                ___) | |___  | |  ___) |___) | |_| |  _ <  ___) |               |
|               |____/ \____||___||____/|____/ \___/|_| \_\|____/                |
+--------------------------------------------------------------------------------+
|                        Welcome to 'ROCK PAPER SCISSORS'!                       |
| Rules:                                                                         |
|   - Rock beats Scissors                                                        |
|   - Paper beats Rock                                                           |
|   - Scissors beats Paper                                                       |
| Instructions:                                                                  |   
|   - Enter 'Rock', 'Paper', or 'Scissors' to play                               |
|   - Enter 'Exit' to quit the game                                              |              
| Shortcuts:                                                                     |
|   [R] - Rock                                                                   |
|   [P] - Paper                                                                  |
|   [S] - Scissors                                                               |
|   [H] - Help                                                                   |
|   [E] - Exit                                                                   |
|   [L] - Leaderboard                                                            |
|   [Reset] - Reset the game                                                     |
| *Input is case-insensitive                                                     |   
+--------------------------------------------------------------------------------+
""", end="")


def help():
    # Display all instructions and valid user input combinations
    print(r"""
+--------------------------------------------------------------------------------+
|             _   _ _____ _     ____       __  __ _____ _   _ _    _             |
|            | | | | ____| |   |  _ \     |  \/  | ____| \ | | |  | |            |
|            | |_| |  _| | |   | |_) |    | |\/| |  _| |  \| | |  | |            |
|            |  _  | |___| |___|  __/     | |  | | |___| |\  | \__/ |            |
|            |_| |_|_____|_____|_|        |_|  |_|_____|_| \_|\____/             |
+--------------------------------------------------------------------------------+
| Rules:                                                                         |
|    - Rock beats Scissors                                                       |
|    - Paper beats Rock                                                          |         
|    - Scissors beats Paper                                                      |
| Instructions:                                                                  |
|    - Enter 'Rock', 'Paper', or 'Scissors' to play                              |
|    - Enter 'Exit' to quit the game                                             |
|    - Enter 'Help' at any time to see these instructions again                  |
|    - Enter 'Reset' to reset the game stats and clear all game data             |
|    - You can also use these shortcuts:                                         |
|           [R] - Rock                                                           |
|           [P] - Paper                                                          |
|           [S] - Scissors                                                       |
|           [E] - Exit                                                           |
|           [H] - Help                                                           |
|           [L] - Leaderboard, to see your scoreboard                            |
|           [Reset] - Reset the game                                             |
| *Input is case-insensitive                                                     |
+--------------------------------------------------------------------------------+
""", end="")
    

def select_computer_choice(CHOICES):
    return random.choice(CHOICES)

def take_input_from_user():
    shortcuts = {
        'rock': 'Rock', 'r': 'Rock',
        'paper': 'Paper', 'p': 'Paper',
        'scissors': 'Scissors', 's': 'Scissors',
        'exit': 'Exit', 'e': 'Exit',
        'help': 'Help', 'h': 'Help',
        'leaderboard': 'Leaderboard', 'l': 'Leaderboard',
        'reset': 'Reset'
    }
    while True:
        try:
            print()
            user_input = input("Enter your choice: ").strip().lower()
        except EOFError:
            print("\nNo input received. Exiting...")
            return 'Exit'
        else:
            if user_input in shortcuts:
                return shortcuts[user_input]
            else:
                print("Invalid input! Please enter valid input or 'Help' to know the instructions.")


def compute_result(user_choice, computer_choice):
    # Determine round result based on user and computer choices.
    if (computer_choice=="Rock"):
        if (user_choice=="Paper"):
            result = "won"
        elif (user_choice=="Rock"):
            result = "tie"
        else:
            result = "lost"
    elif (computer_choice=="Paper"):
        if (user_choice=="Paper"):
            result = "tie"
        elif (user_choice=="Rock"):
            result = "lost"
        else:
            result = "won"
    else:
        if (user_choice=="Paper"):
            result = "lost"
        elif (user_choice=="Rock"):
            result = "won"
        else:
            result = "tie"
    return result


def update_score(stats, result, user_win_count, user_win_streak, computer_win_count):
    if result == "won":
        user_win_count += 1
        user_win_streak += 1
        write_state(stats["rounds_played"] + 1, stats["user_wins"] + 1, stats["computer_wins"], max(stats["high_score"], user_win_streak))
    elif result == "lost":
        user_win_streak = 0
        computer_win_count += 1
        write_state(stats["rounds_played"] + 1, stats["user_wins"], stats["computer_wins"] + 1, max(stats["high_score"], user_win_streak))
    else:
        user_win_streak = 0
        write_state(stats["rounds_played"] + 1, stats["user_wins"] , stats["computer_wins"], max(stats["high_score"], user_win_streak))
    return user_win_count, user_win_streak, computer_win_count


def display_scoreboard(stats):
    print("\n+", "-"*80, "+", sep="",end="")
    print(rf"""                             
|        ____   ____ ___  ____  _____     ____   ___    _    ____  ____          |
|       / ___/ / ___/ _ \|  _ \| ____|   | __ ) / _ \  / \  |  _ \|  _ \         |
|       \___ \| |  | | | | |_) |  _|     |  _ \| | | |/ _ \ | |_) | | | |        |
|        ___) | |__| |_| |  _ <| |___    | |_) | |_| / ___ \|  _ <| |_| |        |
|       \____/ \____\___/|_| \_\_____|   |____/ \___/_/   \_\_| \_\____/         |
""", end="")
    print("+", "-"*80, "+", sep="")
    print_screen("", f"You have played a total of {stats["rounds_played"]} {"round" if stats["rounds_played"] == 1 else "rounds"}", "")
    print_screen("You won", "", f": {stats["user_wins"]:<2} {"round" if stats["user_wins"] == 1 else "rounds"}")
    print_screen("The Computer won", "", f": {stats["computer_wins"]:<2} {"round" if stats["computer_wins"] == 1 else "rounds"}")
    print_screen("Your best streak", "", f": {stats["high_score"]:<2} {"round" if stats["high_score"] == 1 else "rounds"} in a row")
    print("+", "-"*80, "+", sep="")


def print_screen(left, center, right, spacing=0):
    padding = 15
    if center != "":
        text_width = len(center)
        left_padding = (WIDTH - text_width) // 2
        right_padding = WIDTH - text_width - left_padding
        print("|", " " * left_padding, center, " " * right_padding, "|", sep="")
    if left != "" and right != "":
        print("|", " "*padding, f"{left:<25}", " "*spacing, f"{right:<25}", " "*(padding - spacing), "|", sep="")


def read_stats(file):
    try:
        with open(STATS_FILE) as f:
            lines = f.readlines()
            value = lines[STATS_LINE_NUM[file]]
        return int(value)
    except (FileNotFoundError, ValueError, IndexError):
        return 0


def write_state(rounds_played, user_win, computer_win, high_score):
    # Write rounds_played and high_score to user_states.txt (one value per line).
    try:
        with open(STATS_FILE, 'w') as f:
            f.write(f"{rounds_played}\n{user_win}\n{computer_win}\n{high_score}\n")
    except Exception as e:
        print(f"Error writing to {STATS_FILE}: {e}")


def get_ascii(choice):
    drawings = {
    "rock": [
        "    _______    ",
        "---'  ____ )   ",
        "     (_____)   ",
        "     (_____)   ",
        "     (____)    ",
        "---.__(___)    "
    ],
    "paper": [
        "     _______       ",
        "---'    ____ )___  ",
        "           ______) ",
        "          _______) ",
        "         _______)  ",
        "---.__________)    "
    ],
    "scissors": [
        "    _______       ",
        "---'  ____ )____  ",
        "          ______) ",
        "       __________)",
        "      (____)       ",
        "---.__(___)        "
    ]}
    return drawings[choice.lower()]


def print_result(result, round_number, user_choice, computer_choice, user_win_count, user_win_streak, computer_win_count):
    user_art, computer_art = get_ascii(user_choice), get_ascii(computer_choice)
    if result == "won":
        result_msg = "YOU WON! Great move!"
    elif result == "lost":
        result_msg = "YOU LOST! Better luck next time!"
    else:
        result_msg = "IT'S A TIE! Well played!"
    
    print("\n+", "-"*80, "+", sep="")
    print_screen("", f"Round {round_number} ", "")
    print("+", "-"*80, "+", sep="")
    for user_ascii, computer_ascii in zip(user_art, computer_art):
        print_screen(user_ascii, "", computer_ascii, 10)
    print_screen(f"    {user_choice.upper()}", "VS", f"    {computer_choice.upper()}",10)
    print_screen(" ", "", " ")
    print_screen("", f"{result_msg}", "")
    print_screen(" ", "", " ")
    if user_win_streak >= 2:
        print_screen("", f"You've won {user_win_streak} times in a row!", "")
        print_screen(" ", "", " ")
    print_screen(f"Your score is : {user_win_count}", "", f"Computer score is : {computer_win_count}")
    print("+", "-"*80, "+", sep="")


def confirmation(msg):
    confirmation = False
    while True:
        try:
            confirm = input(msg).strip().lower()
            if confirm in ['y', 'yes', '1']:
                confirmation = True
                break
            elif confirm in ['n', 'no', '0']:
                break 
            else:
                print("Please enter 'y' to confirm or 'n' to cancel.\n")
        except EOFError:
            print("\nNo input received!")
            break
    return confirmation

def main():
    # display the game rules and instructions
    display_rules()

    # Initialize counters for wins, streaks, and rounds
    user_win_count = computer_win_count = user_win_streak = round_number = 0

    # Read high score and rounds played from user_states.txt - if user has played before
    stats = {
        "rounds_played": 0, 
        "user_wins": 0,
        "computer_wins": 0,
        "high_score": 0
        }

    try:
        while True:
            # Save the user win streak every time so it save as a high score
            for file in stats:
                stats[file] = read_stats(file)
                # write_state(stats["rounds_played"] + round_number, stats["user_wins"] + user_win_count, stats["computer_wins"] + computer_win_count, user_win_streak)

            # Prompt user for input and computer randomly selects a choice
            computer_choice = select_computer_choice(CHOICES)
            user_choice = take_input_from_user()

            # Handle user command
            if user_choice == 'Help':
                help()
            elif user_choice == 'Exit':
                if confirmation("Do you want to exit the game? [y/n] "):
                    # write_state(stats["rounds_played"] + round_number, stats["user_wins"] + user_win_count, stats["computer_wins"] + computer_win_count, stats["high_score"])
                    print("Exiting...")
                    break
            elif user_choice == "Leaderboard":
                display_scoreboard(stats)
            elif user_choice == "Reset":
                if confirmation("Are you sure you want to reset the game? This will clear your game data. [y/n] "):
                    user_win_count = computer_win_count = user_win_streak = round_number = 0
                    write_state(0, 0, 0, 0)
                    print("Game has been reset.")
            else:
                round_number += 1
                result = compute_result(user_choice, computer_choice)
                user_win_count, user_win_streak, computer_win_count = update_score(stats, result, user_win_count, user_win_streak, computer_win_count)
                print_result(result, round_number, user_choice, computer_choice, user_win_count, user_win_streak, computer_win_count)
    
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")

if __name__ == "__main__":
    main()

