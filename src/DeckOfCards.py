from PlayingCard import PlayingCard
from HandOfCards import HandOfCards
import random


class DeckOfCards:
    def __init__(self):
        suits = ['S', 'H', 'D', 'C']
        self.cards = [PlayingCard(suit, face) for suit in suits for face in range(1, 14)]

    def deal_hand(self, n):
        if not (1 <= n <= 52):
            raise ValueError("Parameter n must be a number between 1 and 52")
        hand_cards = random.sample(self.cards, n)
        return HandOfCards(hand_cards)


    def __str__(self):
        return ', '.join(card.get_as_string() for card in self.cards)
