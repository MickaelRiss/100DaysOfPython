from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# Create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
title = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN, pady=16)
title.grid(row=0, column=1)

# Image
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100,140, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Button : Start/ Reset
start = Button(text="Start", bg=YELLOW, highlightthickness=0, bd=0)
start.grid(row=2, column=0)
reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, bd=0)
reset.grid(row=2, column=3)

# Checkmark
checkmark = Label(text="✔", fg=GREEN, font=(FONT_NAME, 16, "bold"), bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()