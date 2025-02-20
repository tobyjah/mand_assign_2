import unittest
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../src')))

from DeckOfCards import DeckOfCards
from HandOfCards import HandOfCards
from PlayingCard import PlayingCard

class TestDeckOfCards(unittest.TestCase):
    def test_construct(self):
        deck = DeckOfCards()
        self.assertEqual(len(deck.cards), 52)

    def test_deal_hand(self):
        deck = DeckOfCards()
        
        hand = deck.deal_hand(5)
        self.assertEqual(len(hand.cards), 5)

        self.assertRaises(ValueError, deck.deal_hand, 53)
        self.assertRaises(ValueError, deck.deal_hand, 0)

    def test_str(self):
        self.assertEqual(str(DeckOfCards()), 'S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13')


# class TestCard(unittest.TestCase):
#     def test_card(self):
#         self.assertEqual(1,  1)

# class TestHandOfCards(unittest.TestCase):
#     def test_hand_of_cards(self):
#         self.assertEqual(1, 1)


unittest.main()