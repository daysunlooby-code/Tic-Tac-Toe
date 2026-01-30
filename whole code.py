import random


def get_user_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid input. Please try again.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"


def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("Computer chose:", computer_choice)

        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            print("You win!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")

        print("Score -> You:", user_score, "Computer:", computer_score)

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


play_game()

