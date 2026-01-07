"""Rock, paper, scissors game"""

import random

CHOICES = ["Rock", "Paper", "Scissors"]

# Each choice beats the choice at index (i - 1), i.e., Rock beats Scissors, etc.
BEATS = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}


def get_bio_choice():
    """Get and validate human player's choice."""
    while True:
        try:
            choice = int(
                input("Select 0 (Rock), 1 (Paper), or 2 (Scissors): "))
            if choice in (0, 1, 2):
                return CHOICES[choice]
            print("Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_round(bio_choice, gpu_choice):
    """Determine round winner. Returns 1 for win, -1 for loss, 0 for tie."""
    if bio_choice == gpu_choice:
        return 0
    return 1 if BEATS[bio_choice] == gpu_choice else -1


def play_game(rounds=5):
    """Play a complete game of Rock-Paper-Scissors."""
    bio_score = 0
    gpu_score = 0

    for round_num in range(1, rounds + 1):
        bio_choice = get_bio_choice()
        gpu_choice = random.choice(CHOICES)
        result = play_round(bio_choice, gpu_choice)

        bio_score += result == 1
        gpu_score += result == -1

        result_messages = {
            1: f"You win! {bio_choice} beats {gpu_choice}",
            -1: f"You lose! {gpu_choice} beats {bio_choice}",
            0: "It's a tie!"
        }

        print(
            f"\nRound {round_num}: You ({bio_choice}) vs Computer ({gpu_choice})")
        print(result_messages[result])
        print(f"Score: You {bio_score} - Computer {gpu_score}")
        print("-" * 30)

    # Final result
    print("\n*** FINAL RESULT ***")
    if bio_score != gpu_score:
        winner = "You win" if bio_score > gpu_score else "Computer wins"
        print(f"{winner}! Final: You {bio_score} - Computer {gpu_score}")
    else:
        print(f"It's a tie! Final: {bio_score} - {gpu_score}")


if __name__ == "__main__":
    play_game()
# End-of-file (EOF)
