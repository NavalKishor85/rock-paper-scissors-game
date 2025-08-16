import random

# Rock Paper Scissors Game
# The computer randomly selects one of the three choices: Rock, Paper, or Scissors.
# The user is prompted to enter their choice.
# The winner is determined based on the classic rules of the game.

print(" ")
print("This is a 'ROCK PAPER SCISSORS' game")
print("You can enter 'R' for 'Rock', 'P' for 'Paper', and 'S' for 'Scissors'")
print("You can exit the game by entering 'Exit'")
print(" ")

ROUNDS_WIN = 0  # Number of times the user has won
STRIKE = 0      # Number of consecutive wins by the user

def computer_choice():
    # Randomly select Rock, Paper, or Scissors for the computer
    choice_list = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(choice_list)
    return computer

def take_input_from_user():
    # Prompt the user for input until a valid choice is entered
    while True:
        user = input("Enter your choice: ")
        if (user == "rock" or user == "Rock") or (user == 'R' or user == 'r'):
            user = "Rock"
            break
        elif (user == "paper" or user == "Paper") or (user == 'P' or user == 'p'):
            user = "Paper"
            break
        elif (user == "scissors" or user == "Scissors") or (user == 'S' or user == 's'):
            user = "Scissors"
            break
        elif (user == 'exit' or user == 'Exit'):
            user = 'Exit'
            break
        else:
            user = input("Invalid input. Please enter only 'Rock', 'Paper', or 'Scissors': ")
    return user

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

def counts_win(result, ROUNDS_WIN, STRIKE):
    # Update win and streak counters based on the result
    if result == "won":
        ROUNDS_WIN += 1
        STRIKE += 1
    elif result == "tie":
        STRIKE = 0
    else:
        STRIKE = 0
    return ROUNDS_WIN, STRIKE

def print_result(result, ROUNDS_WIN, STRIKE, computer):
    # Print the result of the round and display the current score and streak
    if result == "won":
        print("You won!")
        print("Because the computer has chosen " + computer + ".")
    elif result == "tie":
        print("It's a tie!")
        print("Because the computer has also chosen " + computer + ".")
    else:
        print("You lost!")
        print("Because the computer has chosen " + computer + ".")
    
    print("Your Score is : ", ROUNDS_WIN)

    if (STRIKE >= 2):
        print("Hurray! You won ", STRIKE, "times in a row.")
    print(" ")

while True:
    # Generate a random choice for the computer
    computer = computer_choice()

    # Take input from the user
    user = take_input_from_user()

    # Check if the user wants to exit the game
    if (user == 'Exit'):
        print("Exiting...")
        break

    # Determine the result of the round
    result = compute_result(user, computer)

    # Update win and streak counters
    win_result_counts = counts_win(result, ROUNDS_WIN, STRIKE)

    ROUNDS_WIN = win_result_counts[0]
    STRIKE = win_result_counts[1]

    # Print the result and current score
    print_result(result, ROUNDS_WIN, STRIKE, computer)