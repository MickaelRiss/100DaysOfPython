print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

print(f"{bill}")
match size:
    case "S":
        bill += 15
    case "M":
        bill += 20
    case "L":
        bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

bill += 1 if extra_cheese == 'Y' else 0

print(f"Your final bill is: ${bill}.")