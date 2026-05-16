"""Entry point for the Snowman Meltdown game."""
from game_logic import play_game

def main():
    """Main function to run the Snowman Meltdown game loop with replay option."""
    keep_playing = True
    while keep_playing:
        play_game()
        print()

        while True:
            response = input("Would you like to play again? (y/n): ").lower()

            if response == "y":
                break

            if response == "n":
                print("Good Bye!")
                return

            print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()