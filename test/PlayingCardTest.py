import unittest
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../src')))

from PlayingCard import PlayingCard

class TestDeckOfCards(unittest.TestCase):
    def test_construct(self):
        ace_heart = PlayingCard('H', 1)
        ace_spade = PlayingCard('S', 1)
        ace_diamond = PlayingCard('D', 1)
        ace_club = PlayingCard('C', 1)

        self.assertEqual(ace_heart.suit, 'H')
        self.assertEqual(ace_heart.face, 1)

        self.assertEqual(ace_spade.suit, 'S')
        self.assertEqual(ace_spade.face, 1)

        self.assertEqual(ace_diamond.suit, 'D')
        self.assertEqual(ace_diamond.face, 1)

        self.assertEqual(ace_club.suit, 'C')
        self.assertEqual(ace_club.face, 1)

        self.assertRaises(ValueError, PlayingCard, 'X', 1)
        self.assertRaises(ValueError, PlayingCard, 'H', 0)
        self.assertRaises(ValueError, PlayingCard, 'H', 14)

    def test_get_as_string(self):
        card = PlayingCard('H', 1)
        self.assertEqual(card.get_as_string(), 'H1')

        card = PlayingCard('S', 10)
        self.assertEqual(card.get_as_string(), 'S10')

        card = PlayingCard('D', 11)
        self.assertEqual(card.get_as_string(), 'D11')

        card = PlayingCard('C', 5)
        self.assertEqual(card.get_as_string(), 'C5')

    def test_getters(self):
        card = PlayingCard('H', 1)
        self.assertEqual(card.get_suit(), 'H')
        self.assertEqual(card.get_face(), 1)

        card = PlayingCard('S', 10)
        self.assertEqual(card.get_suit(), 'S')
        self.assertEqual(card.get_face(), 10)

        card = PlayingCard('D', 11)
        self.assertEqual(card.get_suit(), 'D')
        self.assertEqual(card.get_face(), 11)

        card = PlayingCard('C', 5)
        self.assertEqual(card.get_suit(), 'C')
        self.assertEqual(card.get_face(), 5)

    def test_equality(self):
        card1 = PlayingCard('H', 1)
        card2 = PlayingCard('H', 1)

        self.assertEqual(card1, card2)

        card1 = PlayingCard('S', 10)
        card2 = PlayingCard('D', 10)

        self.assertNotEqual(card1, card2)

        card1 = PlayingCard('C', 6)
        card2 = PlayingCard('C', 5)

        self.assertNotEqual(card1, card2)

unittest.main()