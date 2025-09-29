from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

value = 0

input = Entry(width=10)
input.grid(row=0, column=1)

mesure = Label(text="Miles", font=("Arial", 12))
mesure.grid(row=0, column=2)

is_equal = Label(text="is equal to", font=("Arial", 12))
is_equal.grid(row=1, column=0)
is_equal.config(padx=8, pady=8)

miles = Label(text=f"{value}", font=("Arial", 12))
miles.grid(row=1, column=1)
miles.config(padx=8, pady=8)

km = Label(text="km", font=("Arial", 12))
km.grid(row=1, column=2)
km.config(padx=8, pady=8)

def button_clicked():
    value_input = input.get()
    answer = float(value_input) * 1.609344
    miles.config(text=f"{answer}")

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()