
"""
Rock Paper Scissors Game

This is a command-line Python game where the user plays Rock, Paper, Scissors against the computer.
The computer randomly selects one of the three choices each round. The user enters their choice,
and the winner is determined by the classic rules. The game tracks the user's total wins and
consecutive win streaks, and allows the user to exit at any time.
"""

import random

CHOICES = ['Rock', 'Paper', 'Scissors']

def computer_choice(CHOICES):
    # Randomly select Rock, Paper, or Scissors for the computer
    computer = random.choice(CHOICES)
    return computer

def take_input_from_user():
    """Prompt the user for input until a valid choice is entered."""
    while True:
        user = input("Enter your choice: ").strip().lower()
        if user in ['rock', 'r']:
            return "Rock"
        elif user in ['paper', 'p']:
            return "Paper"
        elif user in ['scissors', 's']:
            return "Scissors"
        elif user in ['exit', 'e']:
            return "Exit"
        else:
            print("Invalid input. Please enter only 'Rock', 'Paper', or 'Scissors'.")

def compute_result(user, computer):
    # Determine the result of the round based on user and computer choices
    if (computer=="Rock"):
        if (user=="Paper"):
            result = "won"
        elif (user=="Rock"):
            result = "tie"
        else:
            result = "lost"
    elif (computer=="Paper"):
        if (user=="Paper"):
            result = "tie"
        elif (user=="Rock"):
            result = "lost"
        else:
            result = "won"
    else:
        if (user=="Paper"):
            result = "lost"
        elif (user=="Rock"):
            result = "won"
        else:
            result = "tie"
    return result

def update_score(result, user_win_count, user_win_streak):
    # Update win and streak counters based on the result
    if result == "won":
        user_win_count += 1
        user_win_streak += 1
    else:
        user_win_streak = 0
    return user_win_count, user_win_streak

def print_result(result, computer, user_win_count, user_win_streak):
    # Print the result of the round and display the current score
    if result == "won":
        print("You won!")
        print("Because the computer has chosen " + computer + ".")
    elif result == "tie":
        print("It's a tie!")
        print("Because the computer has also chosen " + computer + ".")
    else:
        print("You lost!")
        print("Because the computer has chosen " + computer + ".")
    print("Your Score is : ", user_win_count)

    # Print a message for consecutive wins
    if (user_win_streak >= 2):
        print(f"Hurray! You won {user_win_streak} times in a row.")
    print(" ")

def main():
    print(" ")
    print("This is a 'ROCK PAPER SCISSORS' game")
    print("You can enter 'R' for 'Rock', 'P' for 'Paper', and 'S' for 'Scissors'")
    print("You can exit the game by entering 'Exit'")
    print(" ")

    user_win_count = 0       # Number of times the user has won
    user_win_streak = 0      # Number of consecutive wins by the user

    while True:
        # Generate a random choice for the computer
        computer = computer_choice(CHOICES)

        # Take input from the user
        user = take_input_from_user()

        # Check if the user wants to exit the game
        if (user == 'Exit'):
            print("Exiting...")
            break

        # Determine the result of the round
        result = compute_result(user, computer)

        # Update win and streak counters
        user_win_count, user_win_streak = update_score(result, user_win_count, user_win_streak)

        # Print the result and current score
        print_result(result, computer, user_win_count, user_win_streak)

if __name__ == "__main__":
    main()