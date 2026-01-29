print("Auction Program....")

auction = {}

def get_valid_bid():
    while True:
        try:
            bid = int(input("What's your bid? ₹ "))
            if bid <= 0:
                print("Bid must be greater than zero.")
                continue
            return bid
        except ValueError:
            print("Please enter a valid number.")

while True:
    name = input("\nWhat's your name? ").strip().title()
    bid = get_valid_bid()

    # duplicate bidders
    if name in auction:
        if bid > auction[name]:
            print(f"Updating bid for {name}.")
            auction[name] = bid
        else:
            print(f"Bid must be higher than your previous bid of ₹{auction[name]}.")
    else:
        auction[name] = bid

    more_bidders = input("Are there any other bidders? (yes/no): ").lower().strip()
    if more_bidders in ("no", "n"):
        break

# highest bid
highest_bid = max(auction.values())
winners = [name for name, bid in auction.items() if bid == highest_bid]

print("\nAuction Summary:")
for name, bid in auction.items():
    print(f"- {name}: ₹{bid}")

print("\nResult:")
if len(winners) == 1:
    print(f"The winner is {winners[0]} with a bid of ₹{highest_bid}")
else:
    print(f"It's a tie between {', '.join(winners)} with a bid of ₹{highest_bid}")
