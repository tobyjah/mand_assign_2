class HandOfCards:
    def __init__(self, cards):
        self.cards = cards

    def is_flush(self):
        if len(self.cards) < 5:
            return False
        first_suit = self.cards[0].get_suit()
        return all(card.get_suit() == first_suit for card in self.cards)

    def __str__(self):
        return ', '.join(card.get_as_string() for card in self.cards)
