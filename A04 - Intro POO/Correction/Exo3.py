# pip install colorama, termcolor

from Card import Card, Deck
from termcolor import colored, cprint

c = Card(4, "4", "♠", "spade", "black")

# Exemple avec fond blanc
print(c.card_color.background_color + c.__str__())
# Exemple sans fond
print(c)
# Exemple avec cprint
cprint(c, c.card_color.forground_color, "on_white")

d = Deck()
d.init52_cards()
d.shuffle()

MAX_SCORE = 5
player_score = 0
cpu_score = 0
end = False
start_card = d.draw()

while not end:
    print(f"Current card : {start_card}")
    signe = input(f"Choose between > or < or =  ")
    new_card = d.draw()
    print(f"Card draw : {new_card}")
    if signe == "<":
        if new_card < start_card:
            player_score += 1
            print("Player score")
        else:
            cpu_score += 1
            print("CPU score")
    elif signe == ">":
        if new_card > start_card:
            player_score += 1
            print("Player score")
        else:
            cpu_score += 1
            print("CPU score")

    elif signe == "=":
        if start_card.is_equal_value(new_card):
            player_score += 1
            print("Player score")
        else:
            cpu_score += 1
            print("CPU score")

    else:
        print("False instruction => CPU score")
        cpu_score += 1

    if cpu_score >= MAX_SCORE or player_score >= MAX_SCORE:
        end = True

    start_card = new_card

    print(f"Player : {player_score} | CPU {cpu_score}")

if player_score >= cpu_score:
    print("Player Win")
else:
    print("CPU Win")
