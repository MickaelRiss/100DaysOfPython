def is_leap_year(year):
    if (year / 4).is_integer():
        if (year / 100).is_integer():
            if (year / 400).is_integer():
                return print(f"{year} is leap")
            else:
                return print(f"{year} is not leap")
        else:
            return print(f"{year} is leap")
    else:
        return print(f"{year} is not leap")

continue_testing = True

while continue_testing:
    year_try = int(input("Give us a year: "))
    is_leap_year(year_try)
    try_again = input("Do you want to test another year? Type 'yes' or 'no' ")
    if try_again == 'no':
        continue_testing = False