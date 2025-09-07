import os
import random
from game_data import data
from art import logo, vs

def clean_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
    print(logo)

def pick_data(exclude=None):
    choice = random.choice(data)
    while exclude and choice == exclude:
        choice = random.choice(data)
    return choice

def compare_values(a, b, points):
    guess = input("Who has more followers? Type 'A' or 'B':     ").lower()
    while guess != 'a' and guess != 'b':
        guess = input("I don't understand, please type 'A' or 'B':     ").lower()

    a_win = a["follower_count"] > b["follower_count"]
    clean_terminal()
    if (guess == "a" and a_win) or (guess == "b" and not a_win):
        points += 1
        print(f"You're right! {a["name"]} has {a["follower_count"]}M and {b["name"]} has {b["follower_count"]}M. Current score: {points}")
        return points, True
    else:
        print(f"Sorry, that's wrong. {a["name"]} has {a["follower_count"]}M and {b["name"]} has {b["follower_count"]}M. Final score: {points}")
        return points, False

def play():
    score = 0
    continue_playing = True
    value_a = pick_data()
    value_b = pick_data(exclude=None)

    while continue_playing:
        print(f"Compare A: {value_a["name"]}, {value_a["description"]}, from {value_a["country"]}\n")
        print(vs)
        print(f"\nCompare B: {value_b["name"]}, {value_b["description"]}, from {value_b["country"]}")

        score, continue_playing = compare_values(value_a, value_b, score)

        if continue_playing:
            value_a = value_b
            value_b = pick_data(exclude=None)

play()