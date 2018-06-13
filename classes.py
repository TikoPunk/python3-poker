from treys import Card


class Player(object):
    def __init__(self, newName, newMoney):
        self.name = newName
        self.money = newMoney
        self.bet = None
        self.In = True
        self.left_player = None
        self.dead = False
        self.cards = []

    def print_cards(self):
        print(self.name, "has", len(self.cards), "cards")
        Card.print_pretty_cards(self.cards)


class Table(object):
    def __init__(self):
        self.bet = 0
        self.turn = -1
        self.cards = []
        self.pot = 0

    def print_cards(self):
        print("\nTable has")
        if (len(self.cards) <= 0):
            print("No Cards")
        else:
            Card.print_pretty_cards(self.cards)
