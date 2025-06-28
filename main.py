import random

#This is a Rock, Paper, Scissors game
#First computer will select one of the three choices
#Then we take input from the user
#Then we check who wins
print(" ")
print("This is ROCK PAPER SCISSORS game")
print("You have three choices 'Rock', 'Paper', 'Scissors'.")
print("You can Exit By Entering 'Exit'.")
print(" ")

ROUNDS_WIN = 0 #how many times user won
STRIKE = 0 #how many times user won in a row

def computer_choice():
    # Randomly select Rock, Paper, or Scissors for the computer
    random_number = random.randint(1,3)
    if (random_number==1):
        computer = "Rock"
    elif (random_number==2):
        computer = "Paper"
    else:
        computer = "Scissors"
    return computer

def take_input_from_user():
    # Take input from user and validate it
    user = input("Enter your choice : ")
    if (user=="rock" or user=="Rock"):
        user = "Rock"
    elif (user=="paper" or user=="Paper"):
        user = "Paper"
    elif (user=="scissors" or user=="Scissors"):
        user = "Scissors"
    else:
        user = input("Enter only 'Rock', 'Paper' and 'Scissors': ")
    return user

def compute_result(user, computer):
    # Compute the result of the game based on user and computer choices
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
    # Update win and strike counters based on result
    if result == "won":
        ROUNDS_WIN += 1
        STRIKE += 1
    elif result == "tie":
        STRIKE = 0
    else:
        STRIKE = 0
    return ROUNDS_WIN, STRIKE

def print_result(result, ROUNDS_WIN, STRIKE, computer):
    # Print the result of the round and current scores
    if result == "won":
        print("You won!")
        print("Your Score is : ", ROUNDS_WIN)
    elif result == "tie":
        print("It's a tie!")
        print("Your Score is : ", ROUNDS_WIN)
    else:
        print("You lost!")
        print("Your Score is : ", ROUNDS_WIN)
    if STRIKE >= 2:
        print("Hurray! You won ", STRIKE, "times in a row.")
    print("Because the computer has chosen " + computer + ".")
    print(" ")

while True:
    # Generate random choice between Rock, Paper, Scissors
    computer = computer_choice()

    # take input 
    user = take_input_from_user()

    # calculate result 
    result = compute_result(user, computer)

    # count how many times user wins
    # Strike is a count when user wins in a row, rest to 0 if user lost or it is a tie
    win_result_counts = counts_win(result, ROUNDS_WIN, STRIKE)

    ROUNDS_WIN = win_result_counts[0]
    STRIKE = win_result_counts[1]

    # Print Result and tell your score
    print_result(result, ROUNDS_WIN, STRIKE, computer)