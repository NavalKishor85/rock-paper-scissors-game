"""
Rock Paper Scissors Game

Command-line game: user vs computer. Computer randomly picks Rock, Paper, or Scissors. User enters choice. Winner is decided by classic rules. Tracks total wins and win streaks. User can exit anytime.
"""

import random

CHOICES = ['Rock', 'Paper', 'Scissors']

def display_rules():
    """Display the game rules and instructions."""
    print("\nWelcome to 'ROCK PAPER SCISSORS'!")
    print("Rules:")
    print("- Rock beats Scissors")
    print("- Paper beats Rock")
    print("- Scissors beats Paper")
    print("Instructions:")
    print("- You can also enter 'R' for Rock, 'P' for Paper, 'S' for Scissors")
    print("- Enter 'Exit' at any time to quit the game\n")

def select_computer_choice(CHOICES):
    # Randomly select a choice for the computer
    computer_choice = random.choice(CHOICES)
    return computer_choice

def take_input_from_user():
    """Prompt user until a valid choice is entered."""
    while True:
        user_input = input("Enter your choice: ").strip().lower()
        if user_input == '':
            print("You entered nothing. Please enter 'Rock', 'Paper', or 'Scissors'.")
            continue
        if user_input in ['rock', 'r']:
            return "Rock"
        elif user_input in ['paper', 'p']:
            return "Paper"
        elif user_input in ['scissors', 's']:
            return "Scissors"
        elif user_input in ['exit', 'e']:
            return "Exit"
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

def update_score(result, user_win_count, user_win_streak):
    # Update win and streak counters
    if result == "won":
        user_win_count += 1
        user_win_streak += 1
    else:
        user_win_streak = 0
    return user_win_count, user_win_streak

def print_result(result, round_number, user_choice, computer_choice, user_win_count, user_win_streak):
    # Print round number, choices, result, and current score
    print(f"\n--- Round {round_number} ---")
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "won":
        print("You won!")
    elif result == "tie":
        print("It's a tie!")
    else:
        print("You lost!")
    print(f"Your score is: {user_win_count}")

    # Print message for win streak
    if user_win_streak >= 2:
        print(f"Congratulations! You've won {user_win_streak} times in a row!")
    print(" ")

def main():
    display_rules()

    user_win_count = 0       # Number of times the user has won
    user_win_streak = 0      # Number of consecutive wins by the user
    round_number = 1         # Round counter

    while True:
        # Generate a random choice for the computer
        computer_choice = select_computer_choice(CHOICES)

        # Take input from the user
        user_choice = take_input_from_user()

        # Check if the user wants to exit the game
        if (user_choice == 'Exit'):
            print("Exiting...")
            break

        # Determine the result of the round
        result = compute_result(user_choice, computer_choice)

        # Update win and streak counters
        user_win_count, user_win_streak = update_score(result, user_win_count, user_win_streak)

        # Print the result and current score, including round and choices
        print_result(result, round_number, user_choice, computer_choice, user_win_count, user_win_streak)

        round_number += 1

if __name__ == "__main__":
    main()