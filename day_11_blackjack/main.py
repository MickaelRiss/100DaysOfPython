import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

# Calculate sum of cards : ["A",5]
def count_cards(player_cards):
    sum_cards = 0
    for card in player_cards:
        if card in ["J","Q","K","A"]:
           if card != "A":
               sum_cards += 10
           else:
               sum_cards += choose_as_value(player_cards)
        else:
            sum_cards += card
    return sum_cards

# Choose rather 1 or 11 for A
def choose_as_value(player_cards):
    list_of_int = []
    a_in_hand = 0
    value = 0
    for card in player_cards:
        if isinstance(card, int):
            list_of_int.append(card)
        elif card in ["J","Q","K"]:
            list_of_int.append(10)
        else:
            a_in_hand += 1

    if a_in_hand > 1:
        # We can't have A = 11 so return numbers of A in hand
        return a_in_hand
    else:
        if sum(list_of_int) > 10:
            return 1
        elif sum(list_of_int) == 10:
            return 11
        else:
            while int(value) != 1 and int(value) != 11:
                value = input("Would you like your 'A' to become 1 or 11?   ")
            return int(value)

# Compare cards between players
def compare_players_cards(player_cards, bank_cards):
    if count_cards(bank_cards) > 21:
        print("YOU WIN !\n")
    elif count_cards(player_cards) == count_cards(bank_cards):
        print("DRAW !\n")
    elif count_cards(player_cards) < count_cards(bank_cards):
        print("Sorry, you loose...\n")
    else:
        print("YOU WIN !\n")

# Pick a card
def pick_card(player_cards):
    new_card = random.choice(cards)
    player_cards.append(new_card)
    return player_cards

# Is it a blackjack?
def is_blackjack(sum_hand):
    return 1 if sum_hand == 21 else 0

# Distribute player cards
def distribute_cards(player,bank):
    for _ in range(2):
        pick_card(player)
        pick_card(bank)

    print(f"Your cards :  {player}")
    print(f"Computer first card :  {bank[0]}")

    while count_cards(player) < 21:
        if input("Type 'y' to get another card:    ") == 'y':
            pick_card(player)
            print(f"Your cards :  {player}")
        else:
            return player, bank
    return player, bank

# Pick bank cards
def pick_bank_cards(bank):
    while count_cards(bank) < 17:
        pick_card(bank)
        print(f"Bank cards: {bank}")

# Play BlackJack
continue_playing = True
answer = input("Are you ready to start a new game of BlackJack ? Type 'y' for yes and 'n' for no:    ")

if answer == 'n':
    print("Too bad! Have a good day :)")
    continue_playing = False
else:
    if answer == 'y':
        print("Cool! Let's go \n")
    else:
        print(f"I didn't understand '{answer}' but let's start a game! :)\n")

# Ask if player wants to play again or not
while continue_playing:
    print(logo)
    player_hand = []
    bank_hand = []
    distribute_cards(player_hand, bank_hand)
    print(f"Your score : {count_cards(player_hand)}")
    print(f"Bank hand : {bank_hand})")

    if is_blackjack(count_cards(player_hand)):
        print("BLACKJACK ! YOU WIN !\n")
    elif count_cards(player_hand) > 21:
        print("Sorry, you loose...\n")
    else:
        pick_bank_cards(bank_hand)
        compare_players_cards(player_hand, bank_hand)

    answer = input("Do you want to play again ? Type 'y' for yes and 'n' for no:    ")
    while answer != 'y' and answer != 'n':
        answer = input("Sorry, I don't understand, do you want to play a game of BlackJack? Type 'y' for yes and 'n' for no:    ")

    if answer == 'n':
        continue_playing = False