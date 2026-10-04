import random


class JeuDevinette:
    """Main game logic for the number guessing game."""

    def __init__(
        self,
        joueur,
        max_iter=5,
        min_value=0,
        max_value=10,
        max_attempts=None,
    ):
        # Keep compatibility with the original constructor style while allowing
        # the game to configure its range and number of attempts.
        if max_attempts is None:
            max_attempts = max_iter

        self.__number_secret = random.randint(min_value, max_value)
        self.min_value = min_value
        self.max_value = max_value
        self.max_attempts = max_attempts
        self.tentatives_restantes = max_attempts
        self.partie_terminee = False
        self.joueur = joueur
        self.message = ""

    def verifier_coup(self, proposal=None):
        """Check a guess and return the result status."""
        if proposal is None:
            proposal = self.joueur.make_a_proposal()

        if proposal < self.min_value or proposal > self.max_value:
            self.message = (
                f"Please choose a number between {self.min_value} and {self.max_value}."
            )
            return "invalid"

        if proposal == self.__number_secret:
            self.partie_terminee = True
            self.message = (
                f"Congratulations {self.joueur.name}! "
                f"You found the secret number: {self.__number_secret}."
            )
            return "win"

        self.tentatives_restantes -= 1

        if proposal < self.__number_secret:
            self.message = "Too low! Try a higher number."
        else:
            self.message = "Too high! Try a lower number."

        if self.tentatives_restantes == 0:
            self.partie_terminee = True
            self.message = (
                f"Game over! The secret number was {self.__number_secret}. "
                f"You used all your attempts."
            )
            return "lost"

        return "too_low" if proposal < self.__number_secret else "too_high"

    def lancer(self):
        """Run the game loop until the player wins or loses."""
        print(f"\nWelcome {self.joueur.name}!")
        print(
            f"I picked a number between {self.min_value} and {self.max_value}. "
            f"You have {self.tentatives_restantes} attempts."
        )

        while not self.partie_terminee and self.tentatives_restantes > 0:
            print(f"\nAttempts left: {self.tentatives_restantes}")
            guess = self.joueur.make_a_proposal()
            result = self.verifier_coup(guess)

            if result == "win":
                print(self.message)
                return True

            if result == "invalid":
                print(self.message)
                continue

            print(self.message)

            if self.tentatives_restantes == 0:
                print(f"\nGame over! The secret number was {self.__number_secret}.")
                return False

        if self.partie_terminee and self.tentatives_restantes > 0:
            print(self.message)
            return True

        print(f"\nGame over! The secret number was {self.__number_secret}.")
        return False
