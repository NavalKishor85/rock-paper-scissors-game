def main():
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

    rounds_win = 0  # Number of times the user has won
    strike = 0      # Number of consecutive wins by the user

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
                print("Invalid input. Please enter only 'Rock', 'Paper', or 'Scissors'.")
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

    def update_score(result, rounds_win, strike):
        # Update win and streak counters based on the result
        if result == "won":
            rounds_win += 1
            strike += 1
        else:
            strike = 0
        return rounds_win, strike

    def print_result(result, computer, rounds_win, strike):
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
        print("Your Score is : ", rounds_win)
        if (strike >= 2):
            print(f"Hurray! You won {strike} times in a row.")
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
        rounds_win, strike = update_score(result, rounds_win, strike)

        # Print the result and current score
        print_result(result, computer, rounds_win, strike)

if __name__ == "__main__":
    main()