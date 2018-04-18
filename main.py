import sys
import random
from table import Table
from player import Player
from card import Card


def countPlayers(players):
    i = 0
    for p in players:
        if p.In:
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
        if p.In:
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

starting_money = 20000

for i in range(int(input("How many players?:"))):
    players.append(Player(input("What is your name?:"), starting_money))
    print("Welcome", players[i].name, "\n")

big_blind = 400
small_blind = big_blind // 2

# Main Game
print("Players are starting off at", starting_money)
print("With", big_blind, "big blinds and", small_blind, "small blinds")

turn = 0

num = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

# Create the deck
deck_backup = []

i = 0
while (len(deck_backup) < 52):
    for n in num:
        deck_backup.append(Card(n, suit[i]))

    i += 1

deck = shuffle(deck_backup)

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

    # tab.setCards(cards)
    tab.cards.extend(cards)

    for p in players:
        # Skip is player is out
        if p.In is False:
            continue

        # Check if the last player
        if (countPlayers(players) is 1):
            print("\n\n", p.name, "Won the pot\n\n")
            turn = 2
            break

        if turn == 0:
            cards, deck = getCard(deck, 2)
            p.cards.extend(cards)

        tab.getCards()
        p.getCards()
        print("tableBet is", tab.bet, "\n\n")
        print(p.name, "'s turn\n", sep='')
        # This is where they decide to fold, bet or match
        decision = makebet(tab.bet, p.bet)
        if decision == "f":
            p.In = False
            p.bet = "Is Out"

        else:
            tab.bet = decision
            p.bet = tab.bet
        print(p.name, "'s bet is ", p.bet, sep='')

    turn += 1

    if turn == 3:
        print("\n\nShow hands\n\n")
        input("Press Enter to continue...")
        turn = 0
        for p in players:
            p.In = True
        deck = shuffle(deck_backup)
