import unittest
from unittest.mock import patch

from Joueur import Joueur
from JeuDevinette import JeuDevinette


class GuessingGameTests(unittest.TestCase):
    def test_player_proposal_reads_integer(self):
        player = Joueur("Alice")
        with patch("builtins.input", return_value="7"):
            self.assertEqual(player.make_a_proposal(), 7)

    def test_game_accepts_a_secret_number_and_wins(self):
        player = Joueur("Bob")
        game = JeuDevinette(player, min_value=0, max_value=10, max_attempts=3)
        game._JeuDevinette__number_secret = 5

        self.assertEqual(game.verifier_coup(5), "win")
        self.assertTrue(game.partie_terminee)

    def test_game_reduces_attempts_and_reports_too_low(self):
        player = Joueur("Charlie")
        game = JeuDevinette(player, min_value=0, max_value=10, max_attempts=3)
        game._JeuDevinette__number_secret = 8

        result = game.verifier_coup(3)

        self.assertEqual(result, "too_low")
        self.assertEqual(game.tentatives_restantes, 2)


if __name__ == "__main__":
    unittest.main()

