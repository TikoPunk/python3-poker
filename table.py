class Table(object):
    def __init__(self):
        self.bet = 0
        self.cards = []

    def setBet(self, newBet):
        self.bet = newBet

    def getBet(self):
        return self.bet

    def setCards(self, newCards):
        self.cards.extend(newCards)

    def getCards(self):
        print("\nTable has")
        if (len(self.cards) <= 0):
            print("No Cards")
        else:
            for c in self.cards:
                print(c.getNumber(), c.getSuit())
