class Joueur:
    """Represent a player in the guessing game."""

    def __init__(self, name="Joueur 1"):
        # Basic player information
        self.name = name
        self.score = 100

    def make_a_proposal(self, prompt=None):
        """Ask the player for a valid integer guess."""
        while True:
            try:
                value = input(prompt or f"Please {self.name}, enter your guess: ")
                return int(value)
            except ValueError:
                print("Please enter a valid integer.")
