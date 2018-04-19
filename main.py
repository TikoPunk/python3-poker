import sys
from classes import Table
from classes import Player
from treys import Deck
from treys import Evaluator


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
        evaluator = Evaluator()

        p1_score = evaluator.evaluate(tab.cards, players[0].cards)
        p2_score = evaluator.evaluate(tab.cards, players[1].cards)

        if p1_score < p2_score:
            print("Player 1 wins!\n")

        else:
            print("Player 2 wins!\n")
        input("Press Enter to continue...")

        # Set everything back to nothing
        turn = 0
        for p in players:
            p.In = True
            p.cards = []
        deck.shuffle()
        tab.cards = []
