
class Player(object):
    def __init__(self, newName, newMoney):
        self.name = newName
        self.money = newMoney
        self.bet = 0
        self.In = True
        self.dead = False
        self.cards = []

    def get_cards(self):
        print("\n", self.name, "has", len(self.cards), "cards\n")
        for c in self.cards:
            print(c.number, c.suit)
