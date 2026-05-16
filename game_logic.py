"""Module containing the core game logic for Snowman Meltdown."""
import random

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS).lower()


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current state of the game including the snowman and the word progress.
    """
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)

    return display_word


def play_game():
    """Starts and manages a single session of the Snowman Meltdown game."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = ""
        while not (len(guess) == 1 and guess.isalpha()):
            guess = input("Guess a letter: ").lower()
            if not (len(guess) == 1 and guess.isalpha()):
                print("Please enter a single alphabetical letter.")

        if guess in secret_word and guess not in guessed_letters:
            guessed_letters.append(guess)

        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        else:
            mistakes += 1

        if mistakes == 3:
            print(f"Game Over! The word was: {secret_word}")
            break

        current_state = display_game_state(mistakes, secret_word, guessed_letters)

        if '_' not in current_state:
            print("Congratulations, you saved the snowman!")
            break

    return


