import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play = 0
bot_choice = 0
actions = [rock,paper,scissors]
player_point = 0
bot_point = 0

while play == 0:
    print(f"Player : {player_point} | Bot : {bot_point}")
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

    if player_choice in [0,1,2]:
        bot_choice = random.randint(0,2)
        print(actions[player_choice])
        print(f"Computer chose:\n {actions[bot_choice]}")

        if player_choice == bot_choice:
            play= int(input("Equality, play again? Press 0 for Yes and 1 for No: "))
        elif player_choice == 0 and bot_choice == 1:
            play = int(input("You lose, play again? Press 0 for Yes and 1 for No: "))
            bot_point += 1
        elif player_choice == 1 and bot_choice == 2:
            play = int(input("You lose, play again? Press 0 for Yes and 1 for No: "))
            bot_point += 1
        elif player_choice == 2 and bot_choice == 0:
            play = int(input("You lose, play again? Press 0 for Yes and 1 for No: "))
            bot_point += 1
        else:
            play = int(input("You win! Play again? Press 0 for Yes and 1 for No: "))
            player_point += 1
    else:
        print("Please press 0 or 1")

print("Congratulations, you won!") if player_point > bot_point else print("We are sorry... you lost :(")