import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

letters = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What's your name?").upper()

# phonetic_code = [value for (index, value) in letters.items() if index in name]
phonetic_code = [letters[value] for value in name]

print(phonetic_code)