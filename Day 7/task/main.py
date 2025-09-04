import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
number_of_letters = len(chosen_word)

for position in range(number_of_letters):
    placeholder += "_"

print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []

while not game_over:

    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in chosen_word and guess not in correct_letters:
        print("Good guess!")
    elif guess in chosen_word and guess in correct_letters:
        print(f"You've already guessed {guess}.")
    else:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if lives == 0:
        game_over = True
        print(f"************************************ SORRY... YOU LOSE ************************************\n")
    elif "_" not in display:
        game_over = True
        print(f"************************************ CONGRATULATION! IT'S A WIN! ************************************\n")
    else:
        print(stages[lives])
        print(f"************************************ {lives} / 6 LIVES LEFT ************************************\n")
        print(f"Word to guess: {display}")