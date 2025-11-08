"""
Rock Paper Scissors Game
------------------------
A simple Python command-line game where the player competes against the computer.

Author: Nick F.
GitHub: https://github.com/nfava
"""

import random

def get_user_choice() -> str:
    """Prompt the user to enter rock, paper, or scissors"""
    choices = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if user_input in choices:
            return user_input
        print("Invalid choice. Please try again.")


def get_computer_choice() -> str:
    """Randomly select the computer's choice."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user: str, computer: str) -> str:
    """Determine the winner of the game."""
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_round() -> None:
    """Play a single round of Rock Paper Scissors"""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

def main() -> None:
    """Main function to run the Rock Paper Scissors game"""
    print("Welcome to Rock Paper Scissors!")
    while True:
        play_round()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()



