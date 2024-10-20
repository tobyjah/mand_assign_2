import unittest
import sys, os

# Add the parent directory of 'notebooks' to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))


from DeckOfCards import DeckOfCards
from HandOfCards import HandOfCards

class TestDeckOfCards(unittest.TestCase):

    def setUp(self):
        self.deck = DeckOfCards()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52)
        suits = ['S', 'H', 'D', 'C']
        faces = list(range(1, 14))
        for card in self.deck.cards:
            self.assertIn(card.suit, suits)
            self.assertIn(card.face, faces)

    def test_deal_hand_valid(self):
        hand = self.deck.deal_hand(5)
        self.assertIsInstance(hand, HandOfCards)
        self.assertEqual(len(hand.cards), 5)

    def test_deal_hand_invalid(self):
        with self.assertRaises(ValueError):
            self.deck.deal_hand(0)
        with self.assertRaises(ValueError):
            self.deck.deal_hand(53)

    def test_str_method(self):
        deck_str = str(self.deck)
        self.assertIsInstance(deck_str, str)
        self.assertEqual(len(deck_str.split(', ')), 52)

if __name__ == '__main__':
    unittest.main()