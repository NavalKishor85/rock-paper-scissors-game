"""
----Rock Paper Scissors Game----
Command-line game: user vs computer. Computer randomly picks Rock, Paper, or Scissors. User enters choice. Winner is decided by classic rules. Tracks total wins and win streaks. User can exit anytime."""
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
    # Prompt user until a valid choice is entered
    while True:
        user_input = input("Enter your choice: ").strip().lower()
        if user_input == '':
            print("You entered nothing. Please enter 'Rock', 'Paper', or 'Scissors'")
            continue
        if user_input in ['rock', 'r']:
            return "Rock"
        elif user_input in ['paper', 'p', 'PAPER']:
            return "Paper"
        elif user_input in ['scissors', 's', 'SCISSORS']:
            return "Scissors"
        elif user_input in ['exit', 'e', 'EXIT']:
            return "Exit"
        elif user_input in ['help', 'h', 'HELP']:
            return "Help"
        elif user_input in ['leaderboard', 'l', 'LEADERBOARD']:
            return "leaderboard"
        else:
            print("Invalid input. Please enter only 'Rock', 'Paper', or 'Scissors'.")

def compute_result(user_choice, computer_choice):
    # Determine round result
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

def update_score(result, user_win_count, user_win_streak, computer_win_count):
    # Update win and streak counters
    if result == "won":
        user_win_count += 1
        user_win_streak += 1
    elif result == "lost":
        user_win_streak = 0
        computer_win_count += 1
    else:
        user_win_streak = 0
    return user_win_count, user_win_streak, computer_win_count

def print_result(result, round_number, user_choice, computer_choice, user_win_count, user_win_streak):
    # Print round number, choices, result, and current score
    print(f"\n----- Round {round_number} -----")
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
        print(f"Congratulations! You've won {user_win_streak} times in a row!")
    print("-------------------\n")

def display_scoreboard(round_number, user_win_count, computer_win_count, best_streak):
    print("\n------ Scoreboard ------")
    print(f"You have played total {round_number - 1} rounds")
    print(f"You won {user_win_count} times")
    print(f"The Computer won {computer_win_count} times")
    print(f"Your best streak is of {best_streak}")
    print("-----------------------\n")

def main():

    display_rules()

    user_win_count = 0       # Number of times the user has won
    computer_win_count = 0   # Number of times the computer has won
    user_win_streak = 0      # Number of consecutive wins by the user
    round_number = 1         # Round counter
    best_streak = 0          # Best score in consecutive wins by user

    while True:
        # Generate a random choice for the computer
        computer_choice = select_computer_choice(CHOICES)

        # Take input from the user
        user_choice = take_input_from_user()

        # Call help if user requests it
        if user_choice == 'Help':
            help()
            continue
        
        # Check if the user wants to exit the game
        if (user_choice == 'Exit'):
            confirm = input("Do you want to exit the game? [y/n] ").strip().lower()
            if confirm in ['y', 'yes', '1']:
                print("Exiting...")
                break
            else:
                continue

        # Display user score 
        if (user_choice == "leaderboard"):
            display_scoreboard(round_number, user_win_count, computer_win_count, best_streak)
            continue

        # Determine the result of the round
        result = compute_result(user_choice, computer_choice)

        # Update win and streak counters
        user_win_count, user_win_streak, computer_win_count  = update_score(result, user_win_count, user_win_streak, computer_win_count)

        # Save highest streak of user
        if (user_win_streak >= best_streak):
            best_streak = user_win_streak

        # Print the result and current score, including round and choices
        print_result(result, round_number, user_choice, computer_choice, user_win_count, user_win_streak)

        # Increament round
        round_number += 1

if __name__ == "__main__":
    main()

