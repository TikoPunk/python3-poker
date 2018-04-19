import sys
from classes import Table
from classes import Player
from classes import Card
from classes import Deck


def clear_screen():
    print(chr(27) + "[2J")


def make_bet(bet, playerBet):
    if bet == playerBet:
        new_bet = input("Bet?: \nCheck(c) Fold(f), or number for bet: ")

    else:
        new_bet = input("Bet?: \nMatch(m), Fold(f), or number for bet: ")

    if new_bet == "q":
        sys.exit("Bye")

    if new_bet == "f":
        return "f"

    if new_bet.isnumeric():
        new_bet = int(new_bet)
        if new_bet < bet:
            print("Whoa, either fold or match")
            make_bet(bet, playerBet)
        if new_bet is not bet:
            return new_bet

    return bet


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
cards = []

i = 0
while (len(cards) < 52):
    for n in num:
        cards.append(Card(n, suit[i]))

    i += 1

deck = Deck(cards)
deck.shuffle()
tab = Table()


while(len(players) > 1):
    clear_screen()
    print("\nGame Start\n")

    cards = []

    # Flop
    if turn is 1:
        print("\nFlop\n\n")
        cards = deck.get_cards(3)

    # Turn
    elif turn is 2:
        print("\nTurn\n\n")
        cards = deck.get_cards(1)

    # River
    elif turn is 3:
        print("\nRiver\n\n")
        cards = deck.get_cards(1)

    tab.cards.extend(cards)

    for p in players:
        # Skip is player is out
        if p.In is False:
            continue

        if len([p for p in players if p.In]) is 1:
            print("\n\n", p.name, "Won the pot\n\n")
            turn = 3
            break

        if turn == 0:
            cards = deck.get_cards(2)
            p.cards.extend(cards)

        tab.print_cards()
        p.print_cards()
        print("Table bet is", tab.bet, "\n\n")
        print(p.name, "'s turn\n", sep='')

        # This is where they decide to fold, bet or match
        decision = make_bet(tab.bet, p.bet)
        if decision == "f":
            p.In = False
            p.bet = "Is Out"

        else:
            tab.bet = decision
            p.bet = tab.bet
        print(p.name, "'s bet is ", p.bet, sep='')

    turn += 1

    if turn == 4:
        print("\n\nShow hands\n\n")
        input("Press Enter to continue...")

        # Set everything back to nothing
        turn = 0
        for p in players:
            p.In = True
            p.cards = []
        deck.shuffle()
        tab.cards = []
