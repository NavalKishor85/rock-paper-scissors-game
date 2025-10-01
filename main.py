"""
----Rock Paper Scissors Game----
Command-line game: user vs computer. 
The computer randomly picks Rock, Paper, or Scissors. The user enters their choice. 
The winner is decided by classic rules. Tracks total wins and win streaks. 
The user can exit at any time.
"""
import random

CHOICES = ['Rock', 'Paper', 'Scissors']


def display_rules():
    # Display the game rules and instructions
    print("\n---- Welcome to 'ROCK PAPER SCISSORS'! ----")
    print("- Enter 'Rock', 'Paper', or 'Scissors' to play")
    print("- Enter 'Exit' at any time to quit the game")
    print("Shortcuts:")
    print("  [R] - Rock, [P] - Paper, [S] - Scissors, [E] - Exit, [H] - Help, [L] - Leaderboard")
    print("(Input is case-insensitive and leading/trailing spaces are ignored)")
    print("  ")

def help():
    # Display all instructions and valid user input combinations
    print("\n------ HELP ------")
    print("Rules:")
    print("- Rock beats Scissors")
    print("- Paper beats Rock")
    print("- Scissors beats Paper")    
    print("Instructions:")
    print("- Enter 'Rock', 'Paper', or 'Scissors' to play")
    print("- Enter 'Exit' or 'E' to quit the game")
    print("- Enter 'Help' at any time to see these instructions again")
    print("- You can also use these shortcuts: \n [R] - Rock \n [P] - Paper \n [S] - Scissors \n [E] - Exit \n [H] - Help \n [L] - Leaderboard")
    print("(Input is case-insensitive and leading/trailing spaces are ignored)")
    print("-----------------------------\n")

def select_computer_choice(CHOICES):
    # Randomly select a choice for the computer
    computer_choice = random.choice(CHOICES)
    return computer_choice

def take_input_from_user():
    # Prompt the user until a valid choice is entered.
    shortcuts = {
        'rock': 'Rock', 'r': 'Rock',
        'paper': 'Paper', 'p': 'Paper',
        'scissors': 'Scissors', 's': 'Scissors',
        'exit': 'Exit', 'e': 'Exit',
        'help': 'Help', 'h': 'Help',
        'leaderboard': 'Leaderboard', 'l': 'Leaderboard'
    }
    while True:
        try:
            user_input = input("Enter your choice: ").strip().lower()
        except EOFError:
            print("Input error. Please try again.")
            continue
        if not user_input:
            print("You entered nothing. Please enter 'Rock', 'Paper', or 'Scissors'.")
            continue
        if user_input in shortcuts:
            return shortcuts[user_input]
        print("Invalid input. Please enter only 'Rock', 'Paper', or 'Scissors'.")

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

def getemoji(user_choice, computer_choice):
    # Return emojis for user and computer choices.
    if (computer_choice=="Rock"):
        computer_emoji = "✊"
    elif (computer_choice=="Paper"):
        computer_emoji = "✋"
    elif (computer_choice=="Scissors"):
        computer_emoji = "✌️"
    else:
        computer_emoji = ""
    if (user_choice=="Rock"):
        user_emoji = "✊"
    elif (user_choice=="Paper"):
        user_emoji = "✋"
    elif (user_choice=="Scissors"):
        user_emoji = "✌️"
    else:
        user_emoji = ""
    return user_emoji, computer_emoji

def update_score(result, user_win_count, user_win_streak, computer_win_count):
    # Update win and streak counters based on result.
    if result == "won":
        user_win_count += 1
        user_win_streak += 1
    elif result == "lost":
        user_win_streak = 0
        computer_win_count += 1
    else:
        user_win_streak = 0
    return user_win_count, user_win_streak, computer_win_count

def print_result(result, round_number, user_choice, computer_choice, user_win_count, user_win_streak, user_emoji, computer_emoji):
    # Print round number, choices, result, and current score.
    print(f"\n----- Round {round_number} -----")
    print(f"     {user_emoji} Vs {computer_emoji}")
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "won":
        print("You won! 🥳")
    elif result == "tie":
        print("It's a tie! 😐")
    else:
        print("You lost! 😥")
        
    print(f"Your score is: {user_win_count}")

    # Print message for win streak
    if user_win_streak >= 2:
        print(f"Congratulations! You've won {user_win_streak} times in a row! 🤩")
    print("-------------------\n")

def display_scoreboard(rounds_played, user_win_count, computer_win_count, hi_score):
    # Display the scoreboard with rounds played, wins, and best streak.
    print("\n------ Scoreboard ------")
    print(f"You have played a total of {rounds_played - 1} rounds")
    print(f"You won {user_win_count} times")
    print(f"The Computer won {computer_win_count} times")
    print(f"Your best streak is {hi_score}")
    print("-----------------------\n")

def read_int_from_file(filename, default=0):
    # Read an integer from a file, return default if error.
    try:
        with open(filename) as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return default

def write_int_to_file(filename, value):
    """Write an integer value to a file."""
    try:
        with open(filename, 'w') as f:
            f.write(str(value))
    except Exception as e:
        print(f"Error writing to {filename}: {e}")

def main():
    display_rules()
    user_win_count = 0
    computer_win_count = 0
    user_win_streak = 0
    round_number = 1
    best_streak = 0
    HIGH_SCORE_FILE = "highscore.txt"
    ROUNDS_FILE = "rounds.txt"
    high_score = read_int_from_file(HIGH_SCORE_FILE)
    rounds_played = read_int_from_file(ROUNDS_FILE)
    try:
        while True:
            computer_choice = select_computer_choice(CHOICES)
            user_choice = take_input_from_user()
            if user_choice == 'Help':
                help()
                continue
            if user_choice == 'Exit':
                confirm = input("Do you want to exit the game? [y/n] ").strip().lower()
                if confirm in ['y', 'yes', '1']:
                    write_int_to_file(ROUNDS_FILE, rounds_played + (round_number - 1))
                    print("Exiting...")
                    break
                else:
                    continue
            if user_choice == "Leaderboard":
                display_scoreboard(rounds_played + round_number - 1, user_win_count, computer_win_count, high_score)
                continue
            result = compute_result(user_choice, computer_choice)
            user_win_count, user_win_streak, computer_win_count = update_score(result, user_win_count, user_win_streak, computer_win_count)
            if user_win_streak > best_streak:
                best_streak = user_win_streak
            if user_win_streak > high_score and user_win_streak > 1:
                high_score = user_win_streak
                print(f"\nYou have set a new high streak of {high_score} wins!")
                write_int_to_file(HIGH_SCORE_FILE, high_score)
            print_result(result, round_number, user_choice, computer_choice, user_win_count, user_win_streak, getemoji(user_choice, computer_choice)[0], getemoji(user_choice, computer_choice)[1])
            round_number += 1
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
        write_int_to_file(ROUNDS_FILE, rounds_played + (round_number - 1))

if __name__ == "__main__":
    main()

