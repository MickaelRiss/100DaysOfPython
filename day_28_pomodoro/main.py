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
reps = 1

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_timer.config(text="Long break", fg=RED)
        count_down(long_break_sec, start_timer)
    elif reps % 2 == 0:
        title_timer.config(text="Short break", fg=PINK)
        count_down(short_break_sec, start_timer)
    else:
        title_timer.config(text="Work", fg=GREEN)
        count_down(work_sec, start_timer)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = int(count / 60)
    count_sec = round(count % 60, 2)

    if count_sec in range(0,10):
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# Create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
title_timer = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN, pady=16)
title_timer.grid(row=0, column=1)

# Image
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,140, text="25:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Button : Start/ Reset
def start_clicked():
    seconds = WORK_MIN * 60
    count_down(seconds)

start = Button(text="Start", bg=YELLOW, highlightthickness=0, bd=0, command=start_clicked)
start.grid(row=2, column=0)
reset = Button(text="Reset", bg=YELLOW, highlightthickness=0, bd=0)
reset.grid(row=2, column=3)

window.mainloop()