# click library is here to use the click.clear() fucntion to clear the terminal screen.
import click
import art
print(art.logo)
stop_auction = False
players = {}

def auction(name,bid_amount):
    players[name] = bid_amount
    winner = max(players,key=players.get)

    return winner

while not stop_auction:
    name = input("What is your name? \n")
    bid_amount = int(input("Enter your Bid amount : \n"))
    next_player = input("If there are other users who want to bid then type 'yes' or type 'no'.").lower()

    winner = auction(name=name,bid_amount=bid_amount)

    if next_player == "no":
        stop_auction = True
        click.clear()
        print(f"The Auction winner is : {winner}")
    elif next_player == "yes":
        click.clear()