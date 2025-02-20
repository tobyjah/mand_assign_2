import unittest
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../src')))

from HandOfCards import HandOfCards
from PlayingCard import PlayingCard

class TestHandOfCards(unittest.TestCase):
    def test_construct(self):
        hand = HandOfCards([
            PlayingCard('H', 1),
            PlayingCard('D', 1),

        ])
        self.assertEqual(len(hand.cards), 2)

    def test_deal_hand(self):
        deck = HandOfCards([
            PlayingCard('H', 1),
            PlayingCard('D', 1),
            PlayingCard('C', 1),
            PlayingCard('S', 1)
        ])

        self.assertEqual(len(deck.cards), 4)

    def test_is_flush(self):
        hand = HandOfCards([
            PlayingCard('H', 1),
            PlayingCard('H', 2),
            PlayingCard('H', 3),
            # PlayingCard('H', 4),
            # PlayingCard('H', 5)
        ])

        self.assertFalse(hand.is_flush())

        hand.cards.append(PlayingCard('H', 4))
        hand.cards.append(PlayingCard('H', 5))

        self.assertTrue(hand.is_flush())

        hand = HandOfCards([
            PlayingCard('H', 1),
            PlayingCard('H', 2),
            PlayingCard('D', 3),
            PlayingCard('H', 4),
            PlayingCard('H', 5)
        ])

        self.assertFalse(hand.is_flush())

    def test_str(self):

        hand = HandOfCards( [
            PlayingCard('H', 1),
            PlayingCard('D', 2)
        ])

        self.assertEqual(str(hand), 'H1, D2')

unittest.main()