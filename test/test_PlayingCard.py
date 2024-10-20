import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):

    def test_valid_card(self):
        card = PlayingCard('H', 5)
        self.assertEqual(card.get_suit(), 'H')
        self.assertEqual(card.get_face(), 5)
        self.assertEqual(card.get_as_string(), 'H5')

    def test_invalid_suit(self):
        with self.assertRaises(ValueError) as context:
            PlayingCard('X', 5)
        self.assertEqual(str(context.exception), "Parameter suit must be one of H, D, C or S")

    def test_invalid_face(self):
        with self.assertRaises(ValueError) as context:
            PlayingCard('H', 0)
        self.assertEqual(str(context.exception), "Parameter face must be a number between 1 to 13")

        with self.assertRaises(ValueError) as context:
            PlayingCard('H', 14)
        self.assertEqual(str(context.exception), "Parameter face must be a number between 1 to 13")

    def test_equality(self):
        card1 = PlayingCard('H', 5)
        card2 = PlayingCard('H', 5)
        card3 = PlayingCard('D', 5)
        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)

    def test_hash(self):
        card1 = PlayingCard('H', 5)
        card2 = PlayingCard('H', 5)
        card3 = PlayingCard('D', 5)
        self.assertEqual(hash(card1), hash(card2))
        self.assertNotEqual(hash(card1), hash(card3))

if __name__ == '__main__':
    unittest.main()