class PlayingCard:
    def __init__(self, suit, face):
        if suit not in ['H', 'D', 'C', 'S']:
            raise ValueError("Parameter suit must be one of H, D, C or S")
        if not (1 <= face <= 13):
            raise ValueError("Parameter face must be a number between 1 to 13")
        
        self.suit = suit
        self.face = face

    def get_as_string(self):
        return f"{self.suit}{self.face}"

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.face

    def __eq__(self, other):
        if isinstance(other, PlayingCard):
            return self.suit == other.suit and self.face == other.face
        return False

    def __hash__(self):
        return hash((self.suit, self.face))