import unittest

import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
    
from HandOfCards import HandOfCards
from PlayingCard import PlayingCard

class TestHandOfCards(unittest.TestCase):
    def test_is_flush_true(self):
        cards = [
            PlayingCard('H', 2),
            PlayingCard('H', 3),
            PlayingCard('H', 4),
            PlayingCard('H', 5),
            PlayingCard('H', 6)
        ]
        hand = HandOfCards(cards)
        self.assertTrue(hand.is_flush())

    def test_is_flush_false(self):
        cards = [
            PlayingCard('H', 2),
            PlayingCard('H', 3),
            PlayingCard('H', 4),
            PlayingCard('H', 5),
            PlayingCard('D', 6)
        ]
        hand = HandOfCards(cards)
        self.assertFalse(hand.is_flush())

    def test_is_flush_not_enough_cards(self):
        cards = [
            PlayingCard('H', 2),
            PlayingCard('H', 3),
            PlayingCard('H', 4),
            PlayingCard('H', 5)
        ]
        hand = HandOfCards(cards)
        self.assertFalse(hand.is_flush())

    def test_str(self):
        cards = [
            PlayingCard('H', 2),
            PlayingCard('D', 3),
            PlayingCard('C', 4),
            PlayingCard('S', 5),
            PlayingCard('H', 6)
        ]
        hand = HandOfCards(cards)
        self.assertEqual(str(hand), 'H2, D3, C4, S5, H6')

if __name__ == '__main__':
    unittest.main()