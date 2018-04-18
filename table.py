class Table(object):
    def __init__(self):
        self.bet = 0
        self.cards = []

    def getCards(self):
        print("\nTable has")
        if (len(self.cards) <= 0):
            print("No Cards")
        else:
            for c in self.cards:
                print(c.number, c.suit)
