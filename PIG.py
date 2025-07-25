# PIG Game
import random

def roll():
    return random.randint(1, 6)

# Get number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4!")
    else:
        print("Invalid input!")

# Initialize scores
max_score = 50
players_score = [0 for _ in range(players)]

# Main game loop
while max(players_score) < max_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn:")
        print(f"Your total score is: {players_score[player_index]}\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll? (y): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            print(f"You rolled a {value} 🎲")

            if value == 1:
                print("You rolled a 1! Your turn's over 😢")
                current_score = 0
                break
            else:
                current_score += value
                print(f"Current turn score: {current_score}")

        # Update total score after turn
        players_score[player_index] += current_score
        print(f"Your total score is: {players_score[player_index]}")

        if players_score[player_index] >= max_score:
            break

# Announce winner
max_score = max(players_score)
winning_index = players_score.index(max_score)
print(f"\n🎉 Player {winning_index + 1} is the winner with a score of {max_score}! 🎉")
