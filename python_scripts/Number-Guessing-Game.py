"""
Number Guessing Game
---------------------
The computer picks a random number between 1 and 100.
The player has to guess it, receiving "too high / too low" 
hints until they get it right.

Concepts covered: random module, while loops, if/elif/else, 
try/except for input validation, functions.
"""


import random

def get_guess():
    """Keep asking until the player types a valid whole number."""
    while True:
        raw = input("Your guess: ")
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number, like 42.")

def play_round():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"You got it! The number was {secret_number}.")
            print(f"It took you {attempts} attempt(s).\n")
            break

def main():
    print("=== Number Guessing Game ===")
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()