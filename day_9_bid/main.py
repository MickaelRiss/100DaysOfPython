logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
list_of_bids = {}
continue_bidding = True

def compare_bids(bids):
    highest_value = 0
    winner = ""

    for key in bids:
        if bids[key] > highest_value:
            highest_value = bids[key]
            winner = key

    print(f"THe winner is {winner} with a bid of ${highest_value}")


while continue_bidding:
    name = input("What is your name?:   ")
    bid = int(input("What is your bid? $   "))
    list_of_bids[name] = bid
    add_bidder = input("Are there any others bidders? Type 'yes' or 'no'    ")
    if add_bidder == 'no':
        continue_bidding = False
        compare_bids(list_of_bids)
    elif add_bidder == 'yes':
        print("\n" * 20)