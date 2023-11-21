import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    total_rounds = 0
    
    while True:
        print("Enter your choice: rock, paper, or scissors (or 'exit' to quit)")
        player_input = input().lower()
        
        if player_input == 'exit':
            break
        
        if player_input not in options:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(options)
        
        result = determine_winner(player_input, computer_choice)
        print(f"Player: {player_input.capitalize()}, Computer: {computer_choice.capitalize()}. {result}")
        
        if result == "You win!":
            player_score += 1
        
        total_rounds += 1
    
    print(f"Game ended! Your score: {player_score}/{total_rounds}.")

if __name__ == "__main__":
    play_game()
