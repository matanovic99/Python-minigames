import random

print("Welcome to Rock, Paper, Scissors game!\n")
moves = ["rock", "paper", "scissors"]

def get_user_move():
    while True:
        move = input("Enter your move (rock/paper/scissors): ")
        if move.lower() in moves:
            return move.lower()
        else:
            print("Invalid move. Please try again.\n")
def get_computer_move():
    return random.choice(moves)
def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "tie"
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        return "user"
    else:
        return "computer"
while True:
    user_move = get_user_move()
    computer_move = get_computer_move()
    winner = determine_winner(user_move, computer_move)
    
    print(f"\nYou chose {user_move}. The computer chose {computer_move}.\n")
    
    if winner == "tie":
        print("It's a tie!\n")
    else:
        print(f"{winner.capitalize()} wins!\n")
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("\nThanks for playing Rock, Paper, Scissors!")
