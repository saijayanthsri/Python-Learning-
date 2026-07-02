print("Welcome to the secret auction program.")
name = input("Enter your name:")
price = int(input("Enter your bid:$"))

bid={}

def auction(name,price):
    bid[name]=price

while True:
    auction(name,price)
    more_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders=='no':
        break
    name = input("Enter your name:")
    price = int(input("Enter your bid:$"))

auction_list = list(bid)
n = len(auction_list)
highest_bidder = auction_list[0]
highest_bid = bid[highest_bidder]

for bidder in bid:
    current_bid = bid[bidder]

    if current_bid > highest_bid:
        highest_bid = current_bid
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

