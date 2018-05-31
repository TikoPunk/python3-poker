import sys
import colorama
from colorama import Fore, Back, Style
from classes import Table
from classes import Player
from treys import Deck
from treys import Evaluator
from collections import OrderedDict
from pprint import pprint


def clear_screen():
    print(chr(27) + "[2J")


def check_num_input(prompt):
    ret = input(prompt)
    try:
        ret = int(ret)
        if ret < 1 or ret > 6:
            ret = check_num_input("Must be more than 1 and 6 or less:")
        return ret
    except ValueError:
        return check_num_input("Number be be a digit:")


def check_input(prompt):
    ret = input(prompt)
    try:
        ret = int(ret)
        return ret
    except ValueError:
        if ret not in ["c", "m", "f", "a"]:
            return check_input("Not valuable c, m, f, a or number:")
        else:
            return ret


def action(turn, players, tab, deck):
    if turn == 0:
        print("drawing 2 cards for players")
        for p in players:
            p.cards.extend(deck.draw(2))

    elif turn == 1:
        print("drawing 3 cards for table")
        tab.cards.extend(deck.draw(3))

    else:
        print("drawing 1 card for table")
        tab.cards.append(deck.draw(1))

    return players, tab, deck


def bet(player, player_bet, highBet):
    if highBet == 0:
        player_bet = check_input(
            "Bet?: \nCheck(c), Fold(f), All In(a), or number for bet: ")
    else:
        player_bet = check_input(
            "Bet?: \nMatch(m), Fold(f), All In(a), or number for bet: ")

    if player_bet == "f":
        sys.exit("Fold")

    elif player_bet in ["c", "m"]:
        player_bet = highBet

    player_bet = int(player_bet)

    if player.money - player_bet < 0:
        player_bet, highBet = bet(player, player_bet, highBet)

    while player_bet < highBet:
        print("Bet needs to be equal or higher than previous bet")
        player_bet, highBet = bet(player, player_bet, highBet)

    highBet = player_bet

    return player_bet, highBet



# Main start
print("\nTexas Hold em\n\n")

players = []

starting_money = 20000
num = check_num_input("How many players? Can only be 6 or less:")


for i in range(num):
    players.append(Player(input("What is your name?:"), starting_money))
    print("Welcome", players[i].name, "\n")

big_blind = 400
small_blind = big_blind // 2

# Main Game
print("Players are starting off at", starting_money)
print("With", big_blind, "big blinds and", small_blind, "small blinds")

tab = Table()


colorama.init()


print("\nGame Start\n")

turn = 0
highBet = 0
player_bet = 0
deck = Deck()
deck.shuffle()


while turn < 4:
    print("Turn is", turn, "\n")
    players, tab, deck = action(turn, players, tab, deck)

    tab.print_cards()
    turn += 1
    out = False

    while (True):
        for p in players:
            if p.bet == highBet:
                highBet = 0

                for p in players:
                    p.bet = None

                out = True

                break

            print("\n{}'s turn\n".format(p.name))
            p.print_cards()

            player_bet, highBet = bet(p, player_bet, highBet)

            try:
                p.money = p.money - (player_bet - p.bet)
            except TypeError:
                p.money = p.money - player_bet

            p.bet = player_bet

            print(Fore.BLUE, "Player", p.name, "has", p.money)

            print(Fore.RED + "\n{}'s bet is {}.".format(p.name, p.bet))
            print(Style.RESET_ALL)

        if out is True:
            break

print("Show hands")
evaluator = Evaluator()

scores = {}

tab.print_cards()
print()

for p in players:
    p.print_cards()
    print()
    scores[evaluator.evaluate(tab.cards, p.cards)] = p.name

d = OrderedDict(sorted(scores.items(), key=lambda t: t[0]))
items = list(d.items())
for i in items:
    print(i)
    p_score = i[0]
    p_class = evaluator.get_rank_class(p_score)
    print(evaluator.class_to_string(p_class))
