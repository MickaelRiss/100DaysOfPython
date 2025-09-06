import random

logo = r'''
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
'''

number = random.randrange(1,101)
attempts = 0
guess = 0

print(logo)
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("First, choose a difficulty: Type 'easy' or 'hard':   ")
while difficulty != 'easy' and difficulty != 'hard':
    difficulty = input("Please type 'easy' or 'hard':   ")

attempts = 10 if difficulty == 'easy' else 5

while attempts != 0 and number != guess:
    print(f"You have {attempts} attempts.")
    guess = int(input("Make a guess: "))
    if number > guess:
        print("Too low.\n")
        attempts -= 1
    elif number < guess:
        print("Too high.\n")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}.\n")

print("Refresh if you want to play again :)")