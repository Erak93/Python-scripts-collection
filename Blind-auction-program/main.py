import os
from art import logo

print(logo)
bidders={}

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f'The winner is {winner} with ${highest_bid}')
    

auction_is_over=False

while auction_is_over==False:
    print("Welcome to simple auction system. Please insert your name and bid.")
    name=input("Name: ")
    bid=int(input("Bid: $"))
    bidders[name]=bid
    #print(bidders)
    next_bidder=input("Are there any other bidders? Y/N:  ").upper()
    if next_bidder=="N":
        auction_is_over=True
        os.system('clear')
    else:
        os.system('clear')

find_highest_bidder(bidders)


