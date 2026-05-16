import random


WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = {
      0:
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
      1:
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
      2:
     """
      ___  
     /___\\ 
     (o o) 
     """,
      3:
     """
      ___  
     /___\\ 
     """
}


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)

    mistakes = 0
    guessed_letters = []

    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)

    display_game_state(mistakes, secret_word, guessed_letters)


if __name__ == "__main__":
    play_game()