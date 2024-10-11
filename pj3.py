import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Enter rock, paper, or scissors: ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        print("Invalid input. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Result: {result}\n")

def play_again():
    while True:
        play_again_choice = input("Do you want to play again? (yes/no): ").lower()
        if play_again_choice in ['yes', 'no']:
            return play_again_choice == 'yes'
        print("Invalid input. Please enter 'yes' or 'no'.")

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Rock beats scissors, scissors beat paper, and paper beats rock.\n")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        if not play_again():
            print("\nThank you for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

if __name__ == "__main__":
    rock_paper_scissors_game()
