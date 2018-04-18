
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


class Card(object):
    def __init__(self, newNumber, newSuit):
        self.number = newNumber
        self.suit = newSuit


class Table(object):
    def __init__(self):
        self.bet = 0
        self.cards = []

    def get_cards(self):
        print("\nTable has")
        if (len(self.cards) <= 0):
            print("No Cards")
        else:
            for c in self.cards:
                print(c.number, c.suit)
