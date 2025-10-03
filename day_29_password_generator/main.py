from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password} \n")
        website_input.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)

# Website
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=42)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

# Email/password
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = Entry(width=42)
email_input.insert(0, "mickaelriss@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=23)
password_input.grid(row=3, column=1)
password_button = Button(text="Generate Password", bd=0)
password_button.grid(row=3, column=2)

# Add password
add_password = Button(text="Add Password", bd=0, width=40, command=save)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()