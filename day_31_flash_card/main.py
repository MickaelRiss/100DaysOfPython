BACKGROUND_COLOR = "#B1DDC6"
import random
from tkinter import *
import pandas as pd

window = Tk()
window.title("Flash Card")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)
current_card = {}
translations = {}

# ---------------------- PICK RANDOM WORD ---------------------- #

try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/portuguese_words.csv")
    translations = df.to_dict(orient="records")
else:
    translations = df.to_dict(orient="records")

# ---------------------- FUNCTIONS ---------------------- #
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(translations)
    card.itemconfig(image, image=card_front_image)
    card.itemconfig(lang, text="Portuguese", fill="black")
    card.itemconfig(word, text=current_card["Portuguese"], fill="black")
    timer = window.after(3000, func=flip_card)
    
def flip_card():
    card.itemconfig(image, image=card_back_image)
    card.itemconfig(lang, text="French", fill="#FFFFFF")
    card.itemconfig(word, text=current_card["French"], fill="#FFFFFF")

def right():
    global translations
    translations.remove(current_card)
    data = pd.DataFrame(translations)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------- CARD ---------------------- #
card_front_image = PhotoImage(file="./images/card_front.png") 
card_back_image = PhotoImage(file="./images/card_back.png") 
card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = card.create_image(400, 263, image=card_front_image)
lang = card.create_text(400, 120, text="", font=("Ariel", 40, "italic"))
word = card.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

# ---------------------- WRONG ---------------------- #
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, bd=0, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# ---------------------- RIGHT ---------------------- #
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, bd=0, highlightthickness=0, command=right)
right_button.grid(row=1, column=1)

# ---------------------- START APP ---------------------- #
timer = window.after(3000, func=flip_card)
next_card()
window.mainloop()