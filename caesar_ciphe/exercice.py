#def greet_with_and_location(name, location):
#    print(f"My name is {name}")
#    print(f"I'm living in {location}")

#greet_with_and_location(location="Paris", name="Mickael")

def calculate_true(name1, name2):
    total = 0
    for letter in name1:
            total += 1 if letter.upper() in "TRUE" else 0
    for letter in name2:
            total += 1 if letter.upper() in "TRUE" else 0
    return total

def calculate_love(name1, name2):
    total = 0
    for letter in name1:
            total += 1 if letter.upper() in "LOVE" else 0
    for letter in name2:
            total += 1 if letter.upper() in "LOVE" else 0
    return total

def calculate_love_score(name1, name2):
    true = str(calculate_true(name1, name2))
    love = str(calculate_love(name1, name2))
    result = true + love
    print(f"{result}")

calculate_love_score("Kanye West", "Kim Kardashian")