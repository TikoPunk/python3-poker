
class Player(object):
    def __init__(self, newName, newMoney):
        self.name = newName
        self.money = newMoney
        self.bet = 0
        self.In = True
        self.dead = False
        self.cards = []

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def setBet(self, bet):
        self.bet = bet

    def getBet(self):
        if self.In is False:
            return "Is Out"

        return self.bet

    def setIn(self, bool):
        self.In = bool

    def getIn(self):
        return self.In

    def setDead(self, bool):
        self.dead = bool

    def getDead(self):
        return self.dead

    def setCards(self, card):
        self.cards.extend(card)

    def getCards(self):
        print("\n", self.getName(), "has", len(self.cards), "cards\n")
        for c in self.cards:
            print(c.getNumber(), c.getSuit())

    def setIntoTrue(self):
        self.In = True
