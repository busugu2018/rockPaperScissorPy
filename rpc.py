import random

def playGame():
    options = ["rock", "paper", "scissor"]

    print("Welcome to rock, paper, scissors.")
    print("Type 'x' to quit the game.\n")

    while True:
        user_choice = input("Choose Rock, Paper, or scissor: ").lower()

        if user_choice == "x":
            print("Thanks for playing, bye.")
            break
        
        if user_choice not in options:
            print("Invalid choice! Please try again.\n")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!\n")
        else:
            print("Computer wins!\n")

if __name__ == "__main__":
    playGame()