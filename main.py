import sys
import random
from table import Table
from player import Player
from card import Card


def countPlayers(players):
    i = 0
    for p in players:
        if p.getIn() is True:
            i += 1

    return i


def clearScreen():
    print(chr(27) + "[2J")


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
        if newBet < bet:
            print("Whoa, either fold or match")
            makebet(bet, playerBet)
        if newBet is not bet:
            return newBet

    return bet


def IsOut(players):
    returnList = []

    for p in players:
        if p.getIn() is not False:
            returnList.append(p)

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


# Main start
print("\nTexas Hold em\n\n")

players = []

startingMoney = 20000

for i in range(int(input("How many players?:"))):
    players.append(Player(input("What is your name?:"), startingMoney))
    print("Welcome", players[i].getName(), "\n")

bigBlind = 400
smallBlind = int(bigBlind / 2)

# Main Game
print("Players are starting off at", startingMoney)
print("With", bigBlind, "big blinds and", smallBlind, "small blinds")

turn = 0

num = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

# Create the deck
deckBackup = []

i = 0
while (len(deckBackup) < 52):
    for n in num:
        deckBackup.append(Card(n, suit[i]))

    i += 1

deck = shuffle(deckBackup)

tab = Table()


while(len(players) > 1):
    clearScreen()
    print("\nGame Start\n")

    cards = []

    # Flop
    if turn is 1:
        print("\nFlop\n\n")
        cards, deck = getCard(deck, 3)

    # Turn
    elif turn is 2:
        print("\nTurn\n\n")
        cards, deck = getCard(deck, 1)

    # River
    elif turn is 3:
        print("\nRiver\n\n")
        cards, deck = getCard(deck, 1)

    tab.setCards(cards)

    for p in players:
        # Skip is player is out
        if p.getIn() is False:
            continue

        # Check if the last player
        if (countPlayers(players) is 1):
            print("\n\n", p.getName(), "Won the pot\n\n")
            turn = 2
            break

        if turn == 0:
            cards, deck = getCard(deck, 2)
            p.setCards(cards)

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

    turn += 1

    if turn == 3:
        print("\n\nShow hands\n\n")
        input("Press Enter to continue...")
        turn = 0
        for p in players:
            p.setIntoTrue()
        deck = shuffle(deckBackup)
