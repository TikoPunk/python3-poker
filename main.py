import sys
from classes import Table
from classes import Player
from treys import Deck
from treys import Evaluator
from collections import OrderedDict


def clear_screen():
    print(chr(27) + "[2J")


def make_bet(bet, playerBet):
    if bet == playerBet or playerBet is 0:
        new_bet = input(
            "Bet?: \nCheck(c), Fold(f), All In(a), or number for bet: ")

    else:
        new_bet = input(
            "Bet?: \nMatch(m), Fold(f), All In(a), or number for bet: ")

    if new_bet is "q":
        sys.exit("Bye")

    elif new_bet is "f":
        return "f"

    elif new_bet is "a":
        print("WOW, all in", p.money)
        bet = p.money

    elif new_bet.isnumeric():
        new_bet = int(new_bet)
        if new_bet < bet:
            print("Whoa, either fold or match")
            make_bet(bet, playerBet)
        if new_bet is not bet:
            return new_bet

    return bet


def bubbleSort(d):

    kL = []
    vL = []

    for key, val in sorted(d.items()):
        kL.append(key)
        vL.append(val)

    for i in range(len(d)):
        for index, (key, val) in enumerate(zip(kL, vL)):
            try:
                if val < vL[index + 1]:
                    vL[index], vL[index + 1] = vL[index + 1], vL[index]
                    kL[index], kL[index + 1] = kL[index + 1], kL[index]
            except IndexError:
                break

    return kL, vL



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

deck = Deck()
deck.shuffle()
tab = Table()


while(len(players) > 1):
    clear_screen()
    print("\nGame Start\n")

    # Flop
    if turn is 1:
        print("\nFlop\n\n")
        cards = deck.draw(3)
        tab.cards.extend(deck.draw(3))

    # Turn
    elif turn is 2:
        print("\nTurn\n\n")
        tab.cards.append(deck.draw(1))

    # River
    elif turn is 3:
        print("\nRiver\n\n")
        tab.cards.append(deck.draw(1))

    for p in players:
        # Skip is player is out
        if p.In is False:
            continue

        if len([p for p in players if p.In]) is 1:
            print("\n\n", p.name, "Won the pot\n\n")
            turn = 3
            break

        if turn == 0:
            p.cards.extend(deck.draw(2))

        tab.print_cards()
        p.print_cards()
        print("Table bet is", tab.bet, "\n")
        print("Table money is", tab.money, "\n\n")

        print(p.name, "'s turn\n", sep='')

        # This is where they decide to fold, bet or match
        if p.money > 0:
            decision = make_bet(tab.bet, p.bet)

        else:
            print("Skipping", p.name, "\n")
            continue

        if decision is "f":
            p.In = False
            p.bet = "Is Out"

        else:
            tab.bet = decision
            tab.money += tab.bet
            p.money -= tab.bet

            p.bet = tab.bet

        print(p.name, "'s bet is ", p.bet, sep='')
        print(p.name, "has", p.money)

    turn += 1

    if turn == 4:
        print("\n\nShow hands\n\n")
        evaluator = Evaluator()

        scores = {}

        for p in players:
            # scores.append([evaluator.evaluate(tab.cards, p.cards), p])
            scores[evaluator.evaluate(tab.cards, p.cards)] = p.name

        d = OrderedDict(sorted(scores.items(), key=lambda t: t[0]))
        items = list(d.items())
        for p in players:
            if p.name is items[0][1]:
                print(p.name, "Gets", tab.money)
                print(p.money, "now")
                p.money += tab.money
                print(p.money, "Adding pot")
                break

        input("Press Enter to continue...")

        # Get rid of players with no no money
        # Set everything back to nothing
        turn = 0
        player_back = []
        for p in players:
            p.In = True
            p.cards = []
            if p.money > 0:
                player_back.append(p)
            else:
                print(p.name, "Good bye\n")

        deck.shuffle()
        tab.cards = []
        tab.bet = 0
        tab.money = 0
        players = player_back

print("\n\n", players[0].name, " Wins everything\n\n", sep='')
