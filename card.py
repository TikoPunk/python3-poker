class Card(object):
    def __init__(self, newNumber, newSuit):
        self.number = newNumber
        self.suit = newSuit

    def getNumber(self):
        return self.number

    def getSuit(self):
        return self.suit
