import random


class Player(object):
    def __init__(self, newName, newMoney):
        self.name = newName
        self.money = newMoney
        self.bet = 0
        self.In = True
        self.dead = False
        self.cards = []

    def print_cards(self):
        print("\n", self.name, "has", len(self.cards), "cards\n")
        for c in self.cards:
            print(c.number, c.suit)


class Table(object):
    def __init__(self):
        self.bet = 0
        self.cards = []

    def print_cards(self):
        print("\nTable has")
        if (len(self.cards) <= 0):
            print("No Cards")
        else:
            for c in self.cards:
                print(c.number, c.suit)


class Deck(object):
    def __init__(self, new_cards):
        self.cards = new_cards
        self.dead_cards = []

    def shuffle(self):

        self.cards.extend(self.dead_cards)
        self.dead_cards = []

        random.shuffle(self.cards)

    def get_cards(self, num):
        draw_cards = []

        for i in range(num):
            draw_cards.append(self.cards[-1])
            self.dead_cards.append(self.cards[-1])
            self.cards.pop()

        return draw_cards


class Card(object):
    def __init__(self, newNumber, newSuit):
        self.number = newNumber
        self.suit = newSuit
