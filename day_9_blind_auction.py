import os

logo = '''
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

print("Welcome to the secret auction program.")

new=[]

def add_new_bidder(name, bid):
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = bid
    new.append(new_bidder)

while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_new_bidder(name, bid)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == "no":
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

highest_bid = 0
winner = ""
for bidder in new:
    if bidder["bid"] > highest_bid:
        highest_bid = bidder["bid"]
        winner = bidder["name"]

print(f"The winner is {winner} with a bid of ${highest_bid}.")