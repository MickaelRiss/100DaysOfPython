print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age < 12:
        print("You are under 12 so you need to pay $5.")
    elif age >= 12 and age <= 18:
        print("You are between 12 and 18 so you need to $7")
    else:
        print("You are over 18 so you need to pay $18.")
else:
    print("Sorry you have to grow taller before you can ride.")

