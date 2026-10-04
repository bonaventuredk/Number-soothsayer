from JeuDevinette import JeuDevinette
from Joueur import Joueur


def main():
    """Start the number guessing game."""
    print("Welcome to the Number Guessing Game!")

    player_name = input("Enter your name: ").strip() or "Player 1"
    player = Joueur(player_name)

    game = JeuDevinette(player, min_value=0, max_value=10, max_attempts=5)
    game.lancer()


if __name__ == "__main__":
    main()
