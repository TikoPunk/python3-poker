import sys
import random


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
        print("Table has")
        for c in self.cards:
            print(c.getNumber(), c.getSuit())


class Card(object):
    def __init__(self, newNumber, newSuit):
        self.number = newNumber
        self.suit = newSuit

    def getNumber(self):
        return self.number

    def getSuit(self):
        return self.suit


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

    def getDead(self):
        return self.dead

    def setCards(self, card):
        self.cards.extend(card)

    def getCards(self):
        print("\n", self.getName(), "has", len(self.cards), "cards\n")
        for c in self.cards:
            print(c.getNumber(), c.getSuit())


def makebet(bet, playerBet):
    if bet == playerBet:
        newBet = input("Bet?: \nCheck(c) Fold(f), or number for bet: ")

    else:
        newBet = input("Bet?: \nMatch(m), Fold(f), or number for bet: ")

    if newBet == "q":
        sys.exit("Bye")

    if newBet == "f":
        return "f"

    if newBet.isnumeric():
        newBet = int(newBet)
        if playerBet < bet:
            print("Whoa, either fold or match")
        if newBet is not bet:
            return newBet

    return bet


def IsOut(players):
    returnList = []

    for p in players:
        if p.getIn() is not False:
            returnList.append(p)
        # else:
        #    print("Goodbye", p.getName())

    return returnList


def shuffle(deck):
    newDeck = []
    counter = []
    for i in range(52):
        counter.append(i)

    while len(newDeck) != 52:
        randomInt = random.randint(0, 51)

        if counter[randomInt] is not False:
            newDeck.append(deck[randomInt])
            counter[randomInt] = False

    return newDeck


def getCard(deck, num):

    cards = []
    newDeck = deck

    for i in range(num):
        cards.append(newDeck[-1])
        newDeck.pop()

    return cards, newDeck


def mainGame(players, tab, deck, turn):

    for p in players:
        cards = []
        if turn == 0:
            cards, deck = getCard(deck, 2)
            p.setCards(cards)

        # Flop
        elif turn == 1:
            print("\nFlop\n\n")
            cards, deck = getCard(deck, 3)
            tab.setCards(cards)
            tab.getCards()

        # Turn
        elif turn == 2:
            print("\nTurn\n\n")
            cards, deck = getCard(deck, 1)
            tab.setCards(cards)
            tab.getCards()

        # River
        else:
            print("\nRiver\n\n")
            cards, deck = getCard(deck, 1)
            tab.setCards(cards)
            tab.getCards()

        p.getCards()
        print("tableBet is", tab.getBet(), "\n\n")
        print(p.getName(), "'s turn\n", sep='')
        # This is where they decide to fold, bet or match
        decision = makebet(tab.getBet(), p.getBet())
        if decision == "f":
            p.setIn(False)

        else:
            tab.setBet(decision)
            p.setBet(tab.getBet())
        print(p.getName(), "'s bet is ", p.getBet(), sep='')

    return tab, IsOut(players), deck


# Main start
print("\nTexas Hold em\n\n")

players = []

startingMoney = 10000

for i in range(int(input("How many players?:"))):
    players.append(Player(input("What is your name?:"), 20000))
    print("Welcome", players[i].getName(), "\n")

bigBlind = 800
smallBlind = int(bigBlind / 2)
# Main Game
print("Players are starting off at", startingMoney)
print("With", bigBlind, "big blinds and", smallBlind, "small blinds")

turn = 0
playersBackup = players

num = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
deck = []

i = 0
while (len(deck) < 52):
    for n in num:
        deck.append(Card(n, suit[i]))

    i += 1

deck = shuffle(deck)

tab = Table()


while(len(players) > 1):
    # tableBet, players, deck = mainGame(players, tableBet, deck, turn)
    tab, players, deck = mainGame(players, tab, deck, turn)
    print("Num of Players is", len(players))
    turn += 1

    if turn == 3:
        print("\n\nShow hands\n\n")
        turn = 0
        players = playersBackup
        deck = shuffle(deck)
