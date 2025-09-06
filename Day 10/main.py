logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

operators = ['+', '-', '*', '/',]

def add(n1, n2):
    return round((n1 + n2), 4)

def subtract(n1, n2):
    return round((n1 - n2), 4)

def multiply(n1, n2):
    return round((n1 * n2), 4)

def divide(n1,n2):
    return round((n1 / n2), 4)

def calculate(n1, n2, op):
    match op:
        case "+":
            return add(n1, n2)
        case "-":
            return subtract(n1, n2)
        case "*":
            return multiply(n1, n2)
        case _:
            return divide(n1,n2)


print(logo)

continue_calculate = True
continue_or_stop = 'n'
result = 0

while continue_calculate:
    if continue_or_stop == 'n':
        number_1 = float(input("What's the first number?     "))

    for op in operators:
        print(f"{op}\n")

    operator = input("Pick and operation:  ")
    while not operator in operators:
        operator = input("Pick and operation:  ")

    number_2 = float(input("What's the second number?    "))

    if continue_or_stop == 'n':
        result = calculate(number_1, number_2, operator)
    elif continue_or_stop == 'y':
        result = calculate(result, number_2, operator)
    else:
        continue_calculate = False
    print(f"{number_1} {operator} {number_2} = {result}")
    continue_or_stop = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or any other key to stop the calculator:     ")
